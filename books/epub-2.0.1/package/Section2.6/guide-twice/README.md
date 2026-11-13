# Two `guide` elements

- Book: `guide-twice.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.6/guide-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#226](https://github.com/veripublica/epub-test-books/issues/226)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has two guide elements. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. There may be one.

## Question

The package document has two `guide` elements. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.6`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.6):

> Within the package there may be one guide element, containing one or more reference elements.

## Expected result

Invalid. There may be one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i guide-twice.epub -u --advisory` | ERROR RSC-005, WARNING RSC-017, WARNING RSC-017; INVALID | `guide-twice.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck guide-twice.epub -u` | ERROR RSC-005, WARNING RSC-017, WARNING RSC-017; INVALID | `guide-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, two `guide` elements are added after `spine`.

## History

- 2026-11-09: First version.
