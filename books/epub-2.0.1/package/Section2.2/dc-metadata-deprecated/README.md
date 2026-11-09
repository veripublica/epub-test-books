# The deprecated `dc-metadata` form (valid)

- Book: `dc-metadata-deprecated.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.2/dc-metadata-deprecated/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#227](https://github.com/veripublica/epub-test-books/issues/227)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata uses the deprecated dc-metadata and x-metadata elements. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. These elements are deprecated, and the specification keeps them.

## Question

The metadata uses the deprecated `dc-metadata` and `x-metadata` elements. Does a validator accept it?

## Clause

OPF 2.0.1, [`Section2.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2):

> It may contain Dublin Core metadata elements directly or within a (now deprecated) dc-metadata sub-element

## Expected result

Valid. These elements are deprecated, and the specification keeps them.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i dc-metadata-deprecated.epub -u --advisory` | no findings; VALID | `dc-metadata-deprecated.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck dc-metadata-deprecated.epub -u` | ERROR OPF-049, ERROR OPF-049; INVALID | `dc-metadata-deprecated.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: epubcheck reports `dc-metadata` and `x-metadata` as manifest items it cannot find (OPF-049).

- **epubcheck: wrong error.** [w3c/epubcheck#1761](https://github.com/w3c/epubcheck/issues/1761).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, the Dublin Core elements move into `dc-metadata` and the `meta` elements into `x-metadata`.

## History

- 2026-11-09: First version.
