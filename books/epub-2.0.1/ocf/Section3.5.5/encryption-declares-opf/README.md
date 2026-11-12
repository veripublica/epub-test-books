# `encryption.xml` that declares the package document encrypted

- Book: `encryption-declares-opf.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.5/encryption-declares-opf/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

META-INF/encryption.xml declares OEBPS/package.opf encrypted with AES-128-CBC. The file's bytes are left as they are. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The package document must never be encrypted.

## Question

`META-INF/encryption.xml` declares `OEBPS/package.opf` encrypted with AES-128-CBC. The file's bytes are left as they are. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.5](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Encryption – META-INF/encryption.xml (Optional); Recommended Specification, 4 September 2010):

> The following files MUST never be encrypted (regardless of whether default or specific encryption is requested):

> mimetype

> META-INF/container.xml

> META-INF/manifest.xml

> META-INF/metadata.xml

> META-INF/signatures.xml

> META-INF/encryption.xml

> META-INF/rights.xml

> EPUB rootfile (the OPF Package file)

## Expected result

Invalid. The package document must never be encrypted.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i encryption-declares-opf.epub -u --advisory` | ERROR SPEC-001; INVALID | `encryption-declares-opf.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck encryption-declares-opf.epub -u` | no findings; VALID | `encryption-declares-opf.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing for the declaration.

- **epubcheck: missed.** [w3c/epubcheck#1757](https://github.com/w3c/epubcheck/issues/1757), opened for EPUB 3; the same happens at EPUB 2.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/encryption.xml`, second in the archive, with one `EncryptedData` whose `CipherReference` is `OEBPS/package.opf`.

## History

- 2026-11-12: First version.
