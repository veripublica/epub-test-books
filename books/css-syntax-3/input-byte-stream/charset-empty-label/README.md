# A stylesheet that declares an empty label, `@charset "";` (valid)

- Book: `charset-empty-label.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/charset-empty-label/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria
- Issue: [#325](https://github.com/veripublica/epub-test-books/issues/325)
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It starts with @charset ""; and holds only ASCII. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet is decoded as UTF-8.

## Question

`style.css` starts with `@charset "";`, then `p { margin: 0; }`, all ASCII. Which encoding does a CSS parser decode it with, and does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> Otherwise, check stylesheet’s byte stream. If the first 1024 bytes of the stream begin with the hex sequence 40 63 68 61 72 73 65 74 20 22 XX* 22 3B where each XX byte is a value between 0₁₆ and 21₁₆ inclusive or a value between 23₁₆ and 7F₁₆ inclusive, then get an encoding from a string formed out of the sequence of XX bytes, interpreted as ASCII.

> If the return value was utf-16be or utf-16le, return utf-8; if it was anything else except failure, return it.

> Otherwise, if an environment encoding is provided by the referring document, return it.

> Otherwise, return utf-8.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet is decoded as UTF-8.

CSS result: An empty label names no encoding, so getting an encoding fails and the sheet takes the referring document's encoding, UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i charset-empty-label.epub -u --advisory` | no findings; VALID | `charset-empty-label.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck charset-empty-label.epub -u` | no findings; VALID | `charset-empty-label.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` starts with `@charset "";`, then `p { margin: 0; }`, all ASCII.

## History

- 2026-11-11: First version.
