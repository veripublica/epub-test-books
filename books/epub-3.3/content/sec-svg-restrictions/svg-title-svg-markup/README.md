# SVG markup inside an SVG `title`

- Book: `svg-title-svg-markup.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/svg-title-svg-markup/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#223](https://github.com/veripublica/epub-test-books/issues/223)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An inline SVG title holds an SVG rect. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The markup must be in the HTML namespace.

## Question

An inline SVG `title` holds an SVG `rect`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> If the [svg] title element contains marked-up text, the markup MUST contain only elements declared in the HTML namespace [infra].

## Expected result

Invalid. The markup must be in the HTML namespace.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-title-svg-markup.epub -u --advisory` | ERROR RSC-005; INVALID | `svg-title-svg-markup.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-title-svg-markup.epub -u` | ERROR RSC-005; INVALID | `svg-title-svg-markup.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG whose `title` holds a `rect` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
