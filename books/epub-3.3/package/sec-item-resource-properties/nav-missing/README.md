# No item with the `nav` property

- Book: `nav-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/nav-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#73](https://github.com/veripublica/epub-test-books/issues/73)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document is in the manifest, but no item has the nav property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one item must have the property.

## Question

The navigation document is in the manifest, but no item has the `nav` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST declare exactly one item as the EPUB navigation document using the nav property.

## Expected result

Invalid. Exactly one item must have the property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i nav-missing.epub -u --advisory` | ERROR RSC-005, USAGE OPF-097; INVALID | `nav-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck nav-missing.epub -u` | ERROR RSC-005, USAGE OPF-097; INVALID | `nav-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `properties="nav"` is removed.

## History

- 2026-11-09: First version.
