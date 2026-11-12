# A viewport tag named " viewport ", with spaces (valid)

- Book: `viewport-name-padded.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-name-padded/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport tag of content.xhtml has name=" viewport ", with a space on each side of the name. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. Whitespace normalization, as the same section defines it, strips the leading and trailing spaces, and the result is `viewport`.

## Question

The viewport tag of `content.xhtml` has `name=" viewport "`, with a space on each side. Does a validator accept it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> The value of the name attribute [html] after whitespace normalization [xml] MUST be viewport.

> The authoring requirements in this section apply after whitespace normalization [xml] (i.e., after a reading system strips leading and trailing whitespace and compacts all instances of multiple whitespace within the attribute to single spaces). EPUB creators MAY include any whitespace characters [xml] in the authored tag so long as the result is valid to this definition.

## Expected result

Valid. Whitespace normalization, as the same section defines it, strips the leading and trailing spaces, and the result is `viewport`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i viewport-name-padded.epub -u --advisory` | no findings; VALID | `viewport-name-padded.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-name-padded.epub -u` | no findings; VALID | `viewport-name-padded.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport tag in `content.xhtml` named `" viewport "`, a space on each side.

## History

- 2026-11-12: First version.
