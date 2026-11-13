# A JPEG in the spine with a fallback (valid)

- Book: `core-in-spine-with-fallback.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-core-media-types/core-in-spine-with-fallback/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#123](https://github.com/veripublica/epub-test-books/issues/123)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A JPEG image is in the spine, and its manifest fallback is an XHTML document. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The fallback the clause asks for is there.

## Question

A JPEG image is in the spine, and its manifest fallback is an XHTML document. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-core-media-types`](https://www.w3.org/TR/epub-33/#sec-core-media-types):

> With the exception of XHTML content documents and SVG content documents, EPUB creators MUST provide manifest fallbacks for core media type resources referenced directly from the spine.

## Expected result

Valid. The fallback the clause asks for is there.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i core-in-spine-with-fallback.epub -u --advisory` | USAGE OPF-097; VALID | `core-in-spine-with-fallback.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck core-in-spine-with-fallback.epub -u` | USAGE OPF-097; VALID | `core-in-spine-with-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated JPEG and `OEBPS/extra.xhtml` are added to the manifest, the JPEG's `fallback` names the document, and the JPEG is added to the end of the spine.

## History

- 2026-11-09: First version.
