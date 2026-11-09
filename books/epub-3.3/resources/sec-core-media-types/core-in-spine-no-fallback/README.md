# A JPEG in the spine with no fallback

- Book: `core-in-spine-no-fallback.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-core-media-types/core-in-spine-no-fallback/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#122](https://github.com/veripublica/epub-test-books/issues/122)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A JPEG image is in the spine and has no manifest fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A core media type resource in the spine needs a manifest fallback unless it is XHTML or SVG.

## Question

A JPEG image is in the spine and has no manifest fallback. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-core-media-types`](https://www.w3.org/TR/epub-33/#sec-core-media-types):

> With the exception of XHTML content documents and SVG content documents, EPUB creators MUST provide manifest fallbacks for core media type resources referenced directly from the spine.

## Expected result

Invalid. A core media type resource in the spine needs a manifest fallback unless it is XHTML or SVG.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i core-in-spine-no-fallback.epub -u --advisory` | ERROR OPF-043; INVALID | `core-in-spine-no-fallback.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck core-in-spine-no-fallback.epub -u` | ERROR OPF-043; INVALID | `core-in-spine-no-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated JPEG is added to the manifest and to the end of the spine.

## History

- 2026-11-09: First version.
