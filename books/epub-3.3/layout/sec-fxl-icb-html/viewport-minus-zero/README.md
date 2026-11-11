# A viewport width of -0

- Book: `viewport-minus-zero.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-minus-zero/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after the fixed-layout sets
- Issue: [#318](https://github.com/veripublica/epub-test-books/issues/318)
- Other clauses: CSS 2.1 `numbers`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width=-0, height=600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. `-0` is a number equal to 0, and 0 is not positive.

## Question

The viewport of `content.xhtml` is `width=-0, height=600`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

[CSS 2.1, 4.3.1 Integers and real numbers](https://www.w3.org/TR/CSS2/syndata.html#numbers):

> Real numbers and integers are specified in decimal notation only. An <integer> consists of one or more digits "0" to "9". A <number> can either be an <integer>, or it can be zero or more digits followed by a dot (.) followed by one or more digits. Both integers and real numbers may be preceded by a "-" or "+" to indicate the sign. -0 is equivalent to 0 and is not a negative number.

## Expected result

Invalid. `-0` is a number equal to 0, and 0 is not positive.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-minus-zero.epub -u --advisory` | ERROR HTM_057; INVALID | `viewport-minus-zero.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-minus-zero.epub -u` | ERROR HTM_057; INVALID | `viewport-minus-zero.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width=-0, height=600"`.

## History

- 2026-11-11: First version.
