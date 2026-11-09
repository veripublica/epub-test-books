# A `p` used as the navigation heading

- Book: `heading-p.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/heading-p/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#104](https://github.com/veripublica/epub-test-books/issues/104)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The toc nav starts with a p in place of a heading. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only a heading or the `ol` may come first.

## Question

The `toc` nav starts with a `p` in place of a heading. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> nav In this order: h1-h6 [0 or 1] ol [exactly 1]

## Expected result

Invalid. Only a heading or the `ol` may come first.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i heading-p.epub -u --advisory` | ERROR RSC-005; INVALID | `heading-p.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck heading-p.epub -u` | ERROR RSC-005; INVALID | `heading-p.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the `h1` becomes a `p`.

## History

- 2026-11-09: First version.
