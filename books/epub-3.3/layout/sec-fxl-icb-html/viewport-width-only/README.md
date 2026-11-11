# A viewport with a width and no height

- Book: `viewport-width-only.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-width-only/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width=1200, with no height. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. Both the height and the width are required.

## Question

The viewport of `content.xhtml` is `width=1200`, with no height. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

## Expected result

Invalid. Both the height and the width are required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-width-only.epub -u --advisory` | ERROR HTM_056; INVALID | `viewport-width-only.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-width-only.epub -u` | ERROR HTM_056; INVALID | `viewport-width-only.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width=1200"`.

## History

- 2026-11-11: First version.
