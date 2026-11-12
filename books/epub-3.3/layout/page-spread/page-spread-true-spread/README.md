# A true spread across two documents (valid)

- Book: `page-spread-true-spread.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/page-spread/page-spread-true-spread/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#258](https://github.com/veripublica/epub-test-books/issues/258)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The two spine documents form a true spread: the about document's itemref has page-spread-left, and the content document's has page-spread-right. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. This is the form the clause recommends for a true spread.

## Question

The about document's `itemref` has `page-spread-left` and the content document's has `page-spread-right`, so the two pages form one spread. Does a validator accept it?

## Clause

EPUB 3.3, [`page-spread`](https://www.w3.org/TR/epub-33/#page-spread):

> To indicate that two consecutive pages represent a true spread, EPUB creators SHOULD use the rendition:page-spread-left and rendition:page-spread-right properties on the spine items for the two adjacent EPUB content documents, and omit the properties on spine items where one-up or two-up presentation is equally acceptable.

## Expected result

Valid. This is the form the clause recommends for a true spread.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i page-spread-true-spread.epub -u --advisory` | no findings; VALID | `page-spread-true-spread.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck page-spread-true-spread.epub -u` | no findings; VALID | `page-spread-true-spread.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the two `itemref` elements get `properties="page-spread-left"` (about) and `properties="page-spread-right"` (content).

## History

- 2026-11-11: First version.
