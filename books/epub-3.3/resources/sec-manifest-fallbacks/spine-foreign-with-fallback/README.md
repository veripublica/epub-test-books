# A foreign spine item with a content document fallback (valid)

- Book: `spine-foreign-with-fallback.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-manifest-fallbacks/spine-foreign-with-fallback/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#132](https://github.com/veripublica/epub-test-books/issues/132)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A BMP in the spine has an XHTML document as its manifest fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The chain holds an EPUB content document.

## Question

A BMP in the spine has an XHTML document as its manifest fallback. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-manifest-fallbacks`](https://www.w3.org/TR/epub-33/#sec-manifest-fallbacks):

> EPUB creators MUST specify a fallback chain for a foreign content document to ensure that reading systems can always render the spine item. In this case, the chain MUST contain at least one EPUB content document.

## Expected result

Valid. The chain holds an EPUB content document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i spine-foreign-with-fallback.epub -u --advisory` | USAGE OPF-097; VALID | `spine-foreign-with-fallback.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-foreign-with-fallback.epub -u` | USAGE OPF-097; VALID | `spine-foreign-with-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and `OEBPS/extra.xhtml` are added, the BMP's `fallback` names the document, and the BMP is added to the end of the spine.

## History

- 2026-11-09: First version.
