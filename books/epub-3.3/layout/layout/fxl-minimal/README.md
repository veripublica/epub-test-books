# A fixed-layout book (valid)

- Book: `fxl-minimal.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout/fxl-minimal/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending
- Other clauses: `sec-fxl-icb-html`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:layout to pre-paginated, and each spine document has a viewport meta tag of width=1200, height=600. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is the fixed-layout form of the template that the other fixed-layout sets start from.

## Question

The package sets `rendition:layout` to `pre-paginated`, and each spine document has a viewport of `width=1200, height=600`. Does a validator accept it?

## Clause

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> EPUB creators MUST use one of the following values with the rendition:layout property: reflowable […] pre-paginated […]

> When the property is set to pre-paginated for a spine item, its content dimensions MUST be set as defined in 8.2.2.6 Content document dimensions.

EPUB 3.3, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-33/#sec-fxl-icb-html):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag, where: the height property MUST have as its value a positive number [css2] or the keyword device-height; and the width property MUST have as its value a positive number [css2] or the keyword device-width.

## Expected result

Valid. This is the fixed-layout form of the template that the other fixed-layout sets start from.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i fxl-minimal.epub -u --advisory` | no findings; VALID | `fxl-minimal.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck fxl-minimal.epub -u` | no findings; VALID | `fxl-minimal.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with nothing else changed.

## History

- 2026-11-11: First version.
