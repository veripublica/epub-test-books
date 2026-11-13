# A hidden `page-list` nav (valid)

- Book: `page-list-hidden.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-pagelist/page-list-hidden/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#116](https://github.com/veripublica/epub-test-books/issues/116)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The page-list nav has the hidden attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Attributes on these elements are not restricted.

## Question

The `page-list` nav has the `hidden` attribute. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> Note that there are no restrictions on the attributes allowed on these elements.

## Expected result

Valid. Attributes on these elements are not restricted.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i page-list-hidden.epub -u --advisory` | no findings; VALID | `page-list-hidden.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck page-list-hidden.epub -u` | no findings; VALID | `page-list-hidden.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `page-list` nav with `hidden="hidden"` is added.

## History

- 2026-11-09: First version.
