# An empty `ol` in the `toc` nav

- Book: `ol-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/ol-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#102](https://github.com/veripublica/epub-test-books/issues/102)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The ol in the toc nav has no li. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. One or more `li` elements are required.

## Question

The `ol` in the `toc` nav has no `li`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> ol In this order: li [1 or more]

## Expected result

Invalid. One or more `li` elements are required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i ol-empty.epub -u --advisory` | ERROR RSC-005; INVALID | `ol-empty.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck ol-empty.epub -u` | ERROR RSC-005; INVALID | `ol-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, every entry is removed from the `ol`.

## History

- 2026-11-09: First version.
