# A content document in ISO-8859-1 that declares UTF-8

- Book: `xml-iso-8859-1-declared-utf-8.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-iso-8859-1-declared-utf-8/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, after veripublica/epubveri#150, whose fix also covers this case
- Issue: [#699](https://github.com/veripublica/epub-test-books/issues/699)
- Other clauses: XML 1.0 `charencoding`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document says it is UTF-8, in its XML declaration and in its meta charset element, but its bytes are ISO-8859-1: it holds the letter é as the single byte E9, which is not valid UTF-8. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The document declares UTF-8, and these bytes are not UTF-8.

## Question

The content document declares UTF-8 in its XML declaration and its `meta charset`, but its bytes are ISO-8859-1. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

XML 1.0 (Fifth Edition), [4.3.3 Character Encoding in Entities](https://www.w3.org/TR/xml/#charencoding):

> It is a fatal error if an XML entity is determined (via default, encoding declaration, or higher-level protocol) to be in a certain encoding but contains byte sequences that are not legal in that encoding. Specifically, it is a fatal error if an entity encoded in UTF-8 contains any ill-formed code unit sequences, as defined in section 3.9 of Unicode [Unicode].

## Expected result

Invalid. The document declares UTF-8, and these bytes are not UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i xml-iso-8859-1-declared-utf-8.epub -u --advisory` | ERROR RSC-028; INVALID | `xml-iso-8859-1-declared-utf-8.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-iso-8859-1-declared-utf-8.epub -u` | no findings; VALID | `xml-iso-8859-1-declared-utf-8.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1784](https://github.com/w3c/epubcheck/issues/1784).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` is the template document, with its `encoding="UTF-8"` declaration and `meta charset="UTF-8"` unchanged, written in ISO-8859-1 instead of UTF-8. It holds one non-ASCII character, é (`E9`). The set with no declaration is `xml-iso-8859-1-undeclared`; the set with a byte order mark is `xml-iso-8859-1-bom-utf-8`.

## History

- 2026-11-22: First version.
