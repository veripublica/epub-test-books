# `epub:type` on an SVG `defs`

- Book: `svg-epub-type-defs.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/svg-epub-type-defs/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#167](https://github.com/veripublica/epub-test-books/issues/167)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An inline SVG defs element has epub:type. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `defs` is not a renderable element.

## Question

An inline SVG `defs` element has `epub:type`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> When specified, the epub:type attribute MUST only be included on renderable elements [svg].

## Expected result

Invalid. `defs` is not a renderable element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i svg-epub-type-defs.epub -u --advisory` | ERROR RSC-005; INVALID | `svg-epub-type-defs.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-epub-type-defs.epub -u` | ERROR RSC-005; INVALID | `svg-epub-type-defs.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG with `epub:type` on `defs` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
