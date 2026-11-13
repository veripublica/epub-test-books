# Two `body` elements in a standalone SVG `foreignObject`

- Book: `standalone-foreignobject-two-bodies.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/standalone-foreignobject-two-bodies/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#165](https://github.com/veripublica/epub-test-books/issues/165)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An SVG content document has a foreignObject holding two body elements. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one `body` is allowed.

## Question

An SVG content document has a `foreignObject` holding two `body` elements. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> MUST contain either [html] flow content or exactly one [html] body element.

## Expected result

Invalid. Exactly one `body` is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i standalone-foreignobject-two-bodies.epub -u --advisory` | ERROR RSC-005; INVALID | `standalone-foreignobject-two-bodies.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck standalone-foreignobject-two-bodies.epub -u` | ERROR RSC-005; INVALID | `standalone-foreignobject-two-bodies.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is added to the manifest and the end of the spine, with a `foreignObject` holding two `body` elements.

## History

- 2026-11-09: First version.
