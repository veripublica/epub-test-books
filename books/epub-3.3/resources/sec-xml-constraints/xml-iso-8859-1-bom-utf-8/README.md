# A content document in ISO-8859-1 behind a UTF-8 byte order mark

- Book: `xml-iso-8859-1-bom-utf-8.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-iso-8859-1-bom-utf-8/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed; epubcheck: missed
- Asked for by: the maintainer, after veripublica/epubveri#150, whose fix also covers this case
- Issue: [#698](https://github.com/veripublica/epub-test-books/issues/698)
- Other clauses: XML 1.0 `charencoding`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document starts with the UTF-8 byte order mark (EF BB BF), which says the document is UTF-8. It has no encoding declaration and no meta charset element. Its bytes are ISO-8859-1: it holds the letter é as the single byte E9, which is not valid UTF-8. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The byte order mark makes the document UTF-8, and these bytes are not UTF-8.

## Question

The content document starts with the UTF-8 byte order mark and has no encoding declaration, but its bytes are ISO-8859-1. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

XML 1.0 (Fifth Edition), [4.3.3 Character Encoding in Entities](https://www.w3.org/TR/xml/#charencoding):

> Entities encoded in UTF-16 MUST and entities encoded in UTF-8 MAY begin with the Byte Order Mark described by Annex H of [ISO/IEC 10646:2000], section 16.8 of [Unicode] (the ZERO WIDTH NO-BREAK SPACE character, #xFEFF). This is an encoding signature, not part of either the markup or the character data of the XML document.

> It is a fatal error if an XML entity is determined (via default, encoding declaration, or higher-level protocol) to be in a certain encoding but contains byte sequences that are not legal in that encoding. Specifically, it is a fatal error if an entity encoded in UTF-8 contains any ill-formed code unit sequences, as defined in section 3.9 of Unicode [Unicode].

## Expected result

Invalid. The byte order mark makes the document UTF-8, and these bytes are not UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i xml-iso-8859-1-bom-utf-8.epub -u --advisory` | ERROR RSC-028; INVALID | `xml-iso-8859-1-bom-utf-8.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-iso-8859-1-bom-utf-8.epub -u` | no findings; VALID | `xml-iso-8859-1-bom-utf-8.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1784](https://github.com/w3c/epubcheck/issues/1784).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` starts with `EF BB BF`, then the template document written in ISO-8859-1. Its XML declaration is `<?xml version="1.0"?>`, with no encoding, and its `meta charset` is removed, so the byte order mark is the only thing that names an encoding. It holds one non-ASCII character, é (`E9`). The set with no byte order mark is `xml-iso-8859-1-undeclared`; the set that declares UTF-8 is `xml-iso-8859-1-declared-utf-8`.

## History

- 2026-11-22: First version.
