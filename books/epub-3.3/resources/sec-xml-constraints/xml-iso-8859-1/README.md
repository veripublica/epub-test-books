# A content document in ISO-8859-1

- Book: `xml-iso-8859-1.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-iso-8859-1/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#146](https://github.com/veripublica/epub-test-books/issues/146)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document is encoded in ISO-8859-1 and says so in its XML declaration. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only UTF-8 and UTF-16 are allowed.

## Question

The content document is encoded in ISO-8859-1 and says so in its XML declaration. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. Only UTF-8 and UTF-16 are allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i xml-iso-8859-1.epub -u --advisory` | ERROR RSC-028; INVALID | `xml-iso-8859-1.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-iso-8859-1.epub -u` | ERROR RSC-028; INVALID | `xml-iso-8859-1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` is written in ISO-8859-1, its XML declaration says so, and its `meta charset` is removed. It holds one non-ASCII character.

## History

- 2026-11-09: First version.
