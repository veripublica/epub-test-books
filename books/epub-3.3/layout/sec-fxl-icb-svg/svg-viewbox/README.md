# A fixed-layout SVG document with `viewBox` (valid)

- Book: `svg-viewbox.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-svg/svg-viewbox/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#274](https://github.com/veripublica/epub-test-books/issues/274)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is fixed-layout and has a third spine item, picture.svg, an SVG content document sized by viewBox="0 0 400 400". Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. The SVG document gives its dimensions with `viewBox`.

## Question

A fixed-layout book has an SVG content document in its spine, sized by `viewBox="0 0 400 400"`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-fxl-icb-svg`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-svg):

> For SVG fixed-layout documents, the initial containing block [css2] dimensions MUST be expressed using the viewBox attribute [svg].

## Expected result

Valid. The SVG document gives its dimensions with `viewBox`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-viewbox.epub -u --advisory` | no findings; VALID | `svg-viewbox.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-viewbox.epub -u` | no findings; VALID | `svg-viewbox.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `picture.svg` added to the manifest and the end of the spine, with `viewBox="0 0 400 400"` and no `width` or `height`.

## History

- 2026-11-11: First version.
