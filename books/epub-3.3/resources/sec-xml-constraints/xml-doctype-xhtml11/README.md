# An XHTML 1.1 document type

- Book: `xml-doctype-xhtml11.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-doctype-xhtml11/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#152](https://github.com/veripublica/epub-test-books/issues/152)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has the XHTML 1.1 public and system identifiers in its DOCTYPE. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The table lists no external identifiers for XHTML.

## Question

The content document has the XHTML 1.1 public and system identifiers in its `DOCTYPE`. Does a validator reject it?

## Clause

EPUB 3.3, [`app-identifiers-allowed`](https://www.w3.org/TR/epub-33/#app-identifiers-allowed):

> EPUB creators MAY use these external identifiers only in publication resources with the listed media types [rfc2046] specified in their manifest declarations.

## Expected result

Invalid. The table lists no external identifiers for XHTML.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i xml-doctype-xhtml11.epub -u --advisory` | ERROR HTM-004; INVALID | `xml-doctype-xhtml11.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-doctype-xhtml11.epub -u` | ERROR HTM-004; INVALID | `xml-doctype-xhtml11.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the `DOCTYPE` becomes the XHTML 1.1 one.

## History

- 2026-11-09: First version.
