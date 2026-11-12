# A `page-list` nav (valid)

- Book: `page-list.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-pagelist/page-list/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#115](https://github.com/veripublica/epub-test-books/issues/115)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document has one page-list nav. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. One is allowed.

## Question

The navigation document has one `page-list` nav. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-pagelist`](https://www.w3.org/TR/epub-33/#sec-nav-pagelist):

> The page-list nav element is OPTIONAL in EPUB navigation documents and MUST NOT occur more than once.

## Expected result

Valid. One is allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i page-list.epub -u --advisory` | no findings; VALID | `page-list.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck page-list.epub -u` | no findings; VALID | `page-list.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `page-list` nav is added.

## History

- 2026-11-09: First version.
