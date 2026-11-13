# An encryption algorithm EPUB does not name (valid)

- Book: `aes-unknown-algorithm.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-unknown-algorithm/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is encrypted, and META-INF/encryption.xml describes it: an EncryptedKey (an RSA-wrapped key) and an EncryptedData that refers to it, as in EPUB 3.3's example of an encrypted image. Its EncryptionMethod names an algorithm by a URI that no specification defines. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.3 uses XML Encryption as a framework and does not restrict the algorithm. A reading system without the algorithm cannot open the document, but the container is not wrong for that.

## Question

`META-INF/encryption.xml` names an encryption algorithm by a URI that no specification defines. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> OCF uses XML Encryption [xmlenc-core1] to provide a framework for encryption, allowing a variety of algorithms to be used.

## Expected result

Valid. EPUB 3.3 uses XML Encryption as a framework and does not restrict the algorithm. A reading system without the algorithm cannot open the document, but the container is not wrong for that.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i aes-unknown-algorithm.epub -u --advisory` | INFO RSC-004; VALID | `aes-unknown-algorithm.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-unknown-algorithm.epub -u` | INFO RSC-004; VALID | `aes-unknown-algorithm.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report INFO RSC-004: the encrypted document is not checked. Neither reports the unknown algorithm. That does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is replaced by its AES-128-CBC encryption (`scripts/lib/miniaes.py`): a 16-byte IV, then the ciphertext, padded as XML Encryption asks. The key and IV are fixed (`scripts/lib/ocfvariants.py`, `AES_KEY` and `AES_IV`), so the book is reproducible. `META-INF/encryption.xml` is added after `META-INF/container.xml`. It has an `EncryptedKey` (`Id="EK"`, `rsa-1_5`, `KeyName` `epub-test-books`, 128 fixed bytes as its `CipherValue`) and an `EncryptedData` with `EncryptionMethod Algorithm="https://example.org/epub-test-books/no-such-cipher"`, a `RetrievalMethod` to `#EK`, and `CipherReference URI="OEBPS/content.xhtml"`. The bytes are AES-128-CBC, as in `aes-encrypted-content`; only the algorithm URI differs.

## History

- 2026-11-13: First version.
