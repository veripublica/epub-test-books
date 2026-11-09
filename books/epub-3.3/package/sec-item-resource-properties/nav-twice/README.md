# Two items with the `nav` property

- Book: `nav-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/nav-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#74](https://github.com/veripublica/epub-test-books/issues/74)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two navigation documents in the manifest both have the nav property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Exactly one item may have the property.

## Question

Two navigation documents in the manifest both have the `nav` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST declare exactly one item as the EPUB navigation document using the nav property.

## Expected result

Invalid. Exactly one item may have the property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i nav-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `nav-twice.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck nav-twice.epub -u` | ERROR RSC-005; INVALID | `nav-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A second navigation document, `OEBPS/nav2.xhtml`, is added with `properties="nav"`.

## History

- 2026-11-09: First version.
