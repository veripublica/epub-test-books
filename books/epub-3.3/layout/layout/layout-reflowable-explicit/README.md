# `rendition:layout` set to `reflowable` (valid)

- Book: `layout-reflowable-explicit.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/layout/layout-reflowable-explicit/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#231](https://github.com/veripublica/epub-test-books/issues/231)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:layout to reflowable, its default value. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. `reflowable` is one of the two values, and the default.

## Question

The package sets `rendition:layout` to `reflowable`, its default value. Does a validator accept it?

## Clause

EPUB 3.3, [`layout`](https://www.w3.org/TR/epub-33/#layout):

> EPUB creators MUST use one of the following values with the rendition:layout property: reflowable […] pre-paginated […]

## Expected result

Valid. `reflowable` is one of the two values, and the default.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i layout-reflowable-explicit.epub -u --advisory` | no findings; VALID | `layout-reflowable-explicit.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck layout-reflowable-explicit.epub -u` | no findings; VALID | `layout-reflowable-explicit.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:layout">reflowable</meta>` is added to the metadata.

## History

- 2026-11-11: First version.
