# `rendition:align-x-center` on a spine item (valid)

- Book: `align-x-center-itemref.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/align-x-center/align-x-center-itemref/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#289](https://github.com/veripublica/epub-test-books/issues/289)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's itemref has rendition:align-x-center. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is the one place the property may be used.

## Question

The content document's `itemref` has `rendition:align-x-center`. Does a validator accept it?

## Clause

EPUB 3.3, [`align-x-center`](https://www.w3.org/TR/epub-33/#align-x-center):

> The property MUST NOT be set globally for all EPUB content documents (i.e., in a meta element without a refines attribute). It is only available as a spine override for individual EPUB content documents via the itemref element's properties attribute.

## Expected result

Valid. This is the one place the property may be used.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i align-x-center-itemref.epub -u --advisory` | WARNING OPF-086; VALID | `align-x-center-itemref.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck align-x-center-itemref.epub -u` | WARNING OPF-086; VALID | `align-x-center-itemref.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-086 says `rendition:align-x-center` is deprecated. EPUB 3.3 does not deprecate it; it says only that the property "is expected to be deprecated". The EPUB 3.4 draft deprecates it (change log, 18 December 2025), which is where the warning comes from. A warning does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, the content document's `itemref` gets `properties="rendition:align-x-center"`.

## History

- 2026-11-11: First version.
