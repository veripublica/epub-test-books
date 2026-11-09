# A `body` in inline SVG `foreignObject`

- Book: `foreignobject-body-inline.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/foreignobject-body-inline/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#162](https://github.com/veripublica/epub-test-books/issues/162)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Inline SVG has a foreignObject holding a body. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `body` is not permitted in SVG embedded by inclusion.

## Question

Inline SVG has a `foreignObject` holding a `body`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> In the case of SVGs embedded by inclusion, a body element is not permitted per the restrictions on SVG defined in [html].

## Expected result

Invalid. `body` is not permitted in SVG embedded by inclusion.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i foreignobject-body-inline.epub -u --advisory` | ERROR RSC-005; INVALID | `foreignobject-body-inline.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck foreignobject-body-inline.epub -u` | ERROR RSC-005; INVALID | `foreignobject-body-inline.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG with a `foreignObject` holding a `body` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
