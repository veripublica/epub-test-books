# `direction: inherit`

- Book: `direction-inherit.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/inherit/direction-inherit/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#388](https://github.com/veripublica/epub-test-books/issues/388)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { direction: inherit; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. inherit is a value every property takes, so this is a direction declaration.

## Question

`style.css` holds `p { direction: inherit; }`. Does a validator reject the book?

## Clause

CSS Cascading and Inheritance Level 5, [`inherit`](https://www.w3.org/TR/css-cascade-5/#inherit) (7.3.2. Explicit Inheritance: the inherit keyword; Candidate Recommendation Snapshot, 13 January 2022):

> If the cascaded value of a property is the inherit keyword, the property’s specified and computed values are the inherited value.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. `inherit` is a value every property takes, so this is a `direction` declaration.

CSS result: One rule with one declaration, `direction: inherit`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i direction-inherit.epub -u --advisory` | ERROR CSS-001; INVALID | `direction-inherit.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck direction-inherit.epub -u` | ERROR CSS-001; INVALID | `direction-inherit.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { direction: inherit; }`, in UTF-8.

## History

- 2026-11-12: First version.
