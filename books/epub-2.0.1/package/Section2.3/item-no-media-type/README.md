# A manifest item without `media-type`

- Book: `item-no-media-type.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3/item-no-media-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#191](https://github.com/veripublica/epub-test-books/issues/191)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One extra manifest item has no media-type attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

One extra manifest item has no `media-type`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3):

> Each item element contained within a manifest element must have the attributes id, href (a URI; if relative, the URI is interpreted as relative to the OPF Package Document file containing the reference), and media-type

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i item-no-media-type.epub -u --advisory` | ERROR RSC-005, USAGE ADV-010; INVALID | `item-no-media-type.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck item-no-media-type.epub -u` | ERROR RSC-005; INVALID | `item-no-media-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

`OEBPS/extra.xhtml` is added, and an `item` without `media-type` is added to the manifest.

## History

- 2026-11-09: First version.
