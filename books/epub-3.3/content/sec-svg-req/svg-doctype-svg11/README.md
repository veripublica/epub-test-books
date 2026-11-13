# An SVG content document with the SVG 1.1 doctype (valid)

- Book: `svg-doctype-svg11.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-req/svg-doctype-svg11/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#589](https://github.com/veripublica/epub-test-books/issues/589)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/picture.svg has the SVG 1.1 document type declaration, with its public and system identifiers. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Those are the identifiers EPUB 3.3 allows for image/svg+xml.

## Question

`picture.svg`, in the spine, has the SVG 1.1 doctype. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MAY only specify a document type declaration that references an external identifier appropriate for its media type — as defined in B. Allowed external identifiers — or that omits external identifiers [xml].

EPUB 3.3, [`app-identifiers-allowed`](https://www.w3.org/TR/epub-33/#app-identifiers-allowed), the row for SVG:

> | image/svg+xml | -//W3C//DTD SVG 1.1//EN | http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd |

## Expected result

Valid. Those are the identifiers EPUB 3.3 allows for image/svg+xml.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-doctype-svg11.epub -u --advisory` | no findings; VALID | `svg-doctype-svg11.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-doctype-svg11.epub -u` | no findings; VALID | `svg-doctype-svg11.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is in the manifest as `image/svg+xml` and last in the spine. It holds the same picture as `svg-document`, after `<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">`.

## History

- 2026-11-13: First version.
