# A file Deflate-compressed, then encrypted, with its Compression property (valid)

- Book: `aes-compressed-first.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-enc-compression/aes-compressed-first/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#529](https://github.com/veripublica/epub-test-books/issues/529)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is compressed with Deflate, then encrypted with AES-128-CBC. META-INF/encryption.xml describes it, and its EncryptionProperties give a Compression element with Method 8 and the original length. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is the order EPUB 3.3 recommends for a non-codec file, with Deflate and the Compression property it asks for.

## Question

`OEBPS/content.xhtml` is Deflate-compressed, then encrypted, and `META-INF/encryption.xml` gives its Compression property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-enc-compression`](https://www.w3.org/TR/epub-33/#sec-enc-compression):

> When stored in an OCF ZIP container, EPUB creators SHOULD compress streams of data with non-codec content types before encrypting them.
>
> EPUB creators MUST use Deflate compression.

EPUB 3.3, [`sec-enc-compression`](https://www.w3.org/TR/epub-33/#sec-enc-compression):

> When EPUB creators compress streams of data before encrypting, they SHOULD provide additional EncryptionProperties metadata to specify the size of the initial resource (i.e., before compression and encryption), as per the Compression XML element defined below.

## Expected result

Valid. This is the order EPUB 3.3 recommends for a non-codec file, with Deflate and the Compression property it asks for.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i aes-compressed-first.epub -u --advisory` | INFO RSC-004; VALID | `aes-compressed-first.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-compressed-first.epub -u` | INFO RSC-004; VALID | `aes-compressed-first.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report INFO RSC-004: the encrypted document is not checked. That does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is compressed with raw Deflate, then replaced by the AES-128-CBC encryption of that (`scripts/lib/miniaes.py`): a 16-byte IV, then the ciphertext, padded as XML Encryption asks. The key and IV are fixed (`scripts/lib/ocfvariants.py`, `AES_KEY` and `AES_IV`), so the book is reproducible. `META-INF/encryption.xml` is added after `META-INF/container.xml`. It has an `EncryptedKey` (`Id="EK"`, `rsa-1_5`, `KeyName` `epub-test-books`, 128 fixed bytes as its `CipherValue`) and an `EncryptedData` with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"`, a `RetrievalMethod` to `#EK`, and `CipherReference URI="OEBPS/content.xhtml"`. Inside `EncryptedData`, `EncryptionProperties` holds one `EncryptionProperty` with `<c:Compression Method="8" OriginalLength="…"/>` (namespace `http://www.idpf.org/2016/encryption#compression`), the length of the document before compression. The ZIP entry is stored.

## History

- 2026-11-13: First version.
