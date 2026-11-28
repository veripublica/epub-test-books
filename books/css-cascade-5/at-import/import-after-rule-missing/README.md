# An `@import` after a style rule, naming a file that does not exist (valid)

- Book: `import-after-rule-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/at-import/import-after-rule-missing/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#700](https://github.com/veripublica/epub-test-books/issues/700)
- Other clauses: EPUB 3.3 `sec-container-iri`, `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0; }, then @import "missing.css";, and there is no missing.css in the container. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The @import comes after a style rule, so it is invalid and CSS drops it. Nothing is imported, and the parsed style sheet refers to no missing.css. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

## Question

`style.css` holds `p { margin: 0; }`, then `@import "missing.css";`, and there is no `missing.css`. Does a validator accept the book?

## Clause

CSS Cascading and Inheritance Level 5, [`at-import`](https://www.w3.org/TR/css-cascade-5/#at-import) (2. Importing Style Sheets: the @import rule; Candidate Recommendation Snapshot, 13 January 2022):

> Any @import rules must precede all other valid at-rules and style rules in a style sheet (ignoring @charset and empty @layer definitions) and must not have any other valid at-rules or style rules between it and previous @import rules, or else the @import rule is invalid.

CSS Syntax Level 3, [`css-stylesheets`](https://www.w3.org/TR/css-syntax-3/#css-stylesheets) (8. CSS stylesheets; Candidate Recommendation Draft, 1 October 2026):

> If any style rule is invalid, or any at-rule is not recognized or is invalid according to its grammar or context, it’s a parse error. Discard that rule.

EPUB 3.3, [`sec-container-iri`](https://www.w3.org/TR/epub-33/#sec-container-iri):

> In addition, all relative-URL-with-fragment strings [url] MUST, after parsing, be equal to the content URL of an existing file in the OCF abstract container.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The `@import` comes after a style rule, so it is invalid, and CSS discards it. Nothing is imported, and no file is fetched. The parsed style sheet holds one rule, `p { margin: 0; }`, and refers to no other file. So no URL in it has to be the content URL of an existing file. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it.

This follows the reading used for `direction` in the CSS sets: what counts is what the parsed style sheet holds. [w3c/epub-specs#3115](https://github.com/w3c/epub-specs/issues/3115) answered that question for properties ("It means the property must be declared"). A dropped rule refers to a file no more than a dropped declaration declares a property.

CSS result: One rule is kept, `p { margin: 0; }`. The `@import` comes after a style rule, so it is invalid and dropped (a parse error), and `missing.css` is not requested.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i import-after-rule-missing.epub -u --advisory` | USAGE ADV-021; VALID | `import-after-rule-missing.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck import-after-rule-missing.epub -u` | ERROR RSC-007; INVALID | `import-after-rule-missing.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result: its USAGE ADV-021 says that browsers ignore the `@import`. epubcheck does not: it reports the URL of the dropped `@import` as a missing resource (RSC-007).

- **epubcheck: wrong error.** [w3c/epubcheck#1787](https://github.com/w3c/epubcheck/issues/1787).

Every epubveri finding here is in its default output, except USAGE ADV-021, which is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then `@import "missing.css";`, in UTF-8. There is no `missing.css`.

## History

- 2026-11-28: First version.
