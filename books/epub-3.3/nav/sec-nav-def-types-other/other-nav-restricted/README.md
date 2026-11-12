# A typed `nav` using `ul`

- Book: `other-nav-restricted.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/nav/sec-nav-def-types-other/other-nav-restricted/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the navigation document section
- Issue: [#111](https://github.com/veripublica/epub-test-books/issues/111)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A nav with epub:type="lot" uses ul in place of ol. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A nav with `epub:type` follows the content model, which requires an `ol`.

## Question

A `nav` with `epub:type="lot"` uses `ul` in place of `ol`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-nav-def-types-other`](https://www.w3.org/TR/epub-33/#sec-nav-def-types-other):

> If these nav elements are intended for reading system processing, they MUST have an epub:type attribute and are subject to the content model restrictions defined in 7.3 The nav element: restrictions.

## Expected result

Invalid. A nav with `epub:type` follows the content model, which requires an `ol`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i other-nav-restricted.epub -u --advisory` | ERROR RSC-005; INVALID | `other-nav-restricted.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck other-nav-restricted.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `other-nav-restricted.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/nav.xhtml`, a `nav` with `epub:type="lot"` and a `ul` is added.

## History

- 2026-11-09: First version.
