# An NCX link to a missing file

- Book: `ncx-src-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/ncx-src-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#208](https://github.com/veripublica/epub-test-books/issues/208)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A content element in the NCX points to a file that is not in the book. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The URI must resolve to an OPS Content Document.

## Question

A `content` element in the NCX points to a file that is not in the book. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> The URI specified by the src of the content element for navMap, pageList, and navList elements must resolve to OPS Content Document fragments.

## Expected result

Invalid. The URI must resolve to an OPS Content Document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i ncx-src-missing.epub -u --advisory` | ERROR RSC-007; INVALID | `ncx-src-missing.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-src-missing.epub -u` | ERROR RSC-007; INVALID | `ncx-src-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/toc.ncx`, one `src` becomes `nope.xhtml`.

## History

- 2026-11-09: First version.
