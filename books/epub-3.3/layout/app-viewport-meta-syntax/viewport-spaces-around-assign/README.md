# A viewport with spaces around `=` and `,` (valid)

- Book: `viewport-spaces-around-assign.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-spaces-around-assign/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#276](https://github.com/veripublica/epub-test-books/issues/276)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width = 1200 , height = 600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. `assign` allows a space on each side of `=`, and a separator may be several separator characters, so ` , ` is one separator.

## Question

The viewport of `content.xhtml` is `width = 1200 , height = 600`. Does a validator accept it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> sep-char = ( ";" | "," | space ) ; assign = [ space ], "=", [ space ] ; space = #x20 ;

## Expected result

Valid. `assign` allows a space on each side of `=`, and a separator may be several separator characters, so ` , ` is one separator.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i viewport-spaces-around-assign.epub -u --advisory` | no findings; VALID | `viewport-spaces-around-assign.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-spaces-around-assign.epub -u` | no findings; VALID | `viewport-spaces-around-assign.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width = 1200 , height = 600"`.

## History

- 2026-11-11: First version.
