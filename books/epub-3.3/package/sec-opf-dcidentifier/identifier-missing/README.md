# No dc:identifier

- Book: `identifier-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-opf-dcidentifier/identifier-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#41](https://github.com/veripublica/epub-test-books/issues/41)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has no dc:identifier element, so the required unique-identifier attribute points to nothing. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `unique-identifier` is required, so it stays in the book and now points to nothing. That follows from the same defect and can't be separated from it.

## Question

The metadata has no `dc:identifier`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-elem`](https://www.w3.org/TR/epub-33/#sec-metadata-elem):

> it MUST contain the [dcterms] dc:title, dc:identifier, and dc:language elements together with the [dcterms] dcterms:modified property.

## Expected result

Invalid. `unique-identifier` is required, so it stays in the book and now points to nothing. That follows from the same defect and can't be separated from it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i identifier-missing.epub -u --advisory` | ERROR RSC-005, ERROR OPF-030, ERROR RSC-005; INVALID | `identifier-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck identifier-missing.epub -u` | ERROR RSC-005, ERROR RSC-005, ERROR OPF-030; INVALID | `identifier-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

The errors other than the missing element are about the `unique-identifier` that now points to nothing.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the `dc:identifier` element is removed.

## History

- 2026-11-09: First version.
