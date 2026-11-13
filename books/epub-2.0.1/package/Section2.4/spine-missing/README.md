# No `spine`

- Book: `spine-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/spine-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#196](https://github.com/veripublica/epub-test-books/issues/196)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has no spine element. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. There must be one.

## Question

The package document has no `spine` element. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> Following manifest, there must be one and only one spine element, which contains one or more itemref elements.

## Expected result

Invalid. There must be one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i spine-missing.epub -u --advisory` | ERROR RSC-005, USAGE ADV-010, USAGE ADV-010, USAGE ADV-010; INVALID | `spine-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-missing.epub -u` | ERROR RSC-005; INVALID | `spine-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, `spine` is removed.

## History

- 2026-11-09: First version.
