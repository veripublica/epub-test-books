# A content document in windows-1252

- Book: `xml-windows-1252.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-xml-constraints/xml-windows-1252/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubsana, to test its repair of these books (note of 2026-11-22)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document is encoded in windows-1252 and says so in its XML declaration. It holds curly quotation marks and the letter é, which windows-1252 writes as the bytes 93, 94 and E9. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only UTF-8 and UTF-16 are allowed.

## Question

The content document is encoded in windows-1252 and says so in its XML declaration. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be encoded in UTF-8 or UTF-16 [unicode], with UTF-8 as the RECOMMENDED encoding.

## Expected result

Invalid. Only UTF-8 and UTF-16 are allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i xml-windows-1252.epub -u --advisory` | ERROR RSC-028; INVALID | `xml-windows-1252.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-windows-1252.epub -u` | ERROR RSC-028; INVALID | `xml-windows-1252.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` is written in windows-1252, its XML declaration says `encoding="windows-1252"`, and its `meta charset` is removed. It holds “Café”: the bytes `93`, `E9` and `94` are its three non-ASCII characters. In ISO-8859-1, `93` and `94` are C1 control characters, so reading the bytes as ISO-8859-1 gives different text. The ISO-8859-1 set is `xml-iso-8859-1`.

## History

- 2026-11-22: First version.
