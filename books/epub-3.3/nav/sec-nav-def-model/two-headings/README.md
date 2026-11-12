# Two headings in the `toc` nav

- Book: `two-headings.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/two-headings/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#103](https://github.com/veripublica/epub-test-books/issues/103)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav has two headings. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. One heading is the most allowed.

## Question

The `toc` nav has two headings. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> nav In this order: h1-h6 [0 or 1] ol [exactly 1]

## Expected result

Invalid. One heading is the most allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i two-headings.epub -u --advisory` | ERROR RSC-005; INVALID | `two-headings.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck two-headings.epub -u` | ERROR RSC-005; INVALID | `two-headings.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, an `h2` is added after the `h1`.

## History

- 2026-11-09: First version.
