# A viewport with properties that have no value (valid)

- Book: `viewport-valueless-property.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-valueless-property/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: epubveri, after the fixed-layout sets
- Issue: [#321](https://github.com/veripublica/epub-test-books/issues/321)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is initial-scale 1, width=1200, height=600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. By the grammar, `initial-scale 1` is two properties with no value, `initial-scale` and `1`, separated by a space. Properties without values are allowed; the specification only discourages them.

## Question

The viewport of `content.xhtml` is `initial-scale 1, width=1200, height=600`. Does a validator accept it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> viewport = property, { sep, property } ; property = name, [ assign, value ] ; name = ? character data ? ; value = ? character data ? ; sep = sep-char, { sep-char } ; sep-char = ( ";" | "," | space ) ; assign = [ space ], "=", [ space ] ; space = #x20 ;

> The only restriction on property names and values is that they MUST NOT contain separator characters or the assignment character.

## Expected result

Valid. By the grammar, `initial-scale 1` is two properties with no value, `initial-scale` and `1`, separated by a space. Properties without values are allowed; the specification only discourages them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-valueless-property.epub -u --advisory` | no findings; VALID | `viewport-valueless-property.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-valueless-property.epub -u` | ERROR HTM-047; INVALID | `viewport-valueless-property.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the content as a syntax error (HTM-047).

- **epubcheck: wrong error.** [w3c/epubcheck#1763](https://github.com/w3c/epubcheck/issues/1763).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="initial-scale 1, width=1200, height=600"`.

## History

- 2026-11-11: First version.
