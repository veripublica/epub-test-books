# A file encrypted with ZIP encryption

- Book: `zip-encryption.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/zip-encryption/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is encrypted with traditional PKWARE ZIP encryption. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. ZIP's own encryption must not be used.

## Question

`OEBPS/content.xhtml` is encrypted with traditional PKWARE ZIP encryption. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> Conforming OCF ZIP Containers MUST NOT use the encryption features defined by the ZIP format; instead, encryption MUST be done using the features described in Section

## Expected result

Invalid. ZIP's own encryption must not be used.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i zip-encryption.epub -u --advisory` | FATAL PKG-027; INVALID | `zip-encryption.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck zip-encryption.epub -u` | FATAL PKG-027; INVALID | `zip-encryption.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry is encrypted with traditional PKWARE encryption (flag bit 0); the password is `epub-test-books`.

## History

- 2026-11-12: First version.
