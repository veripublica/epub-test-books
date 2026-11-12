# A manifest item without `media-type`

- Book: `item-media-type-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-elem/item-media-type-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#72](https://github.com/veripublica/epub-test-books/issues/72)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One extra manifest item has no media-type attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

One extra manifest item has no `media-type` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-elem`](https://www.w3.org/TR/epub-33/#sec-item-elem):

> media-type [required]

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i item-media-type-missing.epub -u --advisory` | ERROR RSC-005, USAGE OPF-097; INVALID | `item-media-type-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck item-media-type-missing.epub -u` | ERROR RSC-005, USAGE OPF-097; INVALID | `item-media-type-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.txt` is added, and `<item id="extra" href="extra.txt"/>` is added to the manifest.

## History

- 2026-11-09: First version.
