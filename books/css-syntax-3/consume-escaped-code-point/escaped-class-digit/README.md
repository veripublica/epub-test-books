# A class selector that starts with an escaped digit, `.\31 0` (valid)

- Book: `escaped-class-digit.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-escaped-code-point/escaped-class-digit/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#361](https://github.com/veripublica/epub-test-books/issues/361)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds .\31 0 { margin: 0; }. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `.\31 0 { margin: 0; }`. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-escaped-code-point`](https://www.w3.org/TR/css-syntax-3/#consume-escaped-code-point) (4.3.7 Consume an escaped code point; Candidate Recommendation Draft, 1 October 2026):

> Consume as many hex digits as possible, but no more than 5. Note that this means 1-6 hex digits have been consumed in total. If the next input code point is whitespace, consume it as well. Interpret the hex digits as a hexadecimal number.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, selector `.10`: `\31 ` is the escape for `1`, and the space after it is part of the escape.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i escaped-class-digit.epub -u --advisory` | no findings; VALID | `escaped-class-digit.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck escaped-class-digit.epub -u` | no findings; VALID | `escaped-class-digit.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `.\31 0 { margin: 0; }`, in UTF-8.

## History

- 2026-11-12: First version.
