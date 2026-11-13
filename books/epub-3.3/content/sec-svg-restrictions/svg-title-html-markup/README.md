# HTML markup inside an SVG `title` (valid)

- Book: `svg-title-html-markup.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-restrictions/svg-title-html-markup/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#166](https://github.com/veripublica/epub-test-books/issues/166)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An inline SVG title holds an HTML span. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The markup is in the HTML namespace.

## Question

An inline SVG `title` holds an HTML `span`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-svg-restrictions`](https://www.w3.org/TR/epub-33/#sec-svg-restrictions):

> If the [svg] title element contains marked-up text, the markup MUST contain only elements declared in the HTML namespace [infra].

## Expected result

Valid. The markup is in the HTML namespace.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i svg-title-html-markup.epub -u --advisory` | no findings; VALID | `svg-title-html-markup.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-title-html-markup.epub -u` | no findings; VALID | `svg-title-html-markup.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, inline SVG whose `title` holds an HTML `span` is added, and the manifest item gets the `svg` property.

## History

- 2026-11-09: First version.
