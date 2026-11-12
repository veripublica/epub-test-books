# A UTF-8 stylesheet that declares `@charset "utf-16";` (valid)

- Book: `charset-utf-16-label-utf-8-bytes.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/charset-utf-16-label-utf-8-bytes/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It starts with @charset "utf-16"; and is written in UTF-8. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet is decoded as UTF-8.

## Question

`style.css` starts with `@charset "utf-16";`, then `p { margin: 0; }` and `.x::before { content: "é"; }`, all in UTF-8. Which encoding does a CSS parser decode it with, and does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> Otherwise, check stylesheet’s byte stream. If the first 1024 bytes of the stream begin with the hex sequence 40 63 68 61 72 73 65 74 20 22 XX* 22 3B where each XX byte is a value between 0₁₆ and 21₁₆ inclusive or a value between 23₁₆ and 7F₁₆ inclusive, then get an encoding from a string formed out of the sequence of XX bytes, interpreted as ASCII.

> If the return value was utf-16be or utf-16le, return utf-8; if it was anything else except failure, return it.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet is decoded as UTF-8.

CSS result: The label utf-16 gives the encoding UTF-16LE, and a declared utf-16be or utf-16le is replaced by utf-8, so the sheet decodes as UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i charset-utf-16-label-utf-8-bytes.epub -u --advisory` | no findings; VALID | `charset-utf-16-label-utf-8-bytes.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck charset-utf-16-label-utf-8-bytes.epub -u` | WARNING CSS-003, ERROR CSS-008; INVALID | `charset-utf-16-label-utf-8-bytes.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it decodes the sheet as UTF-16, warns about UTF-16 (CSS-003) and then cannot parse it (CSS-008).

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` starts with `@charset "utf-16";`, then `p { margin: 0; }` and `.x::before { content: "é"; }`, all in UTF-8.

## History

- 2026-11-11: First version.
