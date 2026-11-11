# A fixed-layout document with no viewport

- Book: `fxl-viewport-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout/fxl-viewport-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#236](https://github.com/veripublica/epub-test-books/issues/236)
- Other clauses: `sec-fxl-icb-html`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is fixed-layout, and content.xhtml has no viewport meta tag. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. A pre-paginated XHTML document must give its width and height in a viewport meta tag.

## Question

The book is fixed-layout, and `content.xhtml` has no viewport meta tag. Does a validator reject it?

## Clause

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> When the property is set to pre-paginated for a spine item, its content dimensions MUST be set as defined in 8.2.2.6 Content document dimensions.

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

## Expected result

Invalid. A pre-paginated XHTML document must give its width and height in a viewport meta tag.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i fxl-viewport-missing.epub -u --advisory` | ERROR HTM-046; INVALID | `fxl-viewport-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck fxl-viewport-missing.epub -u` | ERROR HTM-046; INVALID | `fxl-viewport-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), without the viewport tag in `content.xhtml`.

## History

- 2026-11-11: First version.
