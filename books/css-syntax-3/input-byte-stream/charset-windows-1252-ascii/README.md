# A stylesheet that declares `windows-1252`, with only ASCII in it

- Book: `charset-windows-1252-ascii.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/charset-windows-1252-ascii/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It starts with @charset "windows-1252"; and holds only ASCII. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The sheet is decoded as windows-1252, which is neither UTF-8 nor UTF-16.

## Question

`style.css` starts with `@charset "windows-1252";`, then `p { margin: 0; }`, all ASCII. Which encoding does a CSS parser decode it with, and does a validator reject the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> Otherwise, check stylesheet’s byte stream. If the first 1024 bytes of the stream begin with the hex sequence 40 63 68 61 72 73 65 74 20 22 XX* 22 3B where each XX byte is a value between 0₁₆ and 21₁₆ inclusive or a value between 23₁₆ and 7F₁₆ inclusive, then get an encoding from a string formed out of the sequence of XX bytes, interpreted as ASCII.

> If the return value was utf-16be or utf-16le, return utf-8; if it was anything else except failure, return it.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. The sheet is decoded as windows-1252, which is neither UTF-8 nor UTF-16.

CSS result: The declaration names windows-1252, so the sheet decodes as windows-1252. Its bytes would read the same as UTF-8, but the encoding a CSS parser uses is windows-1252.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i charset-windows-1252-ascii.epub -u --advisory` | ERROR CSS-004; INVALID | `charset-windows-1252-ascii.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck charset-windows-1252-ascii.epub -u` | ERROR CSS-004; INVALID | `charset-windows-1252-ascii.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` starts with `@charset "windows-1252";`, then `p { margin: 0; }`, all ASCII.

## History

- 2026-11-11: First version.
