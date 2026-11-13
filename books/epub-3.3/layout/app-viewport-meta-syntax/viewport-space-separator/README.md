# A viewport with only a space as separator (valid)

- Book: `viewport-space-separator.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-space-separator/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#341](https://github.com/veripublica/epub-test-books/issues/341)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width=1200 height=600, with only a space between the two properties. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. A space is a `sep-char` on its own, so the two properties are separated as the grammar requires.

## Question

The viewport of `content.xhtml` is `width=1200 height=600`, with no comma. Does a validator accept it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> viewport = property, { sep, property } ; property = name, [ assign, value ] ; name = ? character data ? ; value = ? character data ? ; sep = sep-char, { sep-char } ; sep-char = ( ";" | "," | space ) ; assign = [ space ], "=", [ space ] ; space = #x20 ;

## Expected result

Valid. A space is a `sep-char` on its own, so the two properties are separated as the grammar requires.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i viewport-space-separator.epub -u --advisory` | no findings; VALID | `viewport-space-separator.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-space-separator.epub -u` | no findings; VALID | `viewport-space-separator.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width=1200 height=600"`.

## History

- 2026-11-12: First version.
