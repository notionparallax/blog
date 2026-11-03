#!/usr/bin/env python3
"""Publish this blog's posts as a blyg: https://blygger.org/spec/0.4/

Every post in _posts with a `blyg_id` in its front matter is a blyg thread.
Versions come from git history: version 1 is the post as it stood when it got
its id, and each later commit that changes its title or body (or the version of
something it quotes) is the next version. Deleting a post, or setting
`published: false`, withdraws it.

    python _blyg/blyg.py assign-ids        give posts without a blyg_id a new one
    python _blyg/blyg.py prepare --write   before `jekyll build` (rewrites [[id]] in _posts: CI only)
    python _blyg/blyg.py build             after `jekyll build`: blyg.json, items/, blyg-feed.xml
    python _blyg/blyg.py import URL        snapshot a remote blyg item so posts can link to or quote it
    python _blyg/blyg.py send-mentions     send the Webmentions `build` queued (after deploy)
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import secrets
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import yaml
from liquid import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
INCLUDES = ROOT / "_includes"
IMPORTS = ROOT / "_blyg" / "imports"
OUT = ROOT / "_blyg_out"
SITE = ROOT / "_site"
DUMP = "blyg-posts.json"  # written by Jekyll from blyg-posts.json at the repo root, deleted by `build`
FEED = "blyg-feed.xml"  # feed.xml stays the plain RSS feed existing subscribers already read
WATCHED = ("_posts", "_blyg/imports")

CONFIG = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
ORIGIN = CONFIG["url"].rstrip("/") + "/"
AUTHOR = {"name": f'{CONFIG["author"]["first_name"]} {CONFIG["author"]["last_name"]}', "url": ORIGIN}
PROTOCOL = "0.4"
GENERATOR = "notionparallax-blyg/0.1.0"
GENERATOR_URL = "https://github.com/notionparallax/blog/tree/gh-pages/_blyg"
USER_AGENT = f"{GENERATOR} (+{ORIGIN})"
FEED_WINDOW = 50
LINK_PLACEHOLDER = "https://blyg.invalid/item/"
CI = os.environ.get("GITHUB_ACTIONS") == "true"

ID_ALPHABET = "0123456789abcdefghjkmnpqrstvwxyz"
ID = r"[0-9a-hjkmnp-tv-z]{26}"
ID_RE = re.compile(ID)
POST_NAME_RE = re.compile(r"^(\d{4})-(\d{1,2})-(\d{1,2})-(.+)\.(md|markdown|html)$")
FRONT_MATTER_RE = re.compile(r"\A---[ \t]*\r?\n(.*?\r?\n)?---[ \t]*(?:\r?\n|\Z)", re.S)
TIME_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{1,2}):(\d{2})(?::(\d{2}))?)?\s*(Z|[+-]\d{2}:?\d{2})?")

# The bracket grammar (§10.1): ![[id]] alone on a line quotes an item, [[id]] anywhere else links to it.
DIRECTIVE_RE = re.compile(rf"^\s*!\[\[({ID})(?:\s*\|((?:(?!\]\]).)*))?\]\]\s*$")
LINK_RE = re.compile(rf"(?<!!)\[\[({ID})(?:\s*\|((?:(?!\]\]).)*))?\]\]")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
HIGHLIGHT_RE = re.compile(r"\{%-?\s*highlight\s+(\w+)[^%]*-?%\}")
END_HIGHLIGHT_RE = re.compile(r"\{%-?\s*endhighlight\s*-?%\}")
CODE_SPAN_RE = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)")
INCLUDE_RE = re.compile(r"\{%-?\s*include\s+([^\s%'\"]+)\s*-?%\}")

TAG_RE = re.compile(r"""<[a-zA-Z][^\s/>]*(?:\s+[^\s=/>]+(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>]+))?)*\s*/?>""")
URL_ATTR_RE = re.compile(
    r"""(\s)(href|src|poster|cite|action|data|background|srcset|xlink:href)(\s*=\s*)("[^"]*"|'[^']*'|[^\s>]+)""", re.I
)
RAW_TEXT_RE = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")
BLOCK_TAG_RE = re.compile(r"(?i)</?(?:p|div|li|ul|ol|h[1-6]|blockquote|pre|tr|table|section|figure|figcaption|hr|br)\b[^>]*>")


class PublishError(Exception):
    pass


def warn(message: str) -> None:
    print(f"::warning::{message}" if CI else f"warning: {message}", file=sys.stderr)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def iso(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_time(value) -> datetime | None:
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day, tzinfo=timezone.utc)
    m = TIME_RE.match(str(value or "").strip())
    if not m:
        return None
    year, month, day, hour, minute, second, zone = m.groups()
    tz = timezone.utc
    if zone and zone != "Z":
        digits = zone[1:].replace(":", "")
        offset = timedelta(hours=int(digits[:2]), minutes=int(digits[2:]))
        tz = timezone(-offset if zone[0] == "-" else offset)
    return datetime(int(year), int(month), int(day), int(hour or 0), int(minute or 0), int(second or 0), tzinfo=tz)


def new_id() -> str:
    """128 random bits as 26 lowercase Crockford base32 characters (§5.1)."""
    n, chars = secrets.randbits(128), []
    for _ in range(26):
        chars.append(ID_ALPHABET[n & 31])
        n >>= 5
    return "".join(reversed(chars))


def split_post(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1) or "") or {}, text[m.end():]


def is_post(path: str) -> bool:
    return path.startswith("_posts/") and bool(POST_NAME_RE.match(path.rsplit("/", 1)[-1]))


def is_import(path: str) -> bool:
    return path.startswith("_blyg/imports/") and path.endswith(".json")


def post_files():
    for f in sorted(POSTS.rglob("*")):
        if f.is_file() and POST_NAME_RE.match(f.name):
            yield f


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=True
    ).stdout


# --- the bracket grammar -------------------------------------------------------------------------


@dataclass
class Ref:
    id: str
    label: str | None
    quote: bool  # ![[id]] (transclusion) rather than [[id]] (link)
    line: int
    end: int  # one past the last line a quote occupies, selection included
    span: tuple[int, int] | None  # columns of a link within its line
    selection: list[str] | None  # the attached blockquote of a partial quote


def _label(raw: str | None) -> str | None:
    return (raw or "").strip() or None


def scan(body: str) -> list[Ref]:
    """Find [[id]] links and ![[id]] quotes outside code, in document order."""
    lines, refs, fence, i = body.splitlines(), [], None, 0
    while i < len(lines):
        line = lines[i]
        if fence:
            m = FENCE_RE.match(line)
            if fence == "highlight":
                if END_HIGHLIGHT_RE.search(line):
                    fence = None
            elif m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            i += 1
            continue
        if m := FENCE_RE.match(line):
            fence, i = m.group(1), i + 1
            continue
        if HIGHLIGHT_RE.search(line):
            fence, i = "highlight", i + 1
            continue
        if m := DIRECTIVE_RE.match(line):
            end, selection = i + 1, None
            if end < len(lines) and lines[end].lstrip().startswith(">"):
                selection = []
                while end < len(lines) and lines[end].strip():  # CommonMark lazy continuation
                    selection.append(re.sub(r"^\s*>\s?", "", lines[end]).strip())
                    end += 1
            refs.append(Ref(m.group(1), _label(m.group(2)), True, i, end, None, selection))
            i = end
            continue
        masked = CODE_SPAN_RE.sub(lambda c: " " * len(c.group(0)), line)
        for m in LINK_RE.finditer(masked):
            refs.append(Ref(m.group(1), _label(m.group(2)), False, i, i + 1, m.span(), None))
        i += 1
    return refs


# --- imported items ------------------------------------------------------------------------------


@dataclass
class Imported:
    origin: str
    manifest: dict
    doc: dict

    @property
    def page(self) -> str:
        """Where a link or a Webmention should point (§15.2): the page if known, else the item document."""
        if self.doc.get("page"):
            return urllib.parse.urljoin(self.origin, self.doc["page"])
        return item_url(self.origin, self.manifest, self.doc["id"])


def item_url(origin: str, manifest: dict, item_id: str) -> str:
    return urllib.parse.urljoin(origin, (manifest.get("item") or "items/{id}.json").replace("{id}", item_id))


def load_imports() -> dict[str, list[Imported]]:
    found: dict[str, list[Imported]] = {}
    for f in sorted(IMPORTS.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        imp = Imported(data["origin"], data.get("manifest") or {}, data["document"])
        found.setdefault(imp.doc["id"], []).append(imp)
    return found


def resolve(ref: Ref, local: dict, imports: dict[str, list[Imported]], where: str) -> Imported | None:
    """None for one of our own posts, else the imported snapshot (§10.2 resolution order)."""
    remote = imports.get(ref.id, [])
    if ref.id in local:
        if remote:
            raise PublishError(f"{where}: {ref.id} is both one of our posts and an imported item")
        return None
    if not remote:
        raise PublishError(
            f"{where}: {ref.id} is not one of our posts or an imported item (python _blyg/blyg.py import URL)"
        )
    if len(remote) > 1:
        origins = ", ".join(imp.origin for imp in remote)
        raise PublishError(f"{where}: {ref.id} was imported from more than one origin ({origins})")
    if remote[0].doc.get("kind") not in ("fragment", "thread"):
        raise PublishError(f"{where}: imported item {ref.id} is {remote[0].doc.get('kind')}; remove the reference")
    return remote[0]


# --- history -------------------------------------------------------------------------------------


@dataclass(frozen=True)
class Snap:
    """What the history walk needs from one post file at one commit."""

    path: str
    id: str | None
    signal: str
    deps: tuple[str, ...]  # ids it quotes, so a quoted item's new version republishes it
    created: str | None
    page: str


def permalink(path: str, fm: dict) -> str:
    m = POST_NAME_RE.match(path.rsplit("/", 1)[-1])
    year, month, day, slug = m.groups()[:4] if m else ("", "", "", Path(path).stem)
    month, day = month.zfill(2), day.zfill(2)
    pattern = str(fm.get("permalink") or CONFIG.get("permalink") or "/:year/:title")
    url = pattern.replace(":year", year).replace(":month", month).replace(":day", day)
    return urllib.parse.urljoin(ORIGIN, url.replace(":title", str(fm.get("slug") or slug)))


def make_snap(path: str, text: str) -> Snap:
    fm, body = split_post(text)
    blyg_id = fm.get("blyg_id")
    if blyg_id is not None and not ID_RE.fullmatch(str(blyg_id)):
        raise PublishError(f"{path}: blyg_id {blyg_id!r} is not a 26-character blyg id")
    if fm.get("published") is False:
        blyg_id = None
    title = str(fm.get("title") or "")
    m = POST_NAME_RE.match(path.rsplit("/", 1)[-1])
    created = parse_time(fm.get("date")) or (parse_time("-".join(g.zfill(2) for g in m.groups()[:3])) if m else None)
    return Snap(
        path,
        str(blyg_id) if blyg_id else None,
        sha256(title + "\n" + " ".join(body.split())),  # whitespace-only edits are not versions
        tuple(ref.id for ref in scan(body) if ref.quote),
        iso(created) if created else None,
        permalink(path, fm),
    )


@dataclass
class Item:
    changelog: list[dict]  # version 1's "at" is None: it is the post's own date, filled in by `build`
    signal: str
    snap: Snap
    withdrawn: bool = False

    @property
    def version(self) -> int:
        return len(self.changelog)

    def bump(self, at: str | None, note: str | None) -> None:
        self.changelog.append({"version": self.version + 1, "at": at, "note": note})


class History:
    def __init__(self) -> None:
        self.items: dict[str, Item] = {}
        self.posts: dict[str, Snap] = {}
        self.imports: dict[str, tuple[str, int]] = {}

    def apply(self, files: dict[str, str | None], at: str | None, note: str | None) -> None:
        for path, text in files.items():
            if is_post(path):
                if text is None:
                    self.posts.pop(path, None)
                else:
                    self.posts[path] = make_snap(path, text)
            elif is_import(path):
                if text is None:
                    self.imports.pop(path, None)
                else:
                    doc = json.loads(text)["document"]
                    self.imports[path] = (doc["id"], doc["version"])
        self._publish(at, note)

    def _publish(self, at: str | None, note: str | None) -> None:
        present: dict[str, Snap] = {}
        for snap in sorted(self.posts.values(), key=lambda s: s.path):
            if snap.id and snap.id in present:
                warn(f"{snap.path} and {present[snap.id].path} share blyg_id {snap.id}; using the first")
            elif snap.id:
                present[snap.id] = snap
        remote: dict[str, list[int]] = {}
        for rid, version in self.imports.values():
            remote.setdefault(rid, []).append(version)

        done: set[str] = set()

        def visit(item_id: str, stack: frozenset[str]) -> None:
            if item_id in done:
                return
            done.add(item_id)
            snap, parts = present[item_id], [present[item_id].signal]
            for dep in snap.deps:
                if dep in present and dep not in stack:
                    visit(dep, stack | {item_id})
                version = self.items[dep].version if dep in present and dep in self.items else sorted(remote.get(dep, []))
                parts.append(f"{dep}@{version}")
            signal = sha256("\n".join(parts))
            item = self.items.get(item_id)
            if item is None:
                self.items[item_id] = Item([{"version": 1, "at": None, "note": None}], signal, snap)
                return
            if item.withdrawn or item.signal != signal:
                item.bump(at, note)
                item.withdrawn = False
            item.signal, item.snap = signal, snap

        for item_id in present:
            visit(item_id, frozenset())
        for item_id, item in self.items.items():
            if item_id not in present and not item.withdrawn:
                item.bump(at, note)
                item.withdrawn = True


def read_blobs(rev: str, paths: list[str]) -> dict[str, str]:
    if not paths:
        return {}
    request = "".join(f"{rev}:{p}\n" for p in paths).encode("utf-8")
    out = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, input=request, capture_output=True, check=True).stdout
    blobs, pos = {}, 0
    for path in paths:
        end = out.index(b"\n", pos)
        header, pos = out[pos:end].split(), end + 1
        if header[-1] == b"missing":
            continue
        size = int(header[2])
        blobs[path] = out[pos : pos + size].decode("utf-8", "replace")
        pos += size + 1
    return blobs


def changed_paths(rev: str) -> dict[str, bool]:
    """Watched paths a commit changed against its first parent: True if present afterwards."""
    fields = git("diff", "--name-status", "-z", "-M", f"{rev}^1", rev, "--", *WATCHED).split("\0")
    changes, i = {}, 0
    while i < len(fields) and fields[i]:
        status = fields[i]
        if status[0] in "RC":
            if status[0] == "R":
                changes[fields[i + 1]] = False
            changes[fields[i + 2]] = True
            i += 3
        else:
            changes[fields[i + 1]] = status != "D"
            i += 2
    return {p: present for p, present in changes.items() if is_post(p) or is_import(p)}


def history(include_worktree: bool = False) -> dict[str, Item]:
    h = History()
    first = git("log", "--first-parent", "--reverse", "-G", "^blyg_id:", "--format=%H", "--", "_posts").split()
    started = False
    for line in git("log", "--first-parent", "--reverse", "--format=%H%x09%cI%x09%s", "--", *WATCHED).splitlines():
        rev, when, subject = line.split("\t", 2)
        if not started:
            if not first or rev != first[0]:
                continue
            started = True
            tree = git("ls-tree", "-r", "-z", "--name-only", rev, "--", *WATCHED).split("\0")
            h.apply(read_blobs(rev, [p for p in tree if is_post(p) or is_import(p)]), None, None)
            continue
        changes = changed_paths(rev)
        files: dict[str, str | None] = {p: None for p, present in changes.items() if not present}
        files.update(read_blobs(rev, [p for p, present in changes.items() if present]))
        h.apply(files, iso(datetime.fromisoformat(when)), subject)
    if include_worktree:
        disk = {f.relative_to(ROOT).as_posix(): f for f in (*post_files(), *IMPORTS.glob("*.json"))}
        files = {p: None for p in (*h.posts, *h.imports) if p not in disk}
        files.update({p: f.read_text(encoding="utf-8") for p, f in disk.items()})
        h.apply(files, iso(datetime.now(timezone.utc)), None)
    return h.items


# --- HTML ----------------------------------------------------------------------------------------


def _absolute(value: str, base: str) -> str:
    value = value.strip()
    if not value or re.match(r"^[a-z][a-z0-9+.-]*:", value, re.I):
        return value
    return urllib.parse.urljoin(base, value).replace(" ", "%20")


def absolutize(fragment: str, base: str) -> str:
    """Make every URL in an HTML fragment absolute (§5.2), leaving script and style bodies alone."""

    def fix_tag(tag_match: re.Match) -> str:
        tag = tag_match.group(0)
        name = re.match(r"<([^\s/>]+)", tag).group(1).lower()

        def fix_attr(m: re.Match) -> str:
            lead, attr, eq, raw = m.groups()
            value = html.unescape(raw[1:-1] if raw[0] in "\"'" else raw)
            if attr.lower() == "srcset":
                candidates = (c.strip().split(None, 1) for c in value.split(",") if c.strip())
                new = ", ".join(" ".join([_absolute(c[0], base), *c[1:]]) for c in candidates)
            elif value.startswith("#") and (name == "use" or attr.lower() == "xlink:href"):
                return m.group(0)  # a reference inside an inline SVG, not a link
            else:
                new = _absolute(value, base)
            return m.group(0) if new == value else f'{lead}{attr}{eq}"{html.escape(new)}"'

        return URL_ATTR_RE.sub(fix_attr, tag)

    out, pos = [], 0
    for m in RAW_TEXT_RE.finditer(fragment):
        out.append(TAG_RE.sub(fix_tag, fragment[pos : m.start()]))
        out.append(TAG_RE.sub(fix_tag, m.group(0), count=1))
        pos = m.end()
    out.append(TAG_RE.sub(fix_tag, fragment[pos:]))
    return "".join(out)


def text_content(fragment: str) -> str:
    """§10.2's text content: tags stripped, whitespace collapsed within a block, blocks on their own lines."""
    text = re.sub(r"<[^>]+>", "", BLOCK_TAG_RE.sub("\n", RAW_TEXT_RE.sub("", fragment)))
    return "\n".join(" ".join(line.split()) for line in html.unescape(text).splitlines() if line.strip())


def bake(quote: dict, source_html: str, version: int, where: str) -> tuple[str, dict]:
    """The baked blockquote for one ![[id]] (§10.2) and its transclusions[] entry (§10.3)."""
    entry: dict = {"id": quote["id"], "version": version}
    attrs = f' data-blyg-id="{quote["id"]}" data-blyg-version="{version}"'
    if quote["origin"]:
        entry["origin"] = quote["origin"]
        attrs += f' data-blyg-origin="{html.escape(quote["origin"])}"'
    if quote["label"]:
        attrs += f' data-blyg-label="{html.escape(quote["label"])}"'
    if quote["selection"] is None:
        return f'<blockquote class="blyg-transclusion"{attrs}>{source_html}</blockquote>', entry
    lines = [" ".join(line.split()) for line in quote["selection"] if line.strip()]
    if " ".join(lines) not in " ".join(text_content(source_html).split()):
        raise PublishError(f"{where}: the quoted text is not in {quote['id']} v{version}: {' '.join(lines)[:80]!r}")
    entry["selector"] = {"exact": "\n".join(lines)}
    paragraphs = "".join(f"<p>{html.escape(line, quote=False)}</p>" for line in lines)
    return f'<blockquote class="blyg-transclusion blyg-partial"{attrs}>{paragraphs}</blockquote>', entry


# --- HTTP ----------------------------------------------------------------------------------------


def fetch(url: str, method: str = "GET", data: bytes | None = None) -> tuple[int, str, str, dict]:
    """(status, final url, body, headers); HTTP errors come back as statuses, not exceptions."""
    request = urllib.request.Request(url, data=data, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=20) as r:
            return r.status, r.geturl(), r.read(5_000_000).decode("utf-8", "replace"), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, url, "", dict(e.headers or {})


def fetch_json(url: str) -> tuple[dict | None, str]:
    status, final, body, _ = fetch(url)
    if status == 404:
        return None, final
    if status >= 400:
        raise PublishError(f"GET {url}: HTTP {status}")
    try:
        data = json.loads(body)
    except ValueError:
        return None, final
    return (data if isinstance(data, dict) else None), final


def html_links(page: str, rel: str, tags: str = "link") -> list[dict[str, str]]:
    found = []
    for tag in re.finditer(rf"(?is)<(?:{tags})\b[^>]*>", page):
        attrs = {
            k.lower(): html.unescape(v.strip("\"'"))
            for k, v in re.findall(r"""([\w:-]+)\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)""", tag.group(0))
        }
        if rel in attrs.get("rel", "").lower().split() and "href" in attrs:
            found.append(attrs)
    return found


# --- commands ------------------------------------------------------------------------------------


def cmd_assign_ids(args: argparse.Namespace) -> None:
    dirty = set()
    if not args.include_dirty:
        dirty = {line[3:].strip('"') for line in git("status", "--porcelain", "--", "_posts").splitlines()}
    seen: dict[str, str] = {}
    assigned, skipped = 0, []
    for f in post_files():
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_bytes().decode("utf-8")
        m = FRONT_MATTER_RE.match(text)
        if not m:
            warn(f"{rel}: no front matter, so no blyg_id")
            continue
        existing = (yaml.safe_load(m.group(1) or "") or {}).get("blyg_id")
        if existing:
            if str(existing) in seen:
                raise PublishError(f"{rel} and {seen[str(existing)]} share blyg_id {existing}: delete it from the copy")
            seen[str(existing)] = rel
            continue
        if rel in dirty:
            skipped.append(rel)
            continue
        newline = "\r\n" if "\r\n" in m.group(0) else "\n"
        at = m.end(1) if m.group(1) else text.index("\n") + 1
        f.write_bytes((text[:at] + f"blyg_id: {new_id()}{newline}" + text[at:]).encode("utf-8"))
        assigned += 1
    print(f"assigned {assigned} blyg ids")
    for rel in skipped:
        print(f"  skipped {rel}: it has uncommitted changes (--include-dirty to assign anyway)")


def liquid_site() -> dict:
    def load(directory: Path) -> dict:
        data: dict = {}
        for p in sorted(directory.iterdir()) if directory.is_dir() else []:
            if p.is_dir():
                data[p.name] = load(p)
            elif p.suffix in (".yml", ".yaml"):
                data[p.stem] = yaml.safe_load(p.read_text(encoding="utf-8"))
            elif p.suffix == ".json":
                data[p.stem] = json.loads(p.read_text(encoding="utf-8"))
        return data

    # site.baseurl becomes the full origin, so {{ site.baseurl }}/x links in content_md come out absolute
    return {**CONFIG, "baseurl": ORIGIN.rstrip("/"), "data": load(ROOT / "_data")}


def jekyll_to_liquid(text: str) -> str:
    """Rewrite the Jekyll-only tags our posts use into plain Liquid and markdown."""
    text = INCLUDE_RE.sub(lambda m: "{% include '" + m.group(1).lstrip("/") + "' %}", text)
    text = HIGHLIGHT_RE.sub(lambda m: "```" + m.group(1), text)
    return END_HIGHLIGHT_RE.sub("```", text)


class IncludeLoader(FileSystemLoader):
    def get_source(self, env, template_name, *, context=None, **kwargs):
        source = super().get_source(env, template_name, context=context, **kwargs)
        return source._replace(text=jekyll_to_liquid(source.text))


def cmd_prepare(args: argparse.Namespace) -> None:
    """Write content_md for every post, and turn [[id]] / ![[id]] into markdown Jekyll can render."""
    posts = []
    for f in post_files():
        text = f.read_bytes().decode("utf-8").replace("\r\n", "\n")  # content_hash must not depend on checkout
        fm, body = split_post(text)
        if fm.get("blyg_id") and fm.get("published") is not False:
            posts.append((f, text, fm, body))
    local: dict[str, dict] = {}
    for f, _, fm, _ in posts:
        item_id = str(fm["blyg_id"])
        if item_id in local:
            raise PublishError(f"{f.name} and {local[item_id]['file'].name} share blyg_id {item_id}")
        local[item_id] = {"file": f, "title": str(fm.get("title") or "")}
    imports = load_imports()
    env, site = Environment(loader=IncludeLoader(INCLUDES)), liquid_site()

    prepared, rewritten = {}, 0
    for f, text, fm, body in posts:
        item_id, rel = str(fm["blyg_id"]), f.relative_to(ROOT).as_posix()
        title = local[item_id]["title"]
        try:
            markdown = env.from_string(jekyll_to_liquid(body)).render(site=site, page=fm)
        except Exception as e:  # a tag or filter python-liquid lacks: publish the source as written
            warn(f"{rel}: Liquid failed ({e}); its content_md is the raw source")
            markdown = body
        refs = scan(body)
        targets = [resolve(ref, local, imports, rel) for ref in refs]
        quotes, links = [], []
        for ref, target in zip(refs, targets):
            if ref.quote and target is None and ref.id == item_id:
                raise PublishError(f"{rel}: a post cannot quote itself")
            origin = target.origin if target else None
            if ref.quote:
                quotes.append({"id": ref.id, "origin": origin, "label": ref.label, "selection": ref.selection})
            else:
                links.append({"id": ref.id, "origin": origin} if origin else {"id": ref.id})
        prepared[item_id] = {
            "path": rel,
            "title": title,
            "content_md": f"# {title}\n\n{markdown}" if title else markdown,
            "quotes": quotes,
            "links": links,
        }
        if not refs:
            continue
        if not args.write:
            warn(f"{rel} uses [[id]]; run prepare with --write (CI does) or the built page shows them raw")
            continue
        lines = body.splitlines()
        for k in reversed(range(len(refs))):  # from the end, so earlier line numbers and columns hold
            ref, target = refs[k], targets[k]
            if ref.quote:
                n = sum(1 for r in refs[:k] if r.quote)
                lines[ref.line : ref.end] = ["", f"BLYGQUOTE{item_id}N{n}", ""]
            else:
                href = target.page if target else LINK_PLACEHOLDER + ref.id
                label = ref.label or (target.page if target else local[ref.id]["title"]) or href
                label = label.replace("[", r"\[").replace("]", r"\]")
                a, b = ref.span
                lines[ref.line] = lines[ref.line][:a] + f"[{label}]({href})" + lines[ref.line][b:]
        f.write_bytes((text[: len(text) - len(body)] + "\n".join(lines) + "\n").encode("utf-8"))
        rewritten += 1

    OUT.mkdir(exist_ok=True)
    (OUT / "prepared.json").write_text(json.dumps(prepared, ensure_ascii=False), encoding="utf-8")
    print(f"prepared {len(prepared)} posts ({rewritten} rewritten for [[id]])")


def cmd_build(args: argparse.Namespace) -> None:
    dump_path = SITE / DUMP
    rendered = {p["blyg_id"]: p for p in json.loads(dump_path.read_text(encoding="utf-8")) if p.get("blyg_id")}
    dump_path.unlink()
    prepared = json.loads((OUT / "prepared.json").read_text(encoding="utf-8"))
    items = history(include_worktree=args.worktree)
    imports = load_imports()

    def page_of(item_id: str) -> str:
        return urllib.parse.urljoin(ORIGIN, rendered[item_id]["url"])

    live_ids = {i for i, item in items.items() if not item.withdrawn and i in rendered and i in prepared}
    for item_id in sorted(set(rendered) - set(items)):
        warn(f"{prepared.get(item_id, {}).get('path', item_id)}: blyg_id is not committed yet; not published")
    for item_id in sorted(i for i, item in items.items() if not item.withdrawn and i not in live_ids):
        warn(f"{items[item_id].snap.path}: not in the Jekyll build (a future date?); not published")

    built: dict[str, tuple[str, list]] = {}

    def content_html(item_id: str, stack: frozenset[str] = frozenset()) -> tuple[str, list]:
        if item_id in built:
            return built[item_id]
        prep, where = prepared[item_id], prepared[item_id]["path"]
        if item_id in stack:
            raise PublishError(f"{where}: quotes a post that quotes it back")
        body = absolutize(rendered[item_id]["html"], page_of(item_id))
        for link in prep["links"]:
            if "origin" not in link:
                if link["id"] not in live_ids:
                    raise PublishError(f"{where}: links to {link['id']}, which is not published")
                body = body.replace(LINK_PLACEHOLDER + link["id"], page_of(link["id"]))
        transclusions = []
        for n, quote in enumerate(prep["quotes"]):
            token = f"<p>BLYGQUOTE{item_id}N{n}</p>"
            if token not in body:
                raise PublishError(f"{where}: quote {n} is missing from the page (run prepare --write before jekyll)")
            if quote["origin"]:
                imp = next(i for i in imports.get(quote["id"], []) if i.origin == quote["origin"])
                source, version = imp.doc["content_html"], imp.doc["version"]
            elif quote["id"] in live_ids:
                source, version = content_html(quote["id"], stack | {item_id})[0], items[quote["id"]].version
            else:
                raise PublishError(f"{where}: quotes {quote['id']}, which is not published")
            baked, entry = bake(quote, source, version, where)
            body = body.replace(token, baked, 1)
            transclusions.append(entry)
        title = prep["title"]
        built[item_id] = (f"<h1>{html.escape(title, quote=False)}</h1>\n{body}" if title else body, transclusions)
        return built[item_id]

    docs: dict[str, dict] = {}
    for item_id, item in items.items():
        if item_id not in live_ids and not item.withdrawn:
            continue
        created = (
            iso(parse_time(rendered[item_id]["date"])) if item_id in rendered else item.snap.created or iso(datetime.now(timezone.utc))
        )
        changelog, latest = [], created
        for entry in item.changelog:
            latest = max(latest, entry["at"] or created)  # git times can't run backwards past the post's date
            changelog.append({**entry, "at": latest})
        doc = {
            "blyg": PROTOCOL,
            "id": item_id,
            "kind": "withdrawn" if item.withdrawn else "thread",
            "origin": ORIGIN,
            "page": page_of(item_id) if item_id in rendered else item.snap.page,
            "author": AUTHOR,
            "created": created,
            "updated": latest,
            "version": item.version,
        }
        if item.withdrawn:
            doc.update(content_md="", content_html="", content_hash="sha256:" + sha256(""), media=[])
            doc.update(changelog=changelog, transclusions=[])
        else:
            content_md = prepared[item_id]["content_md"]
            html_, transclusions = content_html(item_id)
            doc.update(content_md=content_md, content_html=html_, content_hash="sha256:" + sha256(content_md))
            doc.update(media=[], changelog=changelog, transclusions=transclusions)
            if prepared[item_id]["links"]:
                doc["links"] = prepared[item_id]["links"]
        docs[item_id] = doc

    ordered = sorted(docs.values(), key=lambda d: (d["updated"], d["id"]), reverse=True)
    updated = ordered[0]["updated"] if ordered else iso(datetime.now(timezone.utc))
    index = {
        "updated": updated,
        "items": [{k: d[k] for k in ("id", "kind", "created", "updated", "version")} for d in ordered],
    }
    manifest = {
        "blyg": PROTOCOL,
        "level": 2,
        "generator": GENERATOR,
        "generator_url": GENERATOR_URL,
        "site": ORIGIN,
        "title": CONFIG["title"],
        "author": AUTHOR,
        "feed": FEED,
        "items": "items/index.json",  # the default, but 0.3 readers expect to find it
        "updated": updated,
    }

    mentions = [] if args.offline else check_live_and_queue_mentions(docs, imports)

    (SITE / "items").mkdir(exist_ok=True)
    for doc in docs.values():
        write_json(SITE / "items" / f"{doc['id']}.json", doc)
    write_json(SITE / "items" / "index.json", index)
    write_json(SITE / "blyg.json", manifest)
    (SITE / FEED).write_text(feed_xml(ordered, updated), encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    write_json(OUT / "mentions.json", mentions)
    withdrawn = sum(1 for d in docs.values() if d["kind"] == "withdrawn")
    print(f"published {len(docs) - withdrawn} items, {withdrawn} withdrawn; {len(mentions)} mentions queued")


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def remote_refs(doc: dict) -> set[tuple]:
    refs = {("transclusion", t["origin"], t["id"], t["version"]) for t in doc.get("transclusions", []) if "origin" in t}
    return refs | {("link", l["origin"], l["id"], None) for l in doc.get("links", []) if "origin" in l}


def check_live_and_queue_mentions(docs: dict[str, dict], imports: dict[str, list[Imported]]) -> list[dict]:
    """Refuse to move any published item backwards, and list the remote references that are new (§15.2)."""
    live_index, _ = fetch_json(ORIGIN + "items/index.json")
    live = {e["id"]: e["version"] for e in (live_index or {}).get("items", [])}
    backwards = [
        f"{i} (live v{v}, this build {'v' + str(docs[i]['version']) if i in docs else 'missing'})"
        for i, v in live.items()
        if i not in docs or docs[i]["version"] < v
    ]
    if backwards:
        raise PublishError(
            "this build would move published items backwards, which the protocol forbids. "
            "Was history rewritten, or a post's blyg_id changed? " + "; ".join(backwards[:10])
        )
    queue = []
    for doc in docs.values():
        refs = remote_refs(doc)
        if not refs or live.get(doc["id"]) == doc["version"]:
            continue
        sent = set()
        if doc["id"] in live:
            old, _ = fetch_json(f"{ORIGIN}items/{doc['id']}.json")
            sent = remote_refs(old or {})
        for relation, origin, ref_id, _ in sorted(refs - sent, key=str):
            imp = next(i for i in imports.get(ref_id, []) if i.origin == origin)
            mention = {"source": doc["page"], "target": imp.page, "origin": origin, "relation": relation}
            if mention not in queue:
                queue.append(mention)
    return queue


def feed_xml(docs: list[dict], updated: str) -> str:
    def rfc822(stamp: str) -> str:
        return format_datetime(datetime.fromisoformat(stamp.replace("Z", "+00:00")), usegmt=True)

    events = []
    for doc in docs:
        entries = doc["changelog"][-1:] if doc["kind"] == "withdrawn" else doc["changelog"]
        events += [(entry, doc) for entry in entries]
    events.sort(key=lambda e: (e[0]["at"], e[0]["version"]), reverse=True)

    items = []
    for entry, doc in events[:FEED_WINDOW]:
        if doc["kind"] == "withdrawn":
            title, description = "withdrawn", ""
        else:
            text = " ".join(text_content(doc["content_html"]).split())
            excerpt = text if len(text) <= 120 else text[:119].rstrip() + "…"
            title = f"{entry['note']} — {excerpt}" if entry["note"] else excerpt
            description = "<![CDATA[" + doc["content_html"].replace("]]>", "]]]]><![CDATA[>") + "]]>"
        items.append(
            f"""    <item>
      <guid isPermaLink="false">blyg:{doc['id']}:v{entry['version']}</guid>
      <link>{xml_escape(doc['page'])}</link>
      <title>{xml_escape(title)}</title>
      <description>{description}</description>
      <pubDate>{rfc822(entry['at'])}</pubDate>
      <dc:creator>{xml_escape(AUTHOR['name'])}</dc:creator>
      <blyg:id>{doc['id']}</blyg:id>
      <blyg:kind>{doc['kind']}</blyg:kind>
      <blyg:version>{entry['version']}</blyg:version>
      <blyg:created>{doc['created']}</blyg:created>
      <blyg:item>{ORIGIN}items/{doc['id']}.json</blyg:item>
    </item>"""
        )
    description = " ".join(str(CONFIG.get("description", "")).split())
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:blyg="https://blygger.org/ns/0.1" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>{xml_escape(CONFIG['title'])}</title>
    <link>{ORIGIN}</link>
    <description>{xml_escape(description)}</description>
    <lastBuildDate>{rfc822(updated)}</lastBuildDate>
    <generator>{GENERATOR}</generator>
    <blyg:level>2</blyg:level>
    <blyg:manifest>{ORIGIN}blyg.json</blyg:manifest>
{chr(10).join(items)}
  </channel>
</rss>
"""


def cmd_import(args: argparse.Namespace) -> None:
    """Snapshot a remote item: quoting follows reading (§10.2), so a post can only cite what is imported."""
    url = args.url
    status, final, body, _ = fetch(url)
    if status >= 400:
        raise PublishError(f"GET {url}: HTTP {status}")
    try:
        doc = json.loads(body)
    except ValueError:
        alternates = [a for a in html_links(body, "alternate") if a.get("type") == "application/json"]
        if not alternates:
            raise PublishError(f"{url} is neither a blyg item document nor a page linking to one")
        doc, final = fetch_json(urllib.parse.urljoin(final, alternates[0]["href"]))
    if not isinstance(doc, dict) or not ID_RE.fullmatch(str(doc.get("id", ""))) or "blyg" not in doc:
        raise PublishError(f"{url} did not lead to a blyg item document")

    # The identity origin is where the manifest is actually served (§12.2), not what the document claims.
    manifest, manifest_url = fetch_json(urllib.parse.urljoin(doc.get("origin") or final, "blyg.json"))
    if not manifest or "blyg" not in manifest:
        raise PublishError(f"no blyg manifest found for {url}")
    origin = manifest_url[: -len("blyg.json")]
    canonical = item_url(origin, manifest, doc["id"])
    if canonical != final:
        doc, _ = fetch_json(canonical)
        if not doc:
            raise PublishError(f"{canonical} does not serve the item")
    if doc.get("kind") not in ("fragment", "thread"):
        raise PublishError(f"{doc['id']} is {doc.get('kind')}; there is nothing to cite")

    IMPORTS.mkdir(parents=True, exist_ok=True)
    host = re.sub(r"[^a-z0-9]+", "-", urllib.parse.urlsplit(origin).netloc + urllib.parse.urlsplit(origin).path).strip("-")
    snapshot = {"origin": origin, "retrieved": iso(datetime.now(timezone.utc)), "manifest": manifest, "document": doc}
    write_json(IMPORTS / f"{host}-{doc['id']}.json", snapshot)
    print(f"imported {doc['id']} v{doc['version']} from {origin}")
    print(f"  link to it:  [[{doc['id']}]]   quote it:  ![[{doc['id']}]]   (commit _blyg/imports/ too)")


def discover_endpoint(origin: str, target: str) -> str | None:
    """§15.2: the target's manifest first, then W3C discovery on the target URL."""
    try:
        manifest, manifest_url = fetch_json(urllib.parse.urljoin(origin, "blyg.json"))
        if manifest and manifest.get("webmention"):
            return urllib.parse.urljoin(manifest_url, manifest["webmention"])
    except PublishError:
        pass
    for method in ("HEAD", "GET"):
        status, final, body, headers = fetch(target, method)
        if status >= 400:
            return None
        link_header = next((v for k, v in headers.items() if k.lower() == "link"), "")
        for href, params in re.findall(r"<([^>]*)>\s*((?:;[^,]*)*)", link_header):
            rel = re.search(r'rel\s*=\s*"?([^";]*)', params)
            if rel and "webmention" in rel.group(1).lower().split():
                return urllib.parse.urljoin(final, href)
        if method == "GET":
            found = html_links(body, "webmention", "link|a")
            return urllib.parse.urljoin(final, found[0]["href"]) if found else None
    return None


def cmd_send_mentions(args: argparse.Namespace) -> None:
    """Fire and forget (§15.2): failures are reported, never fatal."""
    path = Path(args.file)
    queue = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    report = []
    for m in queue:
        try:
            endpoint = discover_endpoint(m["origin"], m["target"])
        except OSError as e:
            endpoint, outcome = None, f"discovery failed ({e})"
        else:
            outcome = "no Webmention endpoint"
        if endpoint:
            data = urllib.parse.urlencode({"source": m["source"], "target": m["target"]}).encode()
            for delay in (0, 10, 60, 240):
                time.sleep(delay)
                try:
                    status = fetch(endpoint, "POST", data)[0]
                except OSError as e:
                    status, outcome = None, f"network error ({e})"
                    continue
                outcome = f"HTTP {status}"
                if status < 500 and status != 429:
                    break
        report.append(f"| {m['relation']} | {m['source']} | {m['target']} | {outcome} |")
        print(f"{m['relation']}: {m['source']} -> {m['target']}: {outcome}")
    if report and os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
            summary.write("### Webmentions\n\n| relation | source | target | outcome |\n|---|---|---|---|\n")
            summary.write("\n".join(report) + "\n")
    if not queue:
        print("no mentions to send")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("assign-ids", help="give posts without a blyg_id a new one")
    p.add_argument("--include-dirty", action="store_true", help="also touch posts with uncommitted changes")
    p.set_defaults(run=cmd_assign_ids)
    p = commands.add_parser("prepare", help="run before jekyll build")
    p.add_argument("--write", action="store_true", help="rewrite [[id]] in _posts in place (CI only)")
    p.set_defaults(run=cmd_prepare)
    p = commands.add_parser("build", help="run after jekyll build")
    p.add_argument("--worktree", action="store_true", help="treat uncommitted changes as one more publish")
    p.add_argument("--offline", action="store_true", help="skip the live-site check and mention queue")
    p.set_defaults(run=cmd_build)
    p = commands.add_parser("import", help="snapshot a remote blyg item")
    p.add_argument("url", help="the item's page or item document URL")
    p.set_defaults(run=cmd_import)
    p = commands.add_parser("send-mentions", help="send queued Webmentions")
    p.add_argument("--file", default=str(OUT / "mentions.json"))
    p.set_defaults(run=cmd_send_mentions)
    args = parser.parse_args()
    try:
        args.run(args)
    except PublishError as e:
        print(f"::error::{e}" if CI else f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
