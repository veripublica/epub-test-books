# A file name not encoded as UTF-8

- Book: `filename-not-utf8.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/filename-not-utf8/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#26](https://github.com/veripublica/epub-test-books/issues/26)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document is named with the byte 0x81, which is u with diaeresis in CP437, the old ZIP default encoding, and its UTF-8 flag (bit 11) is clear. The package document refers to it by its UTF-8 name. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The name is not UTF-8: the byte 0x81 cannot start a UTF-8 character.

## Question

The content document's name holds the byte 0x81 (u with diaeresis in CP437, the old ZIP default), and the entry's UTF-8 flag is clear. Does a validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> OCF ZIP containers MUST encode file system names using UTF-8 [unicode].

## Expected result

Invalid. The name is not UTF-8: the byte 0x81 cannot start a UTF-8 character.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i filename-not-utf8.epub -u --advisory` | FATAL PKG-027; INVALID | `filename-not-utf8.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck filename-not-utf8.epub -u` | FATAL PKG-027; INVALID | `filename-not-utf8.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The content document's ZIP name is the bytes `OEBPS/c\x81ntent.xhtml` with general purpose bit 11 clear; the manifest and navigation document use `c%C3%BCntent.xhtml`.

## History

- 2026-11-08: First version.
