# container.xml declared encrypted

- Book: `never-encrypt-container-xml.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/never-encrypt-container-xml/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri, after the encryption sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book has a META-INF/encryption.xml with one entry, which declares META-INF/container.xml encrypted with AES-128-CBC. Only the declaration is wrong. The file itself is left as it is, because real encryption would also make it unreadable, and the book would then show more than one defect. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. META-INF/container.xml is on the list of files that must not be encrypted.

## Question

`META-INF/encryption.xml` declares `META-INF/container.xml` encrypted. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#encryption-restrictions):

> EPUB creators MUST NOT encrypt the following files:
>
> - mimetype
> - META-INF/container.xml
> - META-INF/encryption.xml
> - META-INF/manifest.xml
> - META-INF/metadata.xml
> - META-INF/rights.xml
> - META-INF/signatures.xml
> - package document

## Expected result

Invalid. META-INF/container.xml is on the list of files that must not be encrypted.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i never-encrypt-container-xml.epub -u --advisory` | ERROR SPEC-001; INVALID | `never-encrypt-container-xml.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck never-encrypt-container-xml.epub -u` | VALID | `never-encrypt-container-xml.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** Issue on `w3c/epubcheck`: ISSUE.

SPEC-001 is epubveri's id for a specification rule that epubcheck has no id for. It is in epubveri's default output, not an `--advisory` finding.

## Build

`META-INF/encryption.xml` is added after `META-INF/container.xml`. It has one `EncryptedData` element, with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"` and `CipherReference URI="META-INF/container.xml"`.

## History

- 2026-11-09: First version.
