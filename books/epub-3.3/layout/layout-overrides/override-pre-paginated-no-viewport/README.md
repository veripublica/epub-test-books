# A spine override to pre-paginated, with no viewport

- Book: `override-pre-paginated-no-viewport.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout-overrides/override-pre-paginated-no-viewport/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#238](https://github.com/veripublica/epub-test-books/issues/238)
- Other clauses: `layout`, `sec-fxl-icb-html`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is reflowable, and the content document's itemref has rendition:layout-pre-paginated, but that document has no viewport. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The override makes the document pre-paginated, so it must give its dimensions.

## Question

The book is reflowable, and the content document's `itemref` has `rendition:layout-pre-paginated`, but that document has no viewport. Does a validator reject it?

## Clause

EPUB 3.3, [`layout-overrides`](https://www.w3.org/TR/epub-33/#layout-overrides):

> EPUB creators MAY specify the following properties locally on spine itemref elements to override the global value for the given spine item:

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> When the property is set to pre-paginated for a spine item, its content dimensions MUST be set as defined in 8.2.2.6 Content document dimensions.

## Expected result

Invalid. The override makes the document pre-paginated, so it must give its dimensions.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i override-pre-paginated-no-viewport.epub -u --advisory` | ERROR HTM-046; INVALID | `override-pre-paginated-no-viewport.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck override-pre-paginated-no-viewport.epub -u` | ERROR HTM-046; INVALID | `override-pre-paginated-no-viewport.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, the content document's `itemref` gets `properties="rendition:layout-pre-paginated"`.

## History

- 2026-11-11: First version.
