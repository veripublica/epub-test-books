# An XInclude element

- Book: `xml-xinclude.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-xinclude/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#149](https://github.com/veripublica/epub-test-books/issues/149)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has an xi:include element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. XInclude is not allowed. A schema error for the unknown element would follow from the same defect.

## Question

The content document has an `xi:include` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST NOT make use of XInclude [xinclude].

## Expected result

Invalid. XInclude is not allowed. A schema error for the unknown element would follow from the same defect.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i xml-xinclude.epub -u --advisory` | ERROR RSC-005; INVALID | `xml-xinclude.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-xinclude.epub -u` | ERROR RSC-005; INVALID | `xml-xinclude.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `xi:include` element naming `about.xhtml` is added.

## History

- 2026-11-09: First version.
