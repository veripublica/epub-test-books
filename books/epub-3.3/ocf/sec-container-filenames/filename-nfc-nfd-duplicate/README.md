# Two file names that differ only in Unicode normalization

- Book: `filename-nfc-nfd-duplicate.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-filenames/filename-nfc-nfd-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#11](https://github.com/veripublica/epub-test-books/issues/11)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The OEBPS folder holds two files named e-acute.xhtml: one written with the single code point U+00E9, one with e followed by the combining acute accent U+0301. They look identical, and after normalization they are the same name. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. After canonical normalization the two names are equal.

## Question

The same folder holds `é.xhtml` written as one code point (U+00E9) and as two (U+0065 U+0301). Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-filenames`](https://www.w3.org/TR/epub-33/#sec-container-filenames):

> All file names within the same directory MUST be unique following Unicode canonical normalization [uax15] and then full case folding [unicode].

## Expected result

Invalid. After canonical normalization the two names are equal.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i filename-nfc-nfd-duplicate.epub -u --advisory` | ERROR OPF-060, ERROR OPF-074, USAGE PKG-012, USAGE PKG-012; INVALID | `filename-nfc-nfd-duplicate.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-nfc-nfd-duplicate.epub -u` | USAGE PKG-012, ERROR OPF-060, USAGE PKG-012, ERROR OPF-074; INVALID | `filename-nfc-nfd-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark.

The other findings follow from the defect. ERROR OPF-074 says the two manifest items resolve to one resource once their names are normalized. USAGE PKG-012 appears once for each file name with a non-ASCII character.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

Two documents are added to the ZIP, the manifest and the spine: `OEBPS/\u00e9.xhtml` and `OEBPS/e\u0301.xhtml`, referred to as `%C3%A9.xhtml` and `e%CC%81.xhtml`.

## History

- 2026-11-08: First version.
