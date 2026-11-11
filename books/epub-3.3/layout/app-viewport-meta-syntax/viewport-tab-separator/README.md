# A viewport with a tab after the comma (valid)

- Book: `viewport-tab-separator.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/app-viewport-meta-syntax/viewport-tab-separator/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The viewport of content.xhtml has a tab character (U+0009) after the comma, between width=1200, and height=600. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid. Whitespace normalization turns the tab into a space, and `, ` is a separator. The clause says any XML whitespace may be authored if the normalized result is valid.

## Question

The viewport of `content.xhtml` has a tab character (U+0009) after the comma: `width=1200,<tab>height=600`. Does a validator accept it?

## Clause

EPUB 3.3, [`app-viewport-meta-syntax`](https://www.w3.org/TR/epub-33/#app-viewport-meta-syntax):

> The authoring requirements in this section apply after whitespace normalization [xml] (i.e., after a reading system strips leading and trailing whitespace and compacts all instances of multiple whitespace within the attribute to single spaces). EPUB creators MAY include any whitespace characters [xml] in the authored tag so long as the result is valid to this definition.

> sep-char = ( ";" | "," | space ) ; assign = [ space ], "=", [ space ] ; space = #x20 ;

## Expected result

Valid. Whitespace normalization turns the tab into a space, and `, ` is a separator. The clause says any XML whitespace may be authored if the normalized result is valid.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i viewport-tab-separator.epub -u --advisory` | no findings; VALID | `viewport-tab-separator.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck viewport-tab-separator.epub -u` | no findings; VALID | `viewport-tab-separator.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), with the viewport in `content.xhtml` set to `width=1200,`, a literal tab character, and `height=600`. The tab is written as itself, not as a character reference: XML normalization turns a literal tab into a space but keeps a referenced one.

## History

- 2026-11-11: First version.
