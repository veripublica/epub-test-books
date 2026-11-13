# A stylesheet whose last byte is a backslash (valid)

- Book: `escape-at-eof.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/consume-escaped-code-point/escape-at-eof/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria, after its review of the encoding sets
- Issue: [#360](https://github.com/veripublica/epub-test-books/issues/360)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It holds p { margin: 0; }, then a line with only \, which is the last byte of the file. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet holds neither direction nor unicode-bidi, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

## Question

`style.css` holds `p { margin: 0; }`, then a line with only `\`, which is the last byte of the file. Does a validator accept the book?

## Clause

CSS Syntax Level 3, [`consume-escaped-code-point`](https://www.w3.org/TR/css-syntax-3/#consume-escaped-code-point) (4.3.7 Consume an escaped code point; Candidate Recommendation Draft, 1 October 2026):

> EOF
>
> This is a parse error. Return U+FFFD REPLACEMENT CHARACTER (�).

CSS Syntax Level 3, [`starts-with-a-valid-escape`](https://www.w3.org/TR/css-syntax-3/#starts-with-a-valid-escape) (4.3.8 Check if two code points are a valid escape; Candidate Recommendation Draft, 1 October 2026):

> If the first code point is not U+005C REVERSE SOLIDUS (\), return false.
>
> Otherwise, if the second code point is a newline, return false.
>
> Otherwise, return true.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MAY include any CSS properties, with the following exceptions:

> It MUST NOT include the direction property [css-writing-modes-3].

> It MUST NOT include the unicode-bidi property [css-writing-modes-3].

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet holds neither `direction` nor `unicode-bidi`, and it is UTF-8, so EPUB 3.3 asks nothing more of it. A parse error is not one of its requirements.

CSS result: One rule, `p { margin: 0; }`. The backslash and EOF make an escape: a parse error that gives U+FFFD. That ident starts a qualified rule that ends at EOF with no block, another parse error, and nothing is added.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i escape-at-eof.epub -u --advisory` | USAGE CSS-008, USAGE CSS-008; VALID | `escape-at-eof.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck escape-at-eof.epub -u` | ERROR CSS-008, ERROR CSS-008, ERROR CSS-008; INVALID | `escape-at-eof.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the parse error as errors (CSS-008).

- **epubcheck: wrong error.** [w3c/epubcheck#1768](https://github.com/w3c/epubcheck/issues/1768).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml` and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then a line with only `\`, which is the last byte of the file, in UTF-8.

## History

- 2026-11-12: First version.
