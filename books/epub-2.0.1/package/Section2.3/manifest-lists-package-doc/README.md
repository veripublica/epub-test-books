# The manifest lists the package document

- Book: `manifest-lists-package-doc.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3/manifest-lists-package-doc/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#188](https://github.com/veripublica/epub-test-books/issues/188)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest has an item for the package document itself. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The package document must not be listed.

## Question

The manifest has an item for the package document itself. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3):

> The manifest must not include item elements referring to the file or files that make up the OPF Package Document.

## Expected result

Invalid. The package document must not be listed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i manifest-lists-package-doc.epub -u --advisory` | ERROR OPF-099, USAGE ADV-010; INVALID | `manifest-lists-package-doc.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck manifest-lists-package-doc.epub -u` | ERROR OPF-099; INVALID | `manifest-lists-package-doc.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, an `item` for `package.opf` is added.

## History

- 2026-11-09: First version.
