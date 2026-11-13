# A stylesheet with `@charset 'iso-8859-1';` in single quotes (valid)

- Book: `charset-single-quotes.epub`, built from the EPUB 3 template
- Built by: `scripts/css-syntax-3/input-byte-stream/charset-single-quotes/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: styloria
- Issue: pending
- Other clauses: EPUB 3.3 `sec-css-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links one stylesheet, style.css. It starts with @charset 'iso-8859-1'; in single quotes and holds only ASCII. This document is not styled. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The sheet is decoded as UTF-8.

## Question

`style.css` starts with `@charset 'iso-8859-1';`, then `p { margin: 0; }`, all ASCII. Which encoding does a CSS parser decode it with, and does a validator accept the book?

## Clause

CSS Syntax Level 3, [`input-byte-stream`](https://www.w3.org/TR/css-syntax-3/#input-byte-stream) (Candidate Recommendation Draft, 1 October 2026):

> Otherwise, check stylesheet’s byte stream. If the first 1024 bytes of the stream begin with the hex sequence 40 63 68 61 72 73 65 74 20 22 XX* 22 3B where each XX byte is a value between 0₁₆ and 21₁₆ inclusive or a value between 23₁₆ and 7F₁₆ inclusive, then get an encoding from a string formed out of the sequence of XX bytes, interpreted as ASCII.

> A number of things you can do in CSS that would produce a valid @charset rule (if one existed), such as using multiple spaces, comments, or single quotes, will cause the encoding declaration to not be recognized.

> Otherwise, if an environment encoding is provided by the referring document, return it.

> Otherwise, return utf-8.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> A CSS style sheet: […] MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Valid. The sheet is decoded as UTF-8.

CSS result: The declaration must use double quotes. With single quotes it is not recognized, so the sheet takes the referring document's encoding, UTF-8. The line parses as an unknown at-rule, which a CSS parser drops.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i charset-single-quotes.epub -u --advisory` | no findings; VALID | `charset-single-quotes.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck charset-single-quotes.epub -u` | ERROR CSS-004; INVALID | `charset-single-quotes.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reads the single-quoted line as a declaration of ISO-8859-1 (CSS-004).

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `class="x"` on its paragraph, and `OEBPS/style.css` (`text/css`) in the manifest. `style.css` starts with `@charset 'iso-8859-1';`, then `p { margin: 0; }`, all ASCII.

## History

- 2026-11-11: First version.
