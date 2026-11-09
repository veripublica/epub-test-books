# A navigation list item with two links

- Book: `li-two-links.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-model/li-two-links/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#219](https://github.com/veripublica/epub-test-books/issues/219)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A list item in the toc nav holds two a elements. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one `a` or `span` is allowed.

## Question

A list item in the `toc` nav holds two `a` elements. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> li In this order: (span or a) [exactly 1] ol [conditionally required]

## Expected result

Invalid. Exactly one `a` or `span` is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i li-two-links.epub -u --advisory` | ERROR RSC-005; INVALID | `li-two-links.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck li-two-links.epub -u` | ERROR RSC-005; INVALID | `li-two-links.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, the content document's list item gets a second `a`.

## History

- 2026-11-09: First version.
