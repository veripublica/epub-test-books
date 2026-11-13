# A `unicode-bidi` property name written with an escape, `\75nicode-bidi`

- Book: `unicode-bidi-escaped-name.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-escaped-code-point/unicode-bidi-escaped-name/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#362](https://github.com/veripublica/epub-test-books/issues/362)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { \75nicode-bidi: embed; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. \75 is the escape for u, so the property name is unicode-bidi.

## Question

`style.css` holds `p { \75nicode-bidi: embed; }`. Does a validator reject the book?

## Clause

CSS Syntax Level 3, [`consume-escaped-code-point`](https://www.w3.org/TR/css-syntax-3/#consume-escaped-code-point) (4.3.7 Consume an escaped code point; Candidate Recommendation Draft, 1 October 2026):

> Consume as many hex digits as possible, but no more than 5. Note that this means 1-6 hex digits have been consumed in total. If the next input code point is whitespace, consume it as well. Interpret the hex digits as a hexadecimal number.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. `\75` is the escape for `u`, so the property name is `unicode-bidi`.

CSS result: One rule with one declaration, `unicode-bidi: embed`. The escape `\75` ends at `n`, which is not a hex digit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i unicode-bidi-escaped-name.epub -u --advisory` | ERROR CSS-001; INVALID | `unicode-bidi-escaped-name.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck unicode-bidi-escaped-name.epub -u` | ERROR CSS-001; INVALID | `unicode-bidi-escaped-name.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { \75nicode-bidi: embed; }`, in UTF-8.

## History

- 2026-11-12: First version.
