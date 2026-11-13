# encryption.xml declared encrypted

- Book: `never-encrypt-encryption-xml.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/never-encrypt-encryption-xml/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

META-INF/encryption.xml has one entry, which declares META-INF/encryption.xml itself encrypted with AES-128-CBC. Only the declaration is wrong. The file itself is left as it is, because an encrypted encryption.xml could not be read at all, and the book would then show more than one defect. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. encryption.xml must not be encrypted.

## Question

`META-INF/encryption.xml` declares itself encrypted. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-metainf-encryption.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-encryption.xml):

> EPUB creators MUST NOT encrypt the encryption.xml file when present.

## Expected result

Invalid. encryption.xml must not be encrypted.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i never-encrypt-encryption-xml.epub -u --advisory` | ERROR SPEC-001; INVALID | `never-encrypt-encryption-xml.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck never-encrypt-encryption-xml.epub -u` | no findings; VALID | `never-encrypt-encryption-xml.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1757](https://github.com/w3c/epubcheck/issues/1757), which names the never-encrypt files.

SPEC-001 is epubveri's id for a specification rule that epubcheck has no id for. It is in epubveri's default output, not an `--advisory` finding, so it fails the book and sets the exit code. epubveri lists it under [Known differences from epubcheck](https://github.com/veripublica/epubveri/blob/main/AGENTS.md#known-differences-from-epubcheck).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`META-INF/encryption.xml` is added after `META-INF/container.xml`. It has one `EncryptedData` element, with `EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"` and `CipherReference URI="META-INF/encryption.xml"`. The same build as the three other `never-encrypt-*` sets.

## History

- 2026-11-13: First version.
