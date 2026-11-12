# A JPEG as a data URL in `img` (valid)

- Book: `data-url-img-core.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-data-urls/data-url-img-core/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#141](https://github.com/veripublica/epub-test-books/issues/141)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img element has a data URL holding a JPEG. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The data URL holds a core media type.

## Question

An `img` element has a data URL holding a JPEG. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-data-urls`](https://www.w3.org/TR/epub-33/#sec-data-urls):

> EPUB creators MUST therefore encode data URLs as core media type resources or provide a fallback using the intrinsic fallback mechanisms of the host format.

## Expected result

Valid. The data URL holds a core media type.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i data-url-img-core.epub -u --advisory` | no findings; VALID | `data-url-img-core.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck data-url-img-core.epub -u` | no findings; VALID | `data-url-img-core.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `img` has a data URL holding a generated JPEG.

## History

- 2026-11-09: First version.
