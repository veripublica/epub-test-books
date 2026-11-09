# A `toc` attribute pointing to XHTML

- Book: `toc-not-ncx.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/toc-not-ncx/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#205](https://github.com/veripublica/epub-test-books/issues/205)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine element's toc attribute names the content document. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The `toc` attribute must reference the item that describes the NCX.

## Question

The `spine` element's `toc` names the content document. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> item that describes the NCX must be referenced by the spine toc attribute.

## Expected result

Invalid. The `toc` attribute must reference the item that describes the NCX.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i toc-not-ncx.epub -u --advisory` | ERROR OPF-050, USAGE ADV-010; INVALID | `toc-not-ncx.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck toc-not-ncx.epub -u` | ERROR OPF-050, ERROR CHK-008; INVALID | `toc-not-ncx.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

epubcheck also gives CHK-008, a note that it skipped other checks on that item.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, `toc` becomes `content`.

## History

- 2026-11-09: First version.
