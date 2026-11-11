# A viewport value that holds an equals sign

- Book: `viewport-value-with-equals.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-value-with-equals/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after the fixed-layout sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml is width=1200=1, height=600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. The value of `width` holds the assignment character `=`.

## Question

The viewport of `content.xhtml` is `width=1200=1, height=600`. Does a validator reject it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> viewport = property, { sep, property } ; property = name, [ assign, value ] ; name = ? character data ? ; value = ? character data ? ; sep = sep-char, { sep-char } ; sep-char = ( ";" | "," | space ) ; assign = [ space ], "=", [ space ] ; space = #x20 ;

> The only restriction on property names and values is that they MUST NOT contain separator characters or the assignment character.

## Expected result

Invalid. The value of `width` holds the assignment character `=`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-value-with-equals.epub -u --advisory` | ERROR HTM_057; INVALID | `viewport-value-with-equals.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-value-with-equals.epub -u` | ERROR HTM-047; INVALID | `viewport-value-with-equals.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `content="width=1200=1, height=600"`.

## History

- 2026-11-11: First version.
