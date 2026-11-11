# A viewport with two widths

- Book: `viewport-width-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-width-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width=1200, width=1000, height=600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. A viewport meta tag may have only one width definition.

## Question

The viewport of `content.xhtml` is `width=1200, width=1000, height=600`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> EPUB creators MUST NOT specify more than one height or width definition within a viewport meta tag.

## Expected result

Invalid. A viewport meta tag may have only one width definition.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-width-twice.epub -u --advisory` | ERROR HTM_059; INVALID | `viewport-width-twice.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-width-twice.epub -u` | ERROR HTM_059; INVALID | `viewport-width-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width=1200, width=1000, height=600"`.

## History

- 2026-11-11: First version.
