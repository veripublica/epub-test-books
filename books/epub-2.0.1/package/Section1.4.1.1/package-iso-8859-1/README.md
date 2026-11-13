# A package document in ISO-8859-1

- Book: `package-iso-8859-1.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section1.4.1.1/package-iso-8859-1/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#210](https://github.com/veripublica/epub-test-books/issues/210)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document is encoded in ISO-8859-1 and says so. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. Only UTF-8 and UTF-16 are allowed.

## Question

The package document is encoded in ISO-8859-1 and says so. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section1.4.1.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section1.4.1.1):

> it is encoded in UTF-8 or UTF-16

## Expected result

Invalid. Only UTF-8 and UTF-16 are allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i package-iso-8859-1.epub -u --advisory` | ERROR RSC-028; INVALID | `package-iso-8859-1.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck package-iso-8859-1.epub -u` | ERROR RSC-028, ERROR RSC-028; INVALID | `package-iso-8859-1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/package.opf` is written in ISO-8859-1, its XML declaration says so, and its copyright sign is that encoding's byte.

## History

- 2026-11-09: First version.
