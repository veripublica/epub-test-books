# Two `dc:date` elements

- Book: `date-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-opf-dcdate/date-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#60](https://github.com/veripublica/epub-test-books/issues/60)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has two dc:date elements. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. One is the most allowed.

## Question

The metadata has two `dc:date` elements. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-opf-dcdate`](https://www.w3.org/TR/epub-33/#sec-opf-dcdate):

> EPUB publications MUST NOT contain more than one dc:date element.

## Expected result

Invalid. One is the most allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i date-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `date-twice.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck date-twice.epub -u` | ERROR RSC-005; INVALID | `date-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<dc:date>2026-01-01</dc:date>` is added to the metadata.

## History

- 2026-11-09: First version.
