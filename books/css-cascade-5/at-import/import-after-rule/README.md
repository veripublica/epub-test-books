# An `@import` after a style rule (valid)

- Book: `import-after-rule.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/at-import/import-after-rule/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#382](https://github.com/veripublica/epub-test-books/issues/382)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0; }, then @import "b.css";; b.css, also in the manifest, holds p { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Neither sheet holds direction or unicode-bidi, and both are UTF-8, so EPUB 3.3 asks nothing more of them.

## Question

`style.css` holds `p { margin: 0; }`, then `@import "b.css";`; `b.css`, also in the manifest, holds `p { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Cascading and Inheritance Level 5, [`at-import`](https://www.w3.org/TR/css-cascade-5/#at-import) (2. Importing Style Sheets: the @import rule; Candidate Recommendation Snapshot, 13 January 2022):

> Any @import rules must precede all other valid at-rules and style rules in a style sheet (ignoring @charset and empty @layer definitions) and must not have any other valid at-rules or style rules between it and previous @import rules, or else the @import rule is invalid.

CSS Syntax Level 3, [`css-stylesheets`](https://www.w3.org/TR/css-syntax-3/#css-stylesheets) (8. CSS stylesheets; Candidate Recommendation Draft, 1 October 2026):

> If any style rule is invalid, or any at-rule is not recognized or is invalid according to its grammar or context, it’s a parse error. Discard that rule.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. Neither sheet holds `direction` or `unicode-bidi`, and both are UTF-8, so EPUB 3.3 asks nothing more of them.

CSS result: One rule is kept, `p { margin: 0; }`. The `@import` comes after a style rule, so it is invalid and dropped (a parse error), and `b.css` is not imported.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i import-after-rule.epub -u --advisory` | USAGE ADV-021; VALID | `import-after-rule.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck import-after-rule.epub -u` | no findings; VALID | `import-after-rule.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output, except USAGE ADV-021, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) and `OEBPS/b.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then `@import "b.css";`; `b.css`, also in the manifest, holds `p { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
