# A viewport tag named `Viewport`

- Book: `viewport-name-uppercase.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-name-uppercase/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending
- Other clauses: `sec-fxl-icb-html`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

In a fixed-layout book, the only viewport-like meta tag in content.xhtml has name="Viewport", with a capital V. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The name must be `viewport`, so the document has no viewport meta tag, and its required dimensions are missing.

## Question

In a fixed-layout book, the only viewport-like meta tag in `content.xhtml` has `name="Viewport"`, with a capital V. Does a validator reject it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> The value of the name attribute [html] after whitespace normalization [xml] MUST be viewport.

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

## Expected result

Invalid. The name must be `viewport`, so the document has no viewport meta tag, and its required dimensions are missing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-name-uppercase.epub -u --advisory` | ERROR HTM-046; INVALID | `viewport-name-uppercase.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-name-uppercase.epub -u` | ERROR HTM-046; INVALID | `viewport-name-uppercase.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport tag in `content.xhtml` named `Viewport`.

## History

- 2026-11-11: First version.
