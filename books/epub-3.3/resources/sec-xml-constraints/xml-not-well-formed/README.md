# A content document that is not well-formed

- Book: `xml-not-well-formed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-not-well-formed/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#150](https://github.com/veripublica/epub-test-books/issues/150)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has an unclosed p element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The document is not well-formed XML.

## Question

The content document has an unclosed `p` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be a conformant XML 1.0 Document as defined in Conformance of Documents [xml-names].

## Expected result

Invalid. The document is not well-formed XML.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i xml-not-well-formed.epub -u --advisory` | FATAL RSC-016; INVALID | `xml-not-well-formed.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-not-well-formed.epub -u` | FATAL RSC-016; INVALID | `xml-not-well-formed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `p` element is left unclosed.

## History

- 2026-11-09: First version.
