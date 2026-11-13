# An `img` with no `alt`

- Book: `html-img-no-alt.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-img-no-alt/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to start the content documents section; parked on 2026-11-09 until #27's comments had their time, built on 2026-11-13 for the release after 15 November
- Issue: [#610](https://github.com/veripublica/epub-test-books/issues/610)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img element has no alt attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. HTML requires the `alt` attribute here.

## Question

An `img` element has no `alt` attribute and meets none of the exceptions in HTML. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

## Expected result

Invalid. HTML requires the `alt` attribute here.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i html-img-no-alt.epub -u --advisory` | ERROR RSC-005; INVALID | `html-img-no-alt.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck html-img-no-alt.epub -u` | no findings; VALID | `html-img-no-alt.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1760](https://github.com/w3c/epubcheck/issues/1760).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated JPEG is added to the manifest, and `content.xhtml` shows it with no `alt`. The accessibility metadata says the book has an image.

## History

- 2026-11-09: First version, parked.
- 2026-11-13: Measured on epubveri 0.42.0 and added to the library.
