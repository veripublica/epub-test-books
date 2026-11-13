# No `dcterms:modified`

- Book: `modified-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-metadata-last-modified/modified-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#61](https://github.com/veripublica/epub-test-books/issues/61)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has no dcterms:modified property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one is required.

## Question

The metadata has no `dcterms:modified`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-last-modified`](https://www.w3.org/TR/epub-33/#sec-metadata-last-modified):

> The metadata section MUST contain exactly one dcterms:modified property [dcterms] containing the last modification date.

## Expected result

Invalid. Exactly one is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i modified-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `modified-missing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck modified-missing.epub -u` | ERROR RSC-005; INVALID | `modified-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `dcterms:modified` property is removed.

## History

- 2026-11-09: First version.
