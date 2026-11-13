# An `svg` element inside an SVG `title`

- Book: `svg-title-nested-svg.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/svg-title-nested-svg/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri, after the navigation and content document sets
- Issue: [#228](https://github.com/veripublica/epub-test-books/issues/228)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An inline SVG title holds an svg element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The markup must be in the HTML namespace, and `svg` is not.

## Question

An inline SVG `title` holds an `svg` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> If the [svg] title element contains marked-up text, the markup MUST contain only elements declared in the HTML namespace [infra].

## Expected result

Invalid. The markup must be in the HTML namespace, and `svg` is not.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-title-nested-svg.epub -u --advisory` | ERROR RSC-005; INVALID | `svg-title-nested-svg.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-title-nested-svg.epub -u` | no findings; VALID | `svg-title-nested-svg.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: epubcheck gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1759](https://github.com/w3c/epubcheck/issues/1759).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG whose `title` holds an `svg` element is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
