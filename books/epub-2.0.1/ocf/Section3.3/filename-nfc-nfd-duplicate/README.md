# Two file names that differ only in Unicode normalization (valid)

- Book: `filename-nfc-nfd-duplicate.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.3/filename-nfc-nfd-duplicate/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/ holds é.xhtml twice: once as one code point (U+00E9) and once as two (U+0065 U+0301), both in the manifest and the spine. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. OCF 2.0.1 allows two names in the same directory to map to the same string after accent normalization. (EPUB 3.3 does not.)

## Question

`OEBPS/` holds `é.xhtml` twice: once as one code point (U+00E9) and once as two (U+0065 U+0301), both in the manifest and the spine. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (File Names; Recommended Specification, 4 September 2010):

> Two File Names within the same directory MAY map to the same string following accent normalization.

## Expected result

Valid. OCF 2.0.1 allows two names in the same directory to map to the same string after accent normalization. (EPUB 3.3 does not.)

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i filename-nfc-nfd-duplicate.epub -u --advisory` | USAGE PKG-012, USAGE PKG-012; VALID | `filename-nfc-nfd-duplicate.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-nfc-nfd-duplicate.epub -u` | USAGE PKG-012, ERROR OPF-060, USAGE PKG-012, ERROR OPF-074; INVALID | `filename-nfc-nfd-duplicate.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the two names as duplicates (OPF-060, OPF-074).

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. Two content documents, `OEBPS/é.xhtml` in NFC and in NFD, are added to the manifest (`%C3%A9.xhtml`, `e%CC%81.xhtml`) and the spine.

## History

- 2026-11-12: First version.
