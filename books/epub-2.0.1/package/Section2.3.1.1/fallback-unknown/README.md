# A `fallback` naming no item

- Book: `fallback-unknown.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3.1.1/fallback-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#194](https://github.com/veripublica/epub-test-books/issues/194)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A manifest item has a fallback attribute that names no item. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The value must be the ID of an item.

## Question

A manifest item's `fallback` names an `id` that no item has. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3.1.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3.1.1):

> An item identifies a fallback item using its fallback attribute, which must specify the ID of the item element that identifies the fallback.

## Expected result

Invalid. The value must be the ID of an item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i fallback-unknown.epub -u --advisory` | ERROR OPF-040; INVALID | `fallback-unknown.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck fallback-unknown.epub -u` | ERROR OPF-040; INVALID | `fallback-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the content item gets `fallback="nope"`.

## History

- 2026-11-09: First version.
