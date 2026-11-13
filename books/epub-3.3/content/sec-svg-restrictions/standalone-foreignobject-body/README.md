# A `body` in a standalone SVG `foreignObject` (valid)

- Book: `standalone-foreignobject-body.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/standalone-foreignobject-body/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#164](https://github.com/veripublica/epub-test-books/issues/164)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An SVG content document has a foreignObject holding one body. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The restriction on `body` is only for SVG embedded by inclusion.

## Question

An SVG content document has a `foreignObject` holding one `body`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> MUST contain either [html] flow content or exactly one [html] body element.

## Expected result

Valid. The restriction on `body` is only for SVG embedded by inclusion.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i standalone-foreignobject-body.epub -u --advisory` | no findings; VALID | `standalone-foreignobject-body.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck standalone-foreignobject-body.epub -u` | no findings; VALID | `standalone-foreignobject-body.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is added to the manifest and the end of the spine, with a `foreignObject` holding a `body`.

## History

- 2026-11-09: First version.
