# A manifest item without `id`

- Book: `item-no-id.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3/item-no-id/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#189](https://github.com/veripublica/epub-test-books/issues/189)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One extra manifest item has no id attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

One extra manifest item has no `id`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3):

> Each item element contained within a manifest element must have the attributes id, href (a URI; if relative, the URI is interpreted as relative to the OPF Package Document file containing the reference), and media-type

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i item-no-id.epub -u --advisory` | ERROR RSC-005, USAGE OPF-003, USAGE ADV-010; INVALID | `item-no-id.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck item-no-id.epub -u` | ERROR RSC-005, USAGE OPF-003; INVALID | `item-no-id.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE OPF-003 follows: the file has no usable manifest entry.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

`OEBPS/extra.xhtml` is added, and an `item` without `id` is added to the manifest.

## History

- 2026-11-09: First version.
