# A viewport with a property besides width and height (valid)

- Book: `viewport-extra-property.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/sec-fxl-icb-html/viewport-extra-property/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending
- Other clauses: `app-viewport-meta-syntax`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width=1200, height=600, initial-scale=1.0. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. The width and height are there; the grammar allows other properties, and no clause forbids them.

## Question

The viewport of `content.xhtml` is `width=1200, height=600, initial-scale=1.0`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> viewport = property, { sep, property } ; property = name, [ assign, value ] ;

## Expected result

Valid. The width and height are there; the grammar allows other properties, and no clause forbids them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-extra-property.epub -u --advisory` | no findings; VALID | `viewport-extra-property.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-extra-property.epub -u` | no findings; VALID | `viewport-extra-property.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width=1200, height=600, initial-scale=1.0"`.

## History

- 2026-11-11: First version.
