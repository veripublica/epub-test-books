# Two `spine` elements

- Book: `spine-twice.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/spine-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#198](https://github.com/veripublica/epub-test-books/issues/198)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has two spine elements. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. There must be only one.

## Question

The package document has two `spine` elements. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> Following manifest, there must be one and only one spine element, which contains one or more itemref elements.

## Expected result

Invalid. There must be only one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i spine-twice.epub -u --advisory` | ERROR RSC-005; INVALID | `spine-twice.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-twice.epub -u` | ERROR RSC-005, ERROR OPF-034; INVALID | `spine-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

epubcheck also gives OPF-034, because the two spines list the content document twice.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a second `spine` is added after the first.

## History

- 2026-11-09: First version.
