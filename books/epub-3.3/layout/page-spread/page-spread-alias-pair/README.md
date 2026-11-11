# `rendition:page-spread-left` with its alias `page-spread-left` (valid)

- Book: `page-spread-alias-pair.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/page-spread/page-spread-alias-pair/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#255](https://github.com/veripublica/epub-test-books/issues/255)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has rendition:page-spread-left page-spread-left, the same placement in both vocabularies. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. The clause names this exact pair as valid.

## Question

The content document's `itemref` has `rendition:page-spread-left page-spread-left`, the same placement in both vocabularies. Does a validator accept it?

## Clause

EPUB 3.3, [`page-spread`](https://www.w3.org/TR/epub-33/#page-spread):

> EPUB creators MUST NOT declare more than one rendition:page-spread-* property, and/or their unprefixed equivalents, on any given spine item (e.g., it is valid to specify both "rendition:page-spread-left page-spread-left" in case reading systems only support one of properties).

## Expected result

Valid. The clause names this exact pair as valid.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i page-spread-alias-pair.epub -u --advisory` | no findings; VALID | `page-spread-alias-pair.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck page-spread-alias-pair.epub -u` | no findings; VALID | `page-spread-alias-pair.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and the content document's `itemref` gets `properties="rendition:page-spread-left page-spread-left"`.

## History

- 2026-11-11: First version.
