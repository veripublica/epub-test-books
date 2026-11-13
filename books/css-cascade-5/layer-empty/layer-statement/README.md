# An `@layer` statement, `@layer a, b;` (valid)

- Book: `layer-statement.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/layer-empty/layer-statement/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#391](https://github.com/veripublica/epub-test-books/issues/391)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @layer a, b;, then @layer b { p { margin: 0; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `@layer a, b;`, then `@layer b { p { margin: 0; } }`. Does a validator accept the book?

## Clause

CSS Cascading and Inheritance Level 5, [`layer-empty`](https://www.w3.org/TR/css-cascade-5/#layer-empty) (6.4.4.2. Declaring Without Styles: the @layer statement at-rule; Candidate Recommendation Snapshot, 13 January 2022):

> The @layer rule can also be used to define new layers without assigning any style rules, by providing only the layer name:

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: An `@layer` statement that declares the layers `a` and `b`, then an `@layer b` block with one rule, `p { margin: 0; }`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i layer-statement.epub -u --advisory` | no findings; VALID | `layer-statement.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck layer-statement.epub -u` | no findings; VALID | `layer-statement.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@layer a, b;`, then `@layer b { p { margin: 0; } }`, in UTF-8.

## History

- 2026-11-12: First version.
