# `all: unset`, which leaves `direction` and `unicode-bidi` alone (valid)

- Book: `all-unset.epub`, built from the EPUB 3 template
- Built by: `scripts/css-cascade-5/all-shorthand/all-unset/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#379](https://github.com/veripublica/epub-test-books/issues/379)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { all: unset; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. all resets every property except direction and unicode-bidi, so the sheet does not include either. It is UTF-8, so EPUB 3.3 asks nothing more of it.

## Question

`style.css` holds `p { all: unset; }`. Does a validator accept the book?

## Clause

CSS Cascading and Inheritance Level 5, [`all-shorthand`](https://www.w3.org/TR/css-cascade-5/#all-shorthand) (3.2. Resetting All Properties: the all property; Candidate Recommendation Snapshot, 13 January 2022):

> The all property is a shorthand that resets all CSS properties except direction and unicode-bidi. It only accepts the CSS-wide keywords.

CSS Cascading and Inheritance Level 5, [`all-shorthand`](https://www.w3.org/TR/css-cascade-5/#all-shorthand) (3.2. Resetting All Properties: the all property; Candidate Recommendation Snapshot, 13 January 2022), a note, which is not normative:

> Note: The excepted CSS properties direction and unicode-bidi are actually markup-level features, and should not be set in the author’s style sheet.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. `all` resets every property except `direction` and `unicode-bidi`, so the sheet does not include either. It is UTF-8, so EPUB 3.3 asks nothing more of it.

CSS result: One rule with one declaration, `all: unset`. It sets every property of `p` except `direction` and `unicode-bidi` (and custom properties) to `unset`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i all-unset.epub -u --advisory` | no findings; VALID | `all-unset.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck all-unset.epub -u` | no findings; VALID | `all-unset.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { all: unset; }`, in UTF-8.

## History

- 2026-11-12: First version.
