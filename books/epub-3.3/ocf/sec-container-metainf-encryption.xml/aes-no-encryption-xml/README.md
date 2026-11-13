# An encrypted file with no encryption.xml

- Book: `aes-no-encryption-xml.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/aes-no-encryption-xml/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#526](https://github.com/veripublica/epub-test-books/issues/526)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is encrypted with AES-128-CBC, and the container has no META-INF/encryption.xml. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An encrypted resource needs encryption.xml. Without it, a validator reads the ciphertext as the content document, which is not well-formed either.

## Question

`OEBPS/content.xhtml` is encrypted, and there is no `META-INF/encryption.xml`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> If an EPUB creator encrypts any resources within the container, they MUST include an encryption.xml file to provide information about the encryption used.

## Expected result

Invalid. An encrypted resource needs encryption.xml. Without it, a validator reads the ciphertext as the content document, which is not well-formed either.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i aes-no-encryption-xml.epub -u --advisory` | FATAL RSC-016, FATAL RSC-016; INVALID | `aes-no-encryption-xml.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck aes-no-encryption-xml.epub -u` | FATAL RSC-016; INVALID | `aes-no-encryption-xml.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Both read the ciphertext as the content document and find it not well-formed (FATAL RSC-016). Neither says that `encryption.xml` is missing; the verdict is still the expected one.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is replaced by its AES-128-CBC encryption, as in `aes-encrypted-content`. No `META-INF/encryption.xml` is added.

## History

- 2026-11-13: First version.
