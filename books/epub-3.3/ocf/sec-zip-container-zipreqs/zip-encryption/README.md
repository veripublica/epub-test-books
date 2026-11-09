# A content document encrypted with ZIP encryption

- Book: `zip-encryption.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/zip-encryption/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#31](https://github.com/veripublica/epub-test-books/issues/31)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document, OEBPS/content.xhtml, is encrypted with the ZIP format's traditional encryption, and bit 0 of its general purpose flag is set. The password is epub-test-books. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An OCF ZIP container must not use ZIP encryption; encryption belongs in encryption.xml.

## Question

`OEBPS/content.xhtml` is encrypted with the ZIP format's own (traditional PKWARE) encryption. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> OCF ZIP containers MUST NOT use the encryption features defined by the ZIP format; instead, encryption MUST be done using the features described in 4.2.6.3.2 Encryption file (encryption.xml).

## Expected result

Invalid. An OCF ZIP container must not use ZIP encryption; encryption belongs in encryption.xml.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i zip-encryption.epub -u --advisory` | FATAL PKG-027; INVALID | `zip-encryption.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck zip-encryption.epub -u` | FATAL PKG-027; INVALID | `zip-encryption.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

epubcheck's message guesses at the cause ("probably due to file names not encoded in UTF-8"), but the names here are plain ASCII. epubveri's message names the encrypted entry.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is deflated, then encrypted with traditional PKWARE encryption (APPNOTE 6.1) by `scripts/lib/rawzip.py`. The password is `epub-test-books`. The 12-byte encryption header is fixed, so the build is reproducible: 11 zero bytes, then the CRC check byte. Bit 0 of the general purpose flag is set in the local and central headers.

## History

- 2026-11-08: First version.
