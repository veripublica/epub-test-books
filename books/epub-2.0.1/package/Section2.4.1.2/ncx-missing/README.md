# No NCX

- Book: `ncx-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/ncx-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#203](https://github.com/veripublica/epub-test-books/issues/203)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book has no NCX: no file, no manifest item and no toc attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The NCX is required.

## Question

The book has no NCX: no file, no manifest item and no `toc` attribute. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> OPS Publications must include an NCX.

## Expected result

Invalid. The NCX is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i ncx-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `ncx-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-missing.epub -u` | ERROR RSC-005; INVALID | `ncx-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The NCX file, its manifest item and the `toc` attribute are removed.

## History

- 2026-11-09: First version.
