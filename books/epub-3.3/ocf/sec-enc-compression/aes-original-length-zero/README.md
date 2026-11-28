# A Compression element with OriginalLength="0"

- Book: `aes-original-length-zero.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-enc-compression/aes-original-length-zero/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to complete the OCF section; parked on 2026-11-13 while both verifiers missed it, built on 2026-11-20
- Issue: [#679](https://github.com/veripublica/epub-test-books/issues/679)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is compressed with Deflate, then encrypted with AES-128-CBC. META-INF/encryption.xml describes it, and its EncryptionProperties give a Compression element with Method 8 and OriginalLength 0. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. OriginalLength must be a positive integer, and 0 is not one.

## Question

`OEBPS/content.xhtml` is Deflate-compressed, then encrypted, and its Compression property in `META-INF/encryption.xml` gives `OriginalLength="0"`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-enc-compression`](https://www.w3.org/TR/epub-33/#sec-enc-compression) (the `Compression` element):

> OriginalLength [required] Represents the size of the initial resource (number of bytes). Value is a positive integer.

## Expected result

Invalid. `OriginalLength` must be a positive integer, and 0 is not one. It is also not the size of the initial resource, which is the template's whole `content.xhtml`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i aes-original-length-zero.epub -u --advisory` | ERROR RSC-005, INFO RSC-004; INVALID | `aes-original-length-zero.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-original-length-zero.epub -u` | INFO RSC-004; VALID | `aes-original-length-zero.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result: it reports the zero `OriginalLength` in `META-INF/encryption.xml` (RSC-005). epubcheck does not: it gives only INFO RSC-004.

- **epubcheck: missed.** [w3c/epubcheck#1782](https://github.com/w3c/epubcheck/issues/1782).

Both report INFO RSC-004: the encrypted document is not checked. The error is in `META-INF/encryption.xml`, which is not encrypted.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

As in `aes-compressed-first`: `OEBPS/content.xhtml` is compressed with raw Deflate, then replaced by the AES-128-CBC encryption of that (`scripts/lib/miniaes.py`), with the fixed key and IV of `scripts/lib/ocfvariants.py`. `META-INF/encryption.xml` is added after `META-INF/container.xml`, with the same `EncryptedKey` and `EncryptedData`. The one difference is the Compression element: `<c:Compression Method="8" OriginalLength="0"/>`. The ZIP entry is stored.

## History

- 2026-11-20: First version.
