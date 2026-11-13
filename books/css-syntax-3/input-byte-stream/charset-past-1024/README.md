# A `@charset` declaration that ends after byte 1024 (valid)

- Book: `charset-past-1024.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/charset-past-1024/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria
- Issue: [#330](https://github.com/veripublica/epub-test-books/issues/330)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It starts with a @charset declaration for iso-8859-1, padded with spaces so that it ends at byte 1,025, and holds only ASCII. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet is decoded as UTF-8.

## Question

`style.css` starts with `@charset "`, 1,003 spaces, `iso-8859-1";`, then `p { margin: 0; }`, all ASCII. Its closing `;` is byte 1,025. Which encoding does a CSS parser decode it with, and does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> Otherwise, check stylesheet’s byte stream. If the first 1024 bytes of the stream begin with the hex sequence 40 63 68 61 72 73 65 74 20 22 XX* 22 3B where each XX byte is a value between 0₁₆ and 21₁₆ inclusive or a value between 23₁₆ and 7F₁₆ inclusive, then get an encoding from a string formed out of the sequence of XX bytes, interpreted as ASCII.

> Otherwise, if an environment encoding is provided by the referring document, return it.

> Otherwise, return utf-8.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet is decoded as UTF-8.

CSS result: The declaration must lie within the first 1,024 bytes. Its last byte is byte 1,025, so it is not recognized, and the sheet takes the referring document's encoding, UTF-8. Were it recognized, the spaces would be removed and the sheet would decode as windows-1252.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i charset-past-1024.epub -u --advisory` | no findings; VALID | `charset-past-1024.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck charset-past-1024.epub -u` | no findings; VALID | `charset-past-1024.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` starts with `@charset "`, 1,003 spaces, `iso-8859-1";`, then `p { margin: 0; }`, all ASCII. Its closing `;` is byte 1,025.

## History

- 2026-11-11: First version.
