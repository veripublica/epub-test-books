# Two `landmarks` nav elements

- Book: `landmarks-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-landmarks/landmarks-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#108](https://github.com/veripublica/epub-test-books/issues/108)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document has two landmarks nav elements. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. One is the most allowed.

## Question

The navigation document has two `landmarks` nav elements. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-landmarks`](https://www.w3.org/TR/epub-33/#sec-nav-landmarks):

> The landmarks nav element is OPTIONAL in EPUB navigation documents and MUST NOT occur more than once.

## Expected result

Invalid. One is the most allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i landmarks-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `landmarks-twice.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck landmarks-twice.epub -u` | ERROR RSC-005; INVALID | `landmarks-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, two `landmarks` nav elements are added.

## History

- 2026-11-09: First version.
