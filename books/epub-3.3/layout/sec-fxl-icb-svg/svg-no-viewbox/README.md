# A fixed-layout SVG document without `viewBox`

- Book: `svg-no-viewbox.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-svg/svg-no-viewbox/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#275](https://github.com/veripublica/epub-test-books/issues/275)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is fixed-layout and has a third spine item, picture.svg, an SVG content document sized by width="400" height="400", with no viewBox. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The dimensions of a fixed-layout SVG document must be given with `viewBox`; `width` and `height` do not count.

## Question

A fixed-layout book has an SVG content document in its spine, sized by `width="400" height="400"` and with no `viewBox`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fxl-icb-svg`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-svg):

> For SVG fixed-layout documents, the initial containing block [css2] dimensions MUST be expressed using the viewBox attribute [svg].

## Expected result

Invalid. The dimensions of a fixed-layout SVG document must be given with `viewBox`; `width` and `height` do not count.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i svg-no-viewbox.epub -u --advisory` | ERROR HTM-048; INVALID | `svg-no-viewbox.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-no-viewbox.epub -u` | ERROR HTM-048; INVALID | `svg-no-viewbox.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `picture.svg` added to the manifest and the end of the spine, with `width="400" height="400"` and no `viewBox`.

## History

- 2026-11-11: First version.
