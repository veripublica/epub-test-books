# Two `ol` elements in the `toc` nav

- Book: `nav-two-ol.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/nav-two-ol/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#220](https://github.com/veripublica/epub-test-books/issues/220)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav has two ol elements. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one `ol` is allowed.

## Question

The `toc` nav has two `ol` elements. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> nav In this order: h1-h6 [0 or 1] ol [exactly 1]

## Expected result

Invalid. Exactly one `ol` is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i nav-two-ol.epub -u --advisory` | ERROR RSC-005; INVALID | `nav-two-ol.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck nav-two-ol.epub -u` | ERROR RSC-005; INVALID | `nav-two-ol.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a second `ol` is added to the `toc` nav.

## History

- 2026-11-09: First version.
