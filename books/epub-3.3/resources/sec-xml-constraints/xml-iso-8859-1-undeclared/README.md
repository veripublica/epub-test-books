# A content document in ISO-8859-1 with no encoding declaration

- Book: `xml-iso-8859-1-undeclared.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-iso-8859-1-undeclared/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed; epubcheck: missed
- Asked for by: epubsana, to test its repair of these books (note of 2026-11-22)
- Issue: [#697](https://github.com/veripublica/epub-test-books/issues/697)
- Other clauses: XML 1.0 `charencoding`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document is encoded in ISO-8859-1, but nothing in it says so: its XML declaration has no encoding, it has no byte order mark, and it has no meta charset element. It holds the letter é, written as the single byte E9, which is not valid UTF-8. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A document with no byte order mark and no encoding declaration is read as UTF-8, and these bytes are not UTF-8.

## Question

The content document is encoded in ISO-8859-1 and has no encoding declaration, no byte order mark and no `meta charset`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

XML 1.0 (Fifth Edition), [4.3.3 Character Encoding in Entities](https://www.w3.org/TR/xml/#charencoding):

> In the absence of information provided by an external transport protocol (e.g. HTTP or MIME), it is a fatal error for an entity including an encoding declaration to be presented to the XML processor in an encoding other than that named in the declaration, or for an entity which begins with neither a Byte Order Mark nor an encoding declaration to use an encoding other than UTF-8.

## Expected result

Invalid. A document with no byte order mark and no encoding declaration is read as UTF-8, and these bytes are not UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i xml-iso-8859-1-undeclared.epub -u --advisory` | ERROR RSC-028; INVALID | `xml-iso-8859-1-undeclared.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-iso-8859-1-undeclared.epub -u` | no findings; VALID | `xml-iso-8859-1-undeclared.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1784](https://github.com/w3c/epubcheck/issues/1784).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` is written in ISO-8859-1. Its XML declaration is `<?xml version="1.0"?>`, with no encoding, and its `meta charset` is removed. It holds one non-ASCII character, é (`E9`), which is the same byte in windows-1252. The declared ISO-8859-1 set is `xml-iso-8859-1`.

## History

- 2026-11-22: First version.
