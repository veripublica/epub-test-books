# Two dcterms:modified, neither refining anything

- Book: `modified-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-metadata-last-modified/modified-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#43](https://github.com/veripublica/epub-test-books/issues/43)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has two dcterms:modified properties, and neither refines anything. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Both properties describe the publication, so there are two where exactly one is allowed. Both values are well-formed.

## Question

The metadata has two `dcterms:modified` properties, and neither has a `refines` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-metadata-last-modified`](https://www.w3.org/TR/epub-33/#sec-metadata-last-modified):

> The metadata section MUST contain exactly one dcterms:modified property [dcterms] containing the last modification date.

> EPUB creators MAY specify additional modified properties in the package document metadata, but they MUST have a different subject (i.e., they require a refines attribute that references an element or resource).

## Expected result

Invalid. Both properties describe the publication, so there are two where exactly one is allowed. Both values are well-formed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i modified-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `modified-twice.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck modified-twice.epub -u` | ERROR RSC-005; INVALID | `modified-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a second `dcterms:modified` with the value `2026-01-01T00:00:00Z` follows the template's.

## History

- 2026-11-09: First version.
