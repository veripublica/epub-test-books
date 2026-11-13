# An encryption.xml entry for a file that is not in the container

- Book: `cipher-reference-missing-file.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-encryption.xml-encryption/cipher-reference-missing-file/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after the encryption sets; settled in w3c/epub-specs#3106
- Issue: pending
- Other clauses: XML Encryption 1.1 `sec-CipherData`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

META-INF/encryption.xml declares one file encrypted with AES-128-CBC, OEBPS/secret.xhtml, with an EncryptedKey and an EncryptedData that refers to it. The container has no such file. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An EncryptedData entry describes an encrypted file, and its CipherReference must lead to the encrypted data. Here it leads to nothing.

## Question

`META-INF/encryption.xml` declares `OEBPS/secret.xhtml` encrypted, and the container has no such file. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-encryption.xml-encryption`](https://www.w3.org/TR/epub-33/#sec-encryption.xml-encryption):

> The encryption element contains child elements of type EncryptedKey and EncryptedData as defined by [xmlenc-core1].
>
> An EncryptedKey element describes each encryption key used in the container, while an EncryptedData element describes each encrypted file.

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> OCF encryption supports only the encryption of entire files within the container, not parts of files.

XML Encryption Syntax and Processing Version 1.1, [`sec-CipherData`](https://www.w3.org/TR/xmlenc-core1/#sec-CipherData) (3.3 The CipherData Element; W3C Recommendation, 11 April 2013):

> The CipherData is a mandatory element that provides the encrypted data. It must either contain the encrypted octet sequence as base64 encoded text as element content of the CipherValue element, or provide a reference to an external location containing the encrypted octet sequence via the CipherReference element.

## Expected result

Invalid. An `EncryptedData` entry describes an encrypted file, and its `CipherReference` must lead to the encrypted data. Here it leads to nothing.

The EPUB 3.3 text does not say this in one sentence, so this set waited for the Working Group. In [w3c/epub-specs#3106](https://github.com/w3c/epub-specs/issues/3106), discussed at the [Publishing Maintenance Working Group meeting of 12 November 2026](https://w3c.github.io/pm-wg/minutes/2026-11-12.html#1d80), the group found that a missing referenced file is an error under XML Encryption, and agreed to say so: "no objection to fixing this and requiring pointing at a real thing". [w3c/epub-specs#3109](https://github.com/w3c/epub-specs/pull/3109), a pull request for the EPUB 3.4 draft (open on 2026-11-13), would make it explicit: `CipherData`, as the child of `EncryptedData`, "MUST have a child CipherReference element whose URI attribute references a container resource". (XML Encryption writes "must" in lower case; the group reads it as a requirement.)

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i cipher-reference-missing-file.epub -u --advisory` | ERROR RSC-007; INVALID | `cipher-reference-missing-file.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck cipher-reference-missing-file.epub -u` | ERROR RSC-007; INVALID | `cipher-reference-missing-file.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`META-INF/encryption.xml` is added after `META-INF/container.xml`, built as in `aes-encrypted-content`: an `EncryptedKey` (`Id="EK"`, `rsa-1_5`, `KeyName` `epub-test-books`) and an `EncryptedData` with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"`, a `RetrievalMethod` to `#EK`, and `CipherReference URI="OEBPS/secret.xhtml"`. No file of that name is added, and every other file is left as it is.

## History

- 2026-11-13: First version.
