# A content document encrypted with AES-128-CBC (valid)

- Book: `aes-encrypted-content.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-encrypted-content/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#525](https://github.com/veripublica/epub-test-books/issues/525)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is encrypted with AES-128-CBC, and META-INF/encryption.xml describes it: an EncryptedKey (an RSA-wrapped key) and an EncryptedData that refers to it, as in EPUB 3.3's example of an encrypted image. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Resources other than the listed files may be encrypted, and encryption.xml describes this one. A validator cannot read the encrypted document, so it can only say it did not check it.

## Question

`OEBPS/content.xhtml` is encrypted with AES-128-CBC and described in `META-INF/encryption.xml`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> If an EPUB creator encrypts any resources within the container, they MUST include an encryption.xml file to provide information about the encryption used.

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> Encrypted data replaces unencrypted data in an OCF abstract container.

## Expected result

Valid. Resources other than the listed files may be encrypted, and encryption.xml describes this one. A validator cannot read the encrypted document, so it can only say it did not check it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i aes-encrypted-content.epub -u --advisory` | INFO RSC-004; VALID | `aes-encrypted-content.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-encrypted-content.epub -u` | INFO RSC-004; VALID | `aes-encrypted-content.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report INFO RSC-004: the encrypted document is not checked. That does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is replaced by its AES-128-CBC encryption (`scripts/lib/miniaes.py`): a 16-byte IV, then the ciphertext, padded as XML Encryption asks. The key and IV are fixed (`scripts/lib/ocfvariants.py`, `AES_KEY` and `AES_IV`), so the book is reproducible. `META-INF/encryption.xml` is added after `META-INF/container.xml`. It has an `EncryptedKey` (`Id="EK"`, `rsa-1_5`, `KeyName` `epub-test-books`, 128 fixed bytes as its `CipherValue`) and an `EncryptedData` with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"`, a `RetrievalMethod` to `#EK`, and `CipherReference URI="OEBPS/content.xhtml"`. The entry is stored, not Deflate-compressed.

## History

- 2026-11-13: First version.
