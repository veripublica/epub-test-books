# A stylesheet with `@charset "utf-8";` after a rule (valid)

- Book: `charset-utf-8-later.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/charset-utf-8-later/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It has @charset "utf-8"; after its first rule and holds only ASCII. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet is decoded as UTF-8.

## Question

`style.css` holds `p { margin: 0; }`, then `@charset "utf-8";`, all ASCII. Which encoding does a CSS parser decode it with, and does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> Otherwise, check stylesheet’s byte stream. If the first 1024 bytes of the stream begin with the hex sequence 40 63 68 61 72 73 65 74 20 22 XX* 22 3B where each XX byte is a value between 0₁₆ and 21₁₆ inclusive or a value between 23₁₆ and 7F₁₆ inclusive, then get an encoding from a string formed out of the sequence of XX bytes, interpreted as ASCII.

> Otherwise, if an environment encoding is provided by the referring document, return it.

> Otherwise, return utf-8.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet is decoded as UTF-8.

CSS result: The declaration is not at the start, so it is not recognized; the sheet takes the referring document's encoding, UTF-8. The later line parses as an unknown at-rule, which a CSS parser drops.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i charset-utf-8-later.epub -u --advisory` | no findings; VALID | `charset-utf-8-later.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck charset-utf-8-later.epub -u` | no findings; VALID | `charset-utf-8-later.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` holds `p { margin: 0; }`, then `@charset "utf-8";`, all ASCII.

## History

- 2026-11-11: First version.
