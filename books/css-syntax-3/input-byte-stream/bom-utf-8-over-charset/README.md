# A UTF-8 byte order mark before `@charset "iso-8859-1";` (valid)

- Book: `bom-utf-8-over-charset.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/bom-utf-8-over-charset/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It starts with a UTF-8 byte order mark and then @charset "iso-8859-1";, and is written in UTF-8. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet is decoded as UTF-8.

## Question

`style.css` starts with a UTF-8 byte order mark, then `@charset "iso-8859-1";`, then `p { margin: 0; }` and `.x::before { content: "é"; }`, all in UTF-8. Which encoding does a CSS parser decode it with, and does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> To decode a stylesheet’s stream of bytes into a stream of code points: Determine the fallback encoding of stylesheet, and let fallback be the result. Decode stylesheet’s stream of bytes with fallback encoding fallback, and return the result.

> Note: The decode algorithm gives precedence to a byte order mark (BOM), and only uses the fallback when none is found.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet is decoded as UTF-8.

CSS result: The byte order mark takes precedence over the declaration, so the sheet decodes as UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i bom-utf-8-over-charset.epub -u --advisory` | no findings; VALID | `bom-utf-8-over-charset.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck bom-utf-8-over-charset.epub -u` | no findings; VALID | `bom-utf-8-over-charset.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` starts with a UTF-8 byte order mark, then `@charset "iso-8859-1";`, then `p { margin: 0; }` and `.x::before { content: "é"; }`, all in UTF-8.

## History

- 2026-11-11: First version.
