# Inline SVG `foreignObject` with flow content (valid)

- Book: `foreignobject-flow.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/foreignobject-flow/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#161](https://github.com/veripublica/epub-test-books/issues/161)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Inline SVG has a foreignObject holding a p. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The element holds flow content.

## Question

Inline SVG has a `foreignObject` holding a `p`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> MUST contain either [html] flow content or exactly one [html] body element.

## Expected result

Valid. The element holds flow content.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i foreignobject-flow.epub -u --advisory` | no findings; VALID | `foreignobject-flow.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck foreignobject-flow.epub -u` | no findings; VALID | `foreignobject-flow.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG with a `foreignObject` holding a `p` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
