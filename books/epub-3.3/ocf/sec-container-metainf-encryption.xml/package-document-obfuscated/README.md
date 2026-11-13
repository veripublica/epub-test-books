# The package document obfuscated

- Book: `package-document-obfuscated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-encryption.xml/package-document-obfuscated/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after the encryption sets
- Issue: [#521](https://github.com/veripublica/epub-test-books/issues/521)
- Other clauses: EPUB 3.3 `obfus-specifying`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/package.opf, the package document, is obfuscated with the font obfuscation algorithm: its first 1040 bytes are XORed with the key derived from the unique identifier. META-INF/encryption.xml lists it with that algorithm. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The package document must not be encrypted, and the obfuscation algorithm is only for fonts.

## Question

`OEBPS/package.opf`, the package document, is obfuscated with the font obfuscation algorithm and listed in `META-INF/encryption.xml`. Does a validator reject it?

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

EPUB 3.3, [`obfus-specifying`](https://www.w3.org/TR/epub-33/#obfus-specifying):

> As the obfuscation algorithm is restricted to fonts, the URI attribute of the CipherReference element MUST reference a Font core media type resource.

## Expected result

Invalid. The package document must not be encrypted, and the obfuscation algorithm is only for fonts.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i package-document-obfuscated.epub -u --advisory` | FATAL RSC-016, ERROR SPEC-001, ERROR OPF-001; INVALID | `package-document-obfuscated.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-document-obfuscated.epub -u` | FATAL RSC-016, ERROR OPF-001; INVALID | `package-document-obfuscated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Both read the obfuscated bytes as the package document, find it not well-formed (RSC-016), and so cannot read the EPUB version (OPF-001). Only epubveri also reports the declaration itself: SPEC-001, a package document declared encrypted. epubcheck gives no finding for `META-INF/encryption.xml`, as on `never-encrypt-package-document`, where it misses the case. epubcheck also prints a Java stack trace (`IllegalStateException` in `OCFChecker.checkPublicationVersion`) before its summary; the summary and exit code are still given. The stack trace is reported as [w3c/epubcheck#1774](https://github.com/w3c/epubcheck/issues/1774).

SPEC-001 is epubveri's id for a specification rule that epubcheck has no id for. It is in epubveri's default output, not an `--advisory` finding. Every epubveri finding here is in its default output.

## Build

`META-INF/encryption.xml` is added after `META-INF/container.xml`. It has one `EncryptedData` element, with `EncryptionMethod Algorithm="http://www.idpf.org/2008/embedding"` and `CipherReference URI="OEBPS/package.opf"`. The first 1040 bytes of `OEBPS/package.opf` are XORed with the SHA-1 of the unique identifier (EPUB 3.3 §4.4.3), as `scripts/lib/minifont.py` `obfuscate()` does for fonts; the rest of the file is left as it is. The `obfuscated-not-font` set does the same to a stylesheet, and `never-encrypt-package-document` declares the package document encrypted without changing its bytes.

## History

- 2026-11-13: First version.
