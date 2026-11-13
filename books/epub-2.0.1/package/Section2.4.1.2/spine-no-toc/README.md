# A spine without `toc`

- Book: `spine-no-toc.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/spine-no-toc/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#204](https://github.com/veripublica/epub-test-books/issues/204)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The NCX is in the manifest, and the spine has no toc attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The spine must reference the NCX item.

## Question

The NCX is in the manifest, and the `spine` has no `toc` attribute. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> item that describes the NCX must be referenced by the spine toc attribute.

## Expected result

Invalid. The spine must reference the NCX item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i spine-no-toc.epub -u --advisory` | ERROR RSC-005, USAGE ADV-010; INVALID | `spine-no-toc.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-no-toc.epub -u` | ERROR RSC-005; INVALID | `spine-no-toc.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, `toc` is removed from `spine`.

## History

- 2026-11-09: First version.
