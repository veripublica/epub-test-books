# `dc:identifier` of only spaces

- Book: `identifier-spaces.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-metadata-values/identifier-spaces/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#55](https://github.com/veripublica/epub-test-books/issues/55)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:identifier element holds only spaces. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The value is empty once whitespace is stripped.

## Question

The `dc:identifier` element holds only spaces. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-values`](https://www.w3.org/TR/epub-33/#sec-metadata-values):

> These elements MUST have non-empty values after leading and trailing ASCII whitespace [infra] is stripped (i.e., they must consist of at least one non-whitespace character).

## Expected result

Invalid. The value is empty once whitespace is stripped.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i identifier-spaces.epub -u --advisory` | ERROR RSC-005; INVALID | `identifier-spaces.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck identifier-spaces.epub -u` | ERROR RSC-005; INVALID | `identifier-spaces.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the value of `dc:identifier` becomes three spaces.

## History

- 2026-11-09: First version.
