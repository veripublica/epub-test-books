# `rendition:layout` with `refines`

- Book: `layout-with-refines.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout/layout-with-refines/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#235](https://github.com/veripublica/epub-test-books/issues/235)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rendition:layout meta element has refines="#content", pointing at the content document's manifest item. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The property must not be declared with the `refines` attribute; a spine override is the way to set it for one document.

## Question

The `rendition:layout` meta element has `refines="#content"`, pointing at the content document's manifest item. Does a validator reject it?

## Clause

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> EPUB creators MUST NOT declare the rendition:layout property more than once. They also MUST NOT declare the property using the refines attribute.

## Expected result

Invalid. The property must not be declared with the `refines` attribute; a spine override is the way to set it for one document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i layout-with-refines.epub -u --advisory` | ERROR RSC-005; INVALID | `layout-with-refines.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck layout-with-refines.epub -u` | ERROR RSC-005, USAGE HTM_060b, USAGE HTM_060b; INVALID | `layout-with-refines.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

epubcheck also gives USAGE HTM_060b (once for each document): it ignores the refined declaration, so the book is reflowable and the viewports are not checked. epubveri gives no usage message here. The difference is at usage level and does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), except that the `rendition:layout` meta element carries `refines="#content"`.

## History

- 2026-11-11: First version.
