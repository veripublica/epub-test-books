# An `@import` of a file that is not in the container

- Book: `import-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/at-import/import-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#385](https://github.com/veripublica/epub-test-books/issues/385)
- Other clauses: EPUB 3.3 `sec-container-iri`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @import "missing.css";, then p { margin: 0; }, and there is no missing.css. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The @import is valid and its URL is missing.css, next to style.css. No such file exists in the container.

## Question

`style.css` holds `@import "missing.css";`, then `p { margin: 0; }`, and there is no `missing.css`. Does a validator reject the book?

## Clause

CSS Cascading and Inheritance Level 5, [`at-import`](https://www.w3.org/TR/css-cascade-5/#at-import) (2. Importing Style Sheets: the @import rule; Candidate Recommendation Snapshot, 13 January 2022):

> The @import rule allows users to import style rules from other style sheets.

EPUB 3.3, [`sec-container-iri`](https://www.w3.org/TR/epub-33/#sec-container-iri):

> In addition, all relative-URL-with-fragment strings [url] MUST, after parsing, be equal to the content URL of an existing file in the OCF abstract container.

## Expected result

Invalid. The `@import` is valid and its URL is `missing.css`, next to `style.css`. No such file exists in the container.

CSS result: The `@import` is kept and fails to load; one rule, `p { margin: 0; }`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i import-missing.epub -u --advisory` | ERROR RSC-007; INVALID | `import-missing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck import-missing.epub -u` | ERROR RSC-007; INVALID | `import-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@import "missing.css";`, then `p { margin: 0; }`, and there is no `missing.css`, in UTF-8.

## History

- 2026-11-12: First version.
