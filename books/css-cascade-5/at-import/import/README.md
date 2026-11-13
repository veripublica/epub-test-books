# A stylesheet imported with `@import` (valid)

- Book: `import.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/at-import/import/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#380](https://github.com/veripublica/epub-test-books/issues/380)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @import "b.css";, then p { margin: 0; }; b.css, also in the manifest, holds p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Neither sheet holds direction or unicode-bidi, and both are UTF-8, so EPUB 3.3 asks nothing more of them.

## Question

`style.css` holds `@import "b.css";`, then `p { margin: 0; }`; `b.css`, also in the manifest, holds `p { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Cascading and Inheritance Level 5, [`at-import`](https://www.w3.org/TR/css-cascade-5/#at-import) (2. Importing Style Sheets: the @import rule; Candidate Recommendation Snapshot, 13 January 2022):

> The @import rule allows users to import style rules from other style sheets.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. Neither sheet holds `direction` or `unicode-bidi`, and both are UTF-8, so EPUB 3.3 asks nothing more of them.

CSS result: `style.css` imports `b.css`, then has one rule, `p { margin: 0; }`. `b.css` adds the same rule before it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i import.epub -u --advisory` | no findings; VALID | `import.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck import.epub -u` | no findings; VALID | `import.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) and `OEBPS/b.css` (`text/css`) in the manifest. `style.css` holds `@import "b.css";`, then `p { margin: 0; }`; `b.css`, also in the manifest, holds `p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
