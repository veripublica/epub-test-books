# An empty `spine`

- Book: `spine-empty.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/spine-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#197](https://github.com/veripublica/epub-test-books/issues/197)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine element has no itemref. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. One or more `itemref` elements are required.

## Question

The `spine` element has no `itemref`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> Following manifest, there must be one and only one spine element, which contains one or more itemref elements.

## Expected result

Invalid. One or more `itemref` elements are required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i spine-empty.epub -u --advisory` | ERROR RSC-005, ERROR RSC-011, ERROR RSC-011, USAGE ADV-010, USAGE ADV-010; INVALID | `spine-empty.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck spine-empty.epub -u` | ERROR RSC-005, ERROR RSC-011, ERROR RSC-011; INVALID | `spine-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

The RSC-011 errors follow: the documents the NCX links to are not in the spine.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, every `itemref` is removed.

## History

- 2026-11-09: First version.
