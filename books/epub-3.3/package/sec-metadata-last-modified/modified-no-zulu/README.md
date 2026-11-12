# `dcterms:modified` ending in +00:00

- Book: `modified-no-zulu.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-metadata-last-modified/modified-no-zulu/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#62](https://github.com/veripublica/epub-test-books/issues/62)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dcterms:modified value ends in +00:00 instead of Z. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The time is UTC but does not end in `Z`.

## Question

The `dcterms:modified` value ends in `+00:00` instead of `Z`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-last-modified`](https://www.w3.org/TR/epub-33/#sec-metadata-last-modified):

> EPUB creators MUST express the last modification date in Coordinated Universal Time (UTC) and MUST terminate it with the "Z" (Zulu) time zone indicator.

## Expected result

Invalid. The time is UTC but does not end in `Z`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i modified-no-zulu.epub -u --advisory` | ERROR RSC-005; INVALID | `modified-no-zulu.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck modified-no-zulu.epub -u` | ERROR RSC-005; INVALID | `modified-no-zulu.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the final `Z` of `dcterms:modified` becomes `+00:00`.

## History

- 2026-11-09: First version.
