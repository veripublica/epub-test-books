# A meta element without property

- Book: `meta-no-property.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-meta-elem/meta-no-property/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#45](https://github.com/veripublica/epub-test-books/issues/45)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has one extra meta element with text and no property attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

The metadata has one extra `meta` element with text and no `property` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-meta-elem`](https://www.w3.org/TR/epub-33/#sec-meta-elem):

> property [required]

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i meta-no-property.epub -u --advisory` | ERROR RSC-005; INVALID | `meta-no-property.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-no-property.epub -u` | ERROR RSC-005; INVALID | `meta-no-property.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<meta>A value with no property</meta>` is added to the metadata.

## History

- 2026-11-09: First version.
