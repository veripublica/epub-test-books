# A `nav` with no `epub:type` (valid)

- Book: `other-nav-no-type.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-types-other/other-nav-no-type/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#119](https://github.com/veripublica/epub-test-books/issues/119)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A nav with no epub:type uses ul. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The content model applies only to a nav that carries `epub:type`.

## Question

A `nav` with no `epub:type` uses `ul`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-nav-def-model`](https://www.w3.org/TR/epub-33/#sec-nav-def-model):

> When a nav element carries the epub:type attribute in an EPUB navigation document, this specification restricts the content model of the element and its descendants as follows:

## Expected result

Valid. The content model applies only to a nav that carries `epub:type`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i other-nav-no-type.epub -u --advisory` | no findings; VALID | `other-nav-no-type.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck other-nav-no-type.epub -u` | no findings; VALID | `other-nav-no-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `nav` with no `epub:type` and a `ul` is added.

## History

- 2026-11-09: First version.
