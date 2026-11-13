# A BMP in `img` with no fallback

- Book: `foreign-img-no-fallback.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-foreign-resources/foreign-img-no-fallback/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#124](https://github.com/veripublica/epub-test-books/issues/124)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img element shows a BMP image, a foreign resource, and it has no manifest fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A foreign resource in `img` needs a manifest fallback.

## Question

An `img` element shows a BMP image, which is a foreign resource, and it has no manifest fallback. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fallbacks-img`](https://www.w3.org/TR/epub-33/#sec-fallbacks-img):

> Otherwise, it MAY reference foreign resources in its src and srcset attributes provided EPUB creators define a manifest fallback.

## Expected result

Invalid. A foreign resource in `img` needs a manifest fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i foreign-img-no-fallback.epub -u --advisory` | ERROR RSC-032; INVALID | `foreign-img-no-fallback.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck foreign-img-no-fallback.epub -u` | ERROR RSC-032; INVALID | `foreign-img-no-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP is added to the manifest and shown in `content.xhtml`.

## History

- 2026-11-09: First version.
