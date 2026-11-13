# A navigation heading after the list

- Book: `heading-after-ol.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/heading-after-ol/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#221](https://github.com/veripublica/epub-test-books/issues/221)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The heading of the toc nav comes after its ol. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The heading must come first.

## Question

The heading of the `toc` nav comes after its `ol`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> nav In this order: h1-h6 [0 or 1] ol [exactly 1]

## Expected result

Invalid. The heading must come first.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i heading-after-ol.epub -u --advisory` | ERROR RSC-005; INVALID | `heading-after-ol.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck heading-after-ol.epub -u` | ERROR RSC-005; INVALID | `heading-after-ol.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the `h1` is moved after the `ol`.

## History

- 2026-11-09: First version.
