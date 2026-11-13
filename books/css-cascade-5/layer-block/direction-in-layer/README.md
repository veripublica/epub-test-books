# `direction: rtl` inside an `@layer` block

- Book: `direction-in-layer.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/layer-block/direction-in-layer/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#390](https://github.com/veripublica/epub-test-books/issues/390)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds @layer base { p { direction: rtl; } }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The style rule inside the @layer block is kept, with its direction declaration.

## Question

`style.css` holds `@layer base { p { direction: rtl; } }`. Does a validator reject the book?

## Clause

CSS Cascading and Inheritance Level 5, [`layer-block`](https://www.w3.org/TR/css-cascade-5/#layer-block) (6.4.4.1. Assigning Styles Inline: the @layer block at-rule; Candidate Recommendation Snapshot, 13 January 2022):

> The @layer block at-rule assigns its child style rules to a particular named cascade layer.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. The style rule inside the `@layer` block is kept, with its `direction` declaration.

CSS result: One `@layer base` block rule holding one style rule with one declaration, `direction: rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-in-layer.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-in-layer.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-in-layer.epub -u` | ERROR CSS-001; INVALID | `direction-in-layer.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `@layer base { p { direction: rtl; } }`, in UTF-8.

## History

- 2026-11-12: First version.
