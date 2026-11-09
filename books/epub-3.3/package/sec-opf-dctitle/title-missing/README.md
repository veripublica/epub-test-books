# No `dc:title`

- Book: `title-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-opf-dctitle/title-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#53](https://github.com/veripublica/epub-test-books/issues/53)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has no dc:title element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The element is required.

## Question

The metadata has no `dc:title`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-elem`](https://www.w3.org/TR/epub-33/#sec-metadata-elem):

> it MUST contain the [dcterms] dc:title, dc:identifier, and dc:language elements together with the [dcterms] dcterms:modified property.

## Expected result

Invalid. The element is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i title-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `title-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck title-missing.epub -u` | ERROR RSC-005; INVALID | `title-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `dc:title` element is removed.

## History

- 2026-11-09: First version.
