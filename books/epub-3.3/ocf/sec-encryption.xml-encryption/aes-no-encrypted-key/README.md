# A content document encrypted with AES-128-CBC, with no `EncryptedKey` (valid)

- Book: `aes-no-encrypted-key.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-encryption.xml-encryption/aes-no-encrypted-key/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3112
- Issue: [#673](https://github.com/veripublica/epub-test-books/issues/673)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is encrypted with AES-128-CBC, and META-INF/encryption.xml describes it with one EncryptedData that names its key (KeyName epub-test-books) and no EncryptedKey, as LCP and font obfuscation do. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The EncryptedData names its key itself, and EncryptedKey is optional: the Working Group fixed EPUB 3.3's '1 or more' to '0 or more' (w3c/epub-specs#3112).

## Question

`OEBPS/content.xhtml` is encrypted, and `META-INF/encryption.xml` has an `EncryptedData` for it but no `EncryptedKey`. Does a validator accept the book?

## Clause

EPUB 3.3, [`elemdef-encryption`](https://www.w3.org/TR/epub-33/#elemdef-encryption) (content model of `encryption`):

> EncryptedKey [1 or more]

EPUB 3.3, [`sec-encryption.xml-encryption`](https://www.w3.org/TR/epub-33/#sec-encryption.xml-encryption):

> An EncryptedKey element describes each encryption key used in the container, while an EncryptedData element describes each encrypted file. Each EncryptedData element refers to an EncryptedKey element, as described in XML Encryption.

EPUB 3.4, Editor's Draft, [`elemdef-encryption`](https://w3c.github.io/epub-specs/epub34/authoring/#elemdef-encryption) (fetched 2026-11-20, after [w3c/epub-specs#3114](https://github.com/w3c/epub-specs/pull/3114)):

> EncryptedKey [0 or more]

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> Encrypted data replaces unencrypted data in an OCF abstract container.

## Expected result

Valid. encryption.xml may describe an encrypted file without an EncryptedKey: the EncryptedData names its key itself. The EPUB 3.3 content model asks for one or more EncryptedKey elements, but the Working Group has fixed that as an error (w3c/epub-specs#3112).

EPUB 3.3's content model for `encryption` reads "EncryptedKey [1 or more]", and it says that each `EncryptedData` "refers to an EncryptedKey element". Read alone, that makes this book invalid, but it also makes every font-obfuscated EPUB 3 book invalid (EPUB 3.3's own example of obfuscation has no `EncryptedKey`), and LCP-protected books too. The question was raised in [w3c/epub-specs#3109](https://github.com/w3c/epub-specs/pull/3109#issuecomment-6848488238), and the Working Group opened [w3c/epub-specs#3112](https://github.com/w3c/epub-specs/issues/3112), "EncryptedKey is not always required". [w3c/epub-specs#3114](https://github.com/w3c/epub-specs/pull/3114), merged on 2026-11-16, changes the content model to "EncryptedKey [0 or more]" and drops the sentence that each `EncryptedData` refers to one; its change log calls this a fix of the content model. As that pull request notes, XML Encryption already lets `KeyInfo` refer to a key held elsewhere, or to no key at all; this book's `KeyName` names one. The fix is in the EPUB 3.4 draft; this set follows it for EPUB 3.3 as well, as both verifiers do.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i aes-no-encrypted-key.epub -u --advisory` | INFO RSC-004; VALID | `aes-no-encrypted-key.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-no-encrypted-key.epub -u` | INFO RSC-004; VALID | `aes-no-encrypted-key.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

INFO RSC-004 says the encrypted document is not checked. That does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is replaced by its AES-128-CBC encryption, as in `aes-encrypted-content` (`scripts/lib/miniaes.py`; fixed key and IV in `scripts/lib/ocfvariants.py`). `META-INF/encryption.xml` is added after `META-INF/container.xml`. It has one `EncryptedData` with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"`, `KeyInfo` holding `KeyName` `epub-test-books`, and `CipherReference URI="OEBPS/content.xhtml"`, and no `EncryptedKey`. The entry is stored, not Deflate-compressed.

## History

- 2026-11-20: First version.
