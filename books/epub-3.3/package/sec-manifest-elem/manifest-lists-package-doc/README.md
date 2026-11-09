# The manifest lists the package document

- Book: `manifest-lists-package-doc.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-manifest-elem/manifest-lists-package-doc/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#69](https://github.com/veripublica/epub-test-books/issues/69)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest has an item for the package document itself. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The package document must not be listed.

## Question

The manifest has an item for the package document itself. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-manifest-elem`](https://www.w3.org/TR/epub-33/#sec-manifest-elem):

> the manifest MUST NOT specify an item element for it (i.e., a self-reference serves no purpose).

## Expected result

Invalid. The package document must not be listed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i manifest-lists-package-doc.epub -u --advisory` | ERROR OPF-099, USAGE OPF-097; INVALID | `manifest-lists-package-doc.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck manifest-lists-package-doc.epub -u` | ERROR OPF-099, USAGE OPF-097; INVALID | `manifest-lists-package-doc.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, an `item` for `package.opf` is added to the manifest.

## History

- 2026-11-09: First version.
