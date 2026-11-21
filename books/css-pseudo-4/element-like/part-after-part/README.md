# `::part()` after `::part()`, `x-a::part(a)::part(b)` (valid)

- Book: `part-after-part.epub`, built from the EPUB 3 template
- Built by: `scripts/css-pseudo-4/element-like/part-after-part/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, for its 0.21 release (note 2026-11-18)
- Issue: [#652](https://github.com/veripublica/epub-test-books/issues/652)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds x-a::part(a)::part(b) { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `x-a::part(a)::part(b) { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Pseudo-Elements Module Level 4, [`element-like`](https://www.w3.org/TR/css-pseudo-4/#element-like) (5. Element-backed Pseudo-elements; Working Draft, 27 June 2025):

> All pseudo-classes and pseudo-elements are syntactically allowed after an element-backed pseudo-element (such as x-button::part(label):hover or x-button::part(label)::before), just as if the pseudo-element were a type selector; but some are disallowed from matching:

> ::part() never matches. (Other element-backed pseudo-elements can, however.)

Selectors Level 4, [`sub-pseudo-elements`](https://www.w3.org/TR/selectors-4/#sub-pseudo-elements) (3.6.4. Sub-pseudo-elements; Working Draft, 22 January 2026):

> Unless the corresponding sub-pseudo-element is explicitly defined to exist in another specification, pseudo-element selectors are not valid when compounded to another pseudo-element selector.
>
> So, for example, ::before::before is an invalid selector, but ::before::marker is valid (in implementations that support the ::before::marker sub-pseudo-element).

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, kept, that never matches. Any pseudo-element is allowed after an element-backed pseudo-element such as `::part()`, so the selector is valid, but `::part()` there never matches.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i part-after-part.epub -u --advisory` | no findings; VALID | `part-after-part.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck part-after-part.epub -u` | no findings; VALID | `part-after-part.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `x-a::part(a)::part(b) { margin: 0; }`, in UTF-8.

## History

- 2026-11-18: First version.
