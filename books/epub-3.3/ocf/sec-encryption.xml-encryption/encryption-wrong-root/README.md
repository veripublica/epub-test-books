# encryption.xml with the wrong root element

- Book: `encryption-wrong-root.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-encryption.xml-encryption/encryption-wrong-root/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#30](https://github.com/veripublica/epub-test-books/issues/30)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book's font is obfuscated correctly, but the root element of META-INF/encryption.xml is named encryptions. Everything else is the font-obfuscated book.

Expected result: Invalid. The root element of encryption.xml must be encryption.

## Question

The root element of `META-INF/encryption.xml` is `encryptions` instead of `encryption`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-encryption.xml-encryption`](https://www.w3.org/TR/epub-33/#sec-encryption.xml-encryption):

> Element Name: encryption Namespace: urn:oasis:names:tc:opendocument:xmlns:container Usage: REQUIRED root element [xml] of the encryption.xml file.

The sentence joins the lines of the element definition.

## Expected result

Invalid. The root element of encryption.xml must be encryption.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i encryption-wrong-root.epub -u --advisory` | ERROR RSC-005, INFO RSC-004, USAGE OBS-001, USAGE CSS-028; INVALID | `encryption-wrong-root.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck encryption-wrong-root.epub -u` | ERROR RSC-005, USAGE OBS-001, USAGE CSS-028, USAGE CSS-028, INFO RSC-004; INVALID | `encryption-wrong-root.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark.

The other findings come with the font. Both tools still read the entry, so INFO RSC-004 says the obfuscated font is not checked. USAGE OBS-001 says font obfuscation is outdated. USAGE CSS-028 appears twice from epubcheck and once from epubveri, as in `font-obfuscated`. epubveri 0.37.1 did not give RSC-004 here.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The `font-obfuscated` book, with `<encryption …>` renamed `<encryptions …>` in `META-INF/encryption.xml`. The namespace and the `EncryptedData` entry stay the same.

## History

- 2026-11-08: First version.
