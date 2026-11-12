# An NCX link to a stylesheet

- Book: `ncx-src-css.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/ncx-src-css/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#209](https://github.com/veripublica/epub-test-books/issues/209)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A content element in the NCX points to a CSS file in the manifest. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The URI must resolve to an OPS Content Document.

## Question

A `content` element in the NCX points to a CSS file in the manifest. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> The URI specified by the src of the content element for navMap, pageList, and navList elements must resolve to OPS Content Document fragments.

## Expected result

Invalid. The URI must resolve to an OPS Content Document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i ncx-src-css.epub -u --advisory` | ERROR RSC-010, USAGE ADV-010; INVALID | `ncx-src-css.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-src-css.epub -u` | ERROR RSC-010; INVALID | `ncx-src-css.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

`OEBPS/style.css` is added to the manifest, and one `src` in `OEBPS/toc.ncx` points to it.

## History

- 2026-11-09: First version.
