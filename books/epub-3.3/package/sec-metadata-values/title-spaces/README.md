# `dc:title` of only spaces

- Book: `title-spaces.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-metadata-values/title-spaces/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#54](https://github.com/veripublica/epub-test-books/issues/54)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:title element holds only spaces. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The value is empty once whitespace is stripped.

## Question

The `dc:title` element holds only spaces. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-values`](https://www.w3.org/TR/epub-33/#sec-metadata-values):

> These elements MUST have non-empty values after leading and trailing ASCII whitespace [infra] is stripped (i.e., they must consist of at least one non-whitespace character).

## Expected result

Invalid. The value is empty once whitespace is stripped.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i title-spaces.epub -u --advisory` | ERROR RSC-005; INVALID | `title-spaces.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck title-spaces.epub -u` | ERROR RSC-005; INVALID | `title-spaces.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the value of `dc:title` becomes three spaces.

## History

- 2026-11-09: First version.
