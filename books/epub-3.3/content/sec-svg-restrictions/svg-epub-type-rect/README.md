# `epub:type` on an SVG `rect` (valid)

- Book: `svg-epub-type-rect.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/svg-epub-type-rect/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#168](https://github.com/veripublica/epub-test-books/issues/168)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An inline SVG rect element has epub:type. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. `rect` is a renderable element.

## Question

An inline SVG `rect` element has `epub:type`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> When specified, the epub:type attribute MUST only be included on renderable elements [svg].

## Expected result

Valid. `rect` is a renderable element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i svg-epub-type-rect.epub -u --advisory` | no findings; VALID | `svg-epub-type-rect.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-epub-type-rect.epub -u` | no findings; VALID | `svg-epub-type-rect.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG with `epub:type` on `rect` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
