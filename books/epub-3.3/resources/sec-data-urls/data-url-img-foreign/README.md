# A BMP as a data URL in `img`

- Book: `data-url-img-foreign.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-data-urls/data-url-img-foreign/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#142](https://github.com/veripublica/epub-test-books/issues/142)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img element has a data URL holding a BMP and has no fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The data URL holds a foreign type with no fallback.

## Question

An `img` element has a data URL holding a BMP and has no fallback. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-data-urls`](https://www.w3.org/TR/epub-33/#sec-data-urls):

> EPUB creators MUST therefore encode data URLs as core media type resources or provide a fallback using the intrinsic fallback mechanisms of the host format.

## Expected result

Invalid. The data URL holds a foreign type with no fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i data-url-img-foreign.epub -u --advisory` | ERROR RSC-032; INVALID | `data-url-img-foreign.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck data-url-img-foreign.epub -u` | ERROR RSC-032; INVALID | `data-url-img-foreign.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `img` has a data URL holding a generated BMP.

## History

- 2026-11-09: First version.
