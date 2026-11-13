# An `@import` of a stylesheet on the web

- Book: `import-remote.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/at-import/import-remote/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#386](https://github.com/veripublica/epub-test-books/issues/386)
- Other clauses: EPUB 3.3 `sec-resource-locations`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @import url("https://example.com/a.css");, then p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The imported stylesheet is a resource outside the container, and EPUB 3.3 allows that only for audio, video and fonts.

## Question

`style.css` holds `@import url("https://example.com/a.css");`, then `p { margin: 0; }`. Does a validator reject the book?

## Clause

CSS Cascading and Inheritance Level 5, [`at-import`](https://www.w3.org/TR/css-cascade-5/#at-import) (2. Importing Style Sheets: the @import rule; Candidate Recommendation Snapshot, 13 January 2022):

> The @import rule allows users to import style rules from other style sheets.

EPUB 3.3, [`sec-resource-locations`](https://www.w3.org/TR/epub-33/#sec-resource-locations):

> EPUB creators MUST store all other resources within the EPUB container.

## Expected result

Invalid. The imported stylesheet is a resource outside the container, and EPUB 3.3 allows that only for audio, video and fonts.

CSS result: The `@import` is kept; one rule, `p { margin: 0; }`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i import-remote.epub -u --advisory` | ERROR RSC-006; INVALID | `import-remote.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck import-remote.epub -u` | ERROR RSC-006; INVALID | `import-remote.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@import url("https://example.com/a.css");`, then `p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
