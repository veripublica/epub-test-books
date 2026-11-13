# A complex selector inside `:not()`, `p:not(div p)` (valid)

- Book: `not-complex.epub`, built from the EPUB 3 template
- Built by: `scripts/selectors-4/negation/not-complex/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, for styloria (selectors and cascade)
- Issue: [#400](https://github.com/veripublica/epub-test-books/issues/400)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p:not(div p) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p:not(div p) { margin: 0; }`. Does a validator accept the book?

## Clause

Selectors Level 4, [`negation`](https://www.w3.org/TR/selectors-4/#negation) (4.3. The Negation (Matches-None) Pseudo-class: :not(); Working Draft, 22 January 2026):

> The negation pseudo-class, :not(), is a functional pseudo-class taking a <complex-real-selector-list> as an argument. It represents an element that is not represented by its argument.
>
> Note: In Selectors Level 3, only a single simple selector was allowed as the argument to :not().

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept: every `p` that is not inside a `div`. In Selectors Level 3 this selector was invalid.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i not-complex.epub -u --advisory` | no findings; VALID | `not-complex.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck not-complex.epub -u` | no findings; VALID | `not-complex.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p:not(div p) { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
