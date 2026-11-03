# Blyg publishing

This blog is published as a [blyg](https://blygger.org/spec/0.4/) as well as a website. `blyg.py` adds the blyg files to the Jekyll build, and [the Pages workflow](../.github/workflows/pages.yml) runs it on every push.

## What gets published

- `/blyg.json` is the manifest, and `/items/index.json` lists every item.
- `/items/{id}.json` holds one item document per post in `_posts`.
- `/blyg-feed.xml` is the blyg feed. `/feed.xml` stays the plain RSS feed for existing subscribers, and points blyg readers at the manifest.

Each post is a `thread`, and its permanent identity is the `blyg_id` in its front matter. The workflow gives new posts an id and commits it back, so pull after pushing a new post. You can also run `python _blyg/blyg.py assign-ids` yourself.

**Never change or copy a `blyg_id`.** If you duplicate a post as a starting point, delete the copied `blyg_id` line.

## Versions

Versions come from git history:

- **Version 1** is the post as it stood when it got its id.
- **Each later commit** that changes the title or body is the next version, with the commit subject as the changelog note. Whitespace-only changes don't count.
- **Deleting a post**, or setting `published: false`, publishes a withdrawal. Restoring it publishes the next version.

Don't rewrite pushed history (force-push or squash). A published version number can never go down, so the build refuses to deploy if it would.

## Linking and quoting other blygs

1. Import the item, then commit the snapshot in `_blyg/imports/`:

   ```sh
   python _blyg/blyg.py import https://example.com/blyg/t/7c9wk2mhq0v3xj8tn5rzfd41bg/
   ```

2. Refer to it in a post by id. These forms work for our own posts' ids too.

   - `[[7c9wk2mhq0v3xj8tn5rzfd41bg]]` or `[[7c9wk2mhq0v3xj8tn5rzfd41bg | label]]` is a link that notifies the other blyg.
   - `![[7c9wk2mhq0v3xj8tn5rzfd41bg]]` on its own line quotes the whole item.
   - The directive line followed directly by a `> blockquote` quotes just that text. The text must appear in the item exactly, as plain text without markdown formatting.

   An ordinary markdown link is still a silent citation, and nothing is sent.

After each deploy, the workflow sends a Webmention for every remote reference that is new in this version. The job summary shows the results. This blog doesn't receive Webmentions yet.

## Running it locally

```sh
pip install -r _blyg/requirements.txt
python _blyg/blyg.py prepare
bundle exec jekyll build
python _blyg/blyg.py build --worktree --offline
```

`--worktree` counts uncommitted changes as one more publish. `--offline` skips the live-site check and the mention queue.

Locally, `prepare` leaves `[[id]]` unrendered unless you pass `--write`. That flag rewrites `_posts` in place, so leave it to CI.
