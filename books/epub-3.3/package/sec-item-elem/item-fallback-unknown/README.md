# A `fallback` naming no item

- Book: `item-fallback-unknown.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-elem/item-fallback-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#71](https://github.com/veripublica/epub-test-books/issues/71)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A manifest item has a fallback attribute that names no item. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The value resolves to nothing.

## Question

A manifest item's `fallback` attribute names an `id` that no item has. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-elem`](https://www.w3.org/TR/epub-33/#sec-item-elem):

> The fallback attribute's IDREF [xml] value MUST resolve to another item in the manifest.

## Expected result

Invalid. The value resolves to nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i item-fallback-unknown.epub -u --advisory` | ERROR OPF-040; INVALID | `item-fallback-unknown.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck item-fallback-unknown.epub -u` | ERROR OPF-040; INVALID | `item-fallback-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the content item gets `fallback="nope"`.

## History

- 2026-11-09: First version.
