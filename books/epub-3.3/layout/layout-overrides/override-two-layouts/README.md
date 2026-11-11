# Two layout overrides on one spine item

- Book: `override-two-layouts.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout-overrides/override-two-layouts/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has both rendition:layout-pre-paginated and rendition:layout-reflowable. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. Only one layout override is allowed on a spine item.

## Question

The content document's `itemref` has both `rendition:layout-pre-paginated` and `rendition:layout-reflowable`. Does a validator reject it?

## Clause

EPUB 3.3, [`layout-overrides`](https://www.w3.org/TR/epub-33/#layout-overrides):

> EPUB creators MUST NOT use more than one of these overrides on any given spine item.

## Expected result

Invalid. Only one layout override is allowed on a spine item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i override-two-layouts.epub -u --advisory` | ERROR RSC-005; INVALID | `override-two-layouts.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck override-two-layouts.epub -u` | ERROR RSC-005; INVALID | `override-two-layouts.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the content document's `itemref` gets `properties="rendition:layout-pre-paginated rendition:layout-reflowable"`.

## History

- 2026-11-11: First version.
