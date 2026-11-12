# An NCX without `navMap`

- Book: `ncx-navmap-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/ncx-navmap-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#207](https://github.com/veripublica/epub-test-books/issues/207)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The NCX has no navMap element. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The element is required.

## Question

The NCX has no `navMap`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> navMap is a required element in the NCX

## Expected result

Invalid. The element is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i ncx-navmap-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `ncx-navmap-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-navmap-missing.epub -u` | ERROR RSC-005; INVALID | `ncx-navmap-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/toc.ncx`, `navMap` is removed.

## History

- 2026-11-09: First version.
