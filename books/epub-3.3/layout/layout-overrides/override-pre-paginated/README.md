# One document made pre-paginated by a spine override (valid)

- Book: `override-pre-paginated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout-overrides/override-pre-paginated/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is reflowable, and the content document's itemref has rendition:layout-pre-paginated. That document has a viewport of width=1200, height=600. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The override sets the layout for that one spine item, and the item gives its dimensions.

## Question

The book is reflowable, and the content document's `itemref` has `rendition:layout-pre-paginated`. That document has a viewport. Does a validator accept it?

## Clause

EPUB 3.3, [`layout-overrides`](https://www.w3.org/TR/epub-33/#layout-overrides):

> EPUB creators MAY specify the following properties locally on spine itemref elements to override the global value for the given spine item:

## Expected result

Valid. The override sets the layout for that one spine item, and the item gives its dimensions.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i override-pre-paginated.epub -u --advisory` | no findings; VALID | `override-pre-paginated.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck override-pre-paginated.epub -u` | no findings; VALID | `override-pre-paginated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `content.xhtml` gets `<meta name="viewport" content="width=1200, height=600"/>` and its `itemref` gets `properties="rendition:layout-pre-paginated"`.

## History

- 2026-11-11: First version.
