# Inline SVG `foreignObject` without flow content

- Book: `foreignobject-no-flow.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/foreignobject-no-flow/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#163](https://github.com/veripublica/epub-test-books/issues/163)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Inline SVG has a foreignObject holding only an HTML title. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `title` is not flow content.

## Question

Inline SVG has a `foreignObject` holding only an HTML `title`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> MUST contain either [html] flow content or exactly one [html] body element.

## Expected result

Invalid. `title` is not flow content.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i foreignobject-no-flow.epub -u --advisory` | ERROR RSC-005; INVALID | `foreignobject-no-flow.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck foreignobject-no-flow.epub -u` | ERROR RSC-005; INVALID | `foreignobject-no-flow.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG with a `foreignObject` holding an HTML `title` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
