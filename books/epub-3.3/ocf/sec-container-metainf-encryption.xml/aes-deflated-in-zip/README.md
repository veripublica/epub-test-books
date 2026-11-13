# An encrypted file Deflate-compressed in the ZIP (valid)

- Book: `aes-deflated-in-zip.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-deflated-in-zip/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#524](https://github.com/veripublica/epub-test-books/issues/524)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is encrypted with AES-128-CBC, and META-INF/encryption.xml describes it: an EncryptedKey (an RSA-wrapped key) and an EncryptedData that refers to it, as in EPUB 3.3's example of an encrypted image. Its ZIP entry is Deflate-compressed rather than stored. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Storing encrypted files is only a SHOULD, and Deflate is an allowed ZIP method. A warning would fit.

## Question

The encrypted `OEBPS/content.xhtml` is Deflate-compressed in the ZIP instead of stored. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> Within the ZIP directory, EPUB creators SHOULD store encrypted files rather than Deflate-compress them.

## Expected result

Valid. Storing encrypted files is only a SHOULD, and Deflate is an allowed ZIP method. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i aes-deflated-in-zip.epub -u --advisory` | INFO RSC-004; VALID | `aes-deflated-in-zip.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-deflated-in-zip.epub -u` | INFO RSC-004; VALID | `aes-deflated-in-zip.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report INFO RSC-004: the encrypted document is not checked. Neither warns that the encrypted entry is Deflate-compressed, so the broken SHOULD goes unreported. That does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is replaced by its AES-128-CBC encryption (`scripts/lib/miniaes.py`): a 16-byte IV, then the ciphertext, padded as XML Encryption asks. The key and IV are fixed (`scripts/lib/ocfvariants.py`, `AES_KEY` and `AES_IV`), so the book is reproducible. `META-INF/encryption.xml` is added after `META-INF/container.xml`. It has an `EncryptedKey` (`Id="EK"`, `rsa-1_5`, `KeyName` `epub-test-books`, 128 fixed bytes as its `CipherValue`) and an `EncryptedData` with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"`, a `RetrievalMethod` to `#EK`, and `CipherReference URI="OEBPS/content.xhtml"`. The ZIP entry uses method 8 (Deflate).

## History

- 2026-11-13: First version.
