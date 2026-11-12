# Inline SVG without the `svg` property

- Book: `property-svg-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-svg-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#76](https://github.com/veripublica/epub-test-books/issues/76)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has inline SVG, and its manifest item has no svg property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `svg` is one of the listed properties, and this document embeds SVG.

## Question

The content document has inline SVG, and its manifest item has no `svg` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

## Expected result

Invalid. `svg` is one of the listed properties, and this document embeds SVG.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i property-svg-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-svg-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck property-svg-missing.epub -u` | ERROR OPF-014; INVALID | `property-svg-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

An inline `svg` element is added to `content.xhtml`. The accessibility metadata says the book has an image.

## History

- 2026-11-09: First version.
