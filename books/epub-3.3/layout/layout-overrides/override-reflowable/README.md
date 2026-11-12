# Both documents made reflowable by spine overrides (valid)

- Book: `override-reflowable.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout-overrides/override-reflowable/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#239](https://github.com/veripublica/epub-test-books/issues/239)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book sets rendition:layout to pre-paginated, and both spine items have rendition:layout-reflowable. Neither document has a viewport. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The overrides make both documents reflowable, so the dimension rule does not apply to them.

## Question

The book is pre-paginated, and both spine items have `rendition:layout-reflowable`, so neither needs a viewport. Neither has one. Does a validator accept it?

## Clause

EPUB 3.3, [`layout-overrides`](https://www.w3.org/TR/epub-33/#layout-overrides):

> EPUB creators MAY specify the following properties locally on spine itemref elements to override the global value for the given spine item:

## Expected result

Valid. The overrides make both documents reflowable, so the dimension rule does not apply to them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i override-reflowable.epub -u --advisory` | no findings; VALID | `override-reflowable.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck override-reflowable.epub -u` | no findings; VALID | `override-reflowable.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:layout">pre-paginated</meta>` is added and both `itemref` elements get `properties="rendition:layout-reflowable"`. No document has a viewport tag.

## History

- 2026-11-11: First version.
