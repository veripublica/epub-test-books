# A stylesheet imported into a layer, `@import url("b.css") layer(base)` (valid)

- Book: `import-layer.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/at-import/import-layer/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#384](https://github.com/veripublica/epub-test-books/issues/384)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @import url("b.css") layer(base);, then p { margin: 0; }; b.css, also in the manifest, holds p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Neither sheet holds direction or unicode-bidi, and both are UTF-8, so EPUB 3.3 asks nothing more of them.

## Question

`style.css` holds `@import url("b.css") layer(base);`, then `p { margin: 0; }`; `b.css`, also in the manifest, holds `p { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Cascading and Inheritance Level 5, [`at-import`](https://www.w3.org/TR/css-cascade-5/#at-import) (2. Importing Style Sheets: the @import rule; Candidate Recommendation Snapshot, 13 January 2022):

> The @import rule allows users to import style rules from other style sheets.

> the optional layer keyword or layer() function assigns the contents of the style sheet into its own anonymous cascade layer or into the named cascade layer.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. Neither sheet holds `direction` or `unicode-bidi`, and both are UTF-8, so EPUB 3.3 asks nothing more of them.

CSS result: `style.css` imports `b.css` into the layer `base`, then has one unlayered rule, `p { margin: 0; }`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i import-layer.epub -u --advisory` | no findings; VALID | `import-layer.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck import-layer.epub -u` | no findings; VALID | `import-layer.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) and `OEBPS/b.css` (`text/css`) in the manifest. `style.css` holds `@import url("b.css") layer(base);`, then `p { margin: 0; }`; `b.css`, also in the manifest, holds `p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
