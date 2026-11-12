# An `hgroup` as a navigation heading

- Book: `nav-hgroup-heading.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/nav-hgroup-heading/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri, after the navigation and content document sets
- Issue: [#229](https://github.com/veripublica/epub-test-books/issues/229)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The heading of the toc nav is an hgroup holding an h1. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The heading must be an `h1` to `h6` element, and `hgroup` is not one.

## Question

The heading of the `toc` nav is an `hgroup` holding an `h1`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> nav In this order: h1-h6 [0 or 1] ol [exactly 1]

## Expected result

Invalid. The heading must be an `h1` to `h6` element, and `hgroup` is not one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i nav-hgroup-heading.epub -u --advisory` | ERROR RSC-005; INVALID | `nav-hgroup-heading.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck nav-hgroup-heading.epub -u` | no findings; VALID | `nav-hgroup-heading.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: epubcheck gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1758](https://github.com/w3c/epubcheck/issues/1758).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the `h1` is wrapped in an `hgroup`.

## History

- 2026-11-09: First version.
