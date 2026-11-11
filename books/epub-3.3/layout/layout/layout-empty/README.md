# `rendition:layout` with an empty value

- Book: `layout-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout/layout-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#233](https://github.com/veripublica/epub-test-books/issues/233)
- Other clauses: `sec-metadata-values`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package declares rendition:layout with an empty value. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. An empty value is not `reflowable` or `pre-paginated`.

## Question

The package declares `rendition:layout` with an empty value. Does a validator reject it?

## Clause

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> EPUB creators MUST use one of the following values with the rendition:layout property: reflowable […] pre-paginated […]

## Expected result

Invalid. An empty value is not `reflowable` or `pre-paginated`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i layout-empty.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005, USAGE HTM_060b, USAGE HTM_060b; INVALID | `layout-empty.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck layout-empty.epub -u` | ERROR RSC-005, ERROR RSC-005, USAGE HTM_060b, USAGE HTM_060b; INVALID | `layout-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report two RSC-005 errors: the value is not one of the two, and a `meta` element must have a non-empty value (EPUB 3.3 `sec-metadata-values`). Both follow from the one change. The message lists a third value, `roll`, from the EPUB 3.4 draft; epubcheck says it validates with EPUB 3.4 rules. EPUB 3.3 has only the two values, and the verdict is the same under either. USAGE HTM_060b (once for each document) says the viewport is not checked because the document is reflowable: with the bad declaration ignored, the book falls back to the default layout, `reflowable`. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the `rendition:layout` meta element left empty.

## History

- 2026-11-11: First version.
