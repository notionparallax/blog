// Margin sidenotes for posts.
//
// Heavily inspired by https://gwern.net/sidenote and the sidenotes.js
// (Said Achmiz, MIT licensed) it describes. That implementation is written
// for Pandoc-style footnotes and is tightly coupled to Gwern.net's own
// front-end framework (its transclusion/popup event system, utility
// library, etc.), so rather than port it, this is an independent,
// much smaller re-implementation of the same core idea -- relocate each
// footnote into the margin next to its reference, stacking to avoid
// overlap -- built directly against kramdown's existing footnote markup.
// No changes to post content are required; narrower viewports (and
// no-JS) fall back to the ordinary footnotes list untouched.
(function () {
    "use strict";

    var BREAKPOINT = "(min-width: 1350px)";
    var SPACING = 20; // minimum px gap between stacked sidenotes

    var article = document.querySelector("article.post");
    var footnotesBlock = article && article.querySelector(".footnotes");
    if (!article || !footnotesBlock) return;

    var citations = Array.prototype.slice.call(
        article.querySelectorAll('sup[id^="fnref:"] a.footnote')
    );
    if (citations.length === 0) return;

    var column = document.createElement("div");
    column.id = "sidenote-column-right";
    column.className = "sidenote-column";
    article.appendChild(column);

    var sidenotes = citations.map(function (citation) {
        // The fragment of the id (after "fnref:") is kramdown's internal key,
        // which may be a word slug (e.g. [^construal]) rather than a number --
        // it's only usable for locating the matching footnote, not display.
        // The number actually printed next to the reference is the link text.
        var key = citation.closest("sup").id.replace("fnref:", "");
        var displayNumber = citation.textContent.trim();
        var source = document.getElementById("fn:" + key);
        if (!source) return null;

        var sidenote = document.createElement("div");
        sidenote.className = "sidenote";
        sidenote.id = "sn:" + key;
        sidenote.setAttribute("role", "note");

        var number = document.createElement("span");
        number.className = "sidenote-number";
        number.textContent = displayNumber + ".";
        sidenote.appendChild(number);

        Array.prototype.forEach.call(source.children, function (child) {
            var clone = child.cloneNode(true);
            var backlink = clone.querySelector(".reversefootnote");
            if (backlink) backlink.remove();
            sidenote.appendChild(clone);
        });

        column.appendChild(sidenote);
        return sidenote;
    });

    citations.forEach(function (citation, i) {
        var sidenote = sidenotes[i];
        if (!sidenote) return;

        citation.addEventListener("click", function (event) {
            if (!window.matchMedia(BREAKPOINT).matches) return;

            event.preventDefault();
            sidenotes.forEach(function (sn) {
                if (sn) sn.classList.remove("highlighted");
            });
            sidenote.classList.add("highlighted");
            sidenote.scrollIntoView({ block: "nearest", behavior: "smooth" });
        });
    });

    function layout() {
        if (!window.matchMedia(BREAKPOINT).matches) return;

        var articleTop = article.getBoundingClientRect().top + window.scrollY;
        var previousBottom = 0;

        citations.forEach(function (citation, i) {
            var sidenote = sidenotes[i];
            if (!sidenote) return;

            var citationTop =
                citation.getBoundingClientRect().top + window.scrollY - articleTop;
            var top = Math.max(citationTop, previousBottom + SPACING);
            sidenote.style.top = top + "px";
            previousBottom = top + sidenote.offsetHeight;
        });
    }

    document.body.classList.add("sidenotes-active");
    layout();

    window.addEventListener("load", layout);
    if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(layout);
    }

    var resizeTimer;
    window.addEventListener("resize", function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(layout, 150);
    });
})();
