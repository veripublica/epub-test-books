# A `landmarks` nav (valid)

- Book: `landmarks.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-landmarks/landmarks/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#117](https://github.com/veripublica/epub-test-books/issues/117)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document has one landmarks nav. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. One is allowed.

## Question

The navigation document has one `landmarks` nav. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-landmarks`](https://www.w3.org/TR/epub-33/#sec-nav-landmarks):

> The landmarks nav element is OPTIONAL in EPUB navigation documents and MUST NOT occur more than once.

## Expected result

Valid. One is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i landmarks.epub -u --advisory` | no findings; VALID | `landmarks.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck landmarks.epub -u` | no findings; VALID | `landmarks.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `landmarks` nav is added.

## History

- 2026-11-09: First version.
