# `rendition:align-x-center` in a `meta` element with `refines`

- Book: `align-x-center-refines.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/align-x-center/align-x-center-refines/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#291](https://github.com/veripublica/epub-test-books/issues/291)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package has a meta element with property rendition:align-x-center, the value true and refines="#content". It is not a global setting, but it is not a spine override either. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The property "is only available as a spine override" through the `itemref` element's `properties` attribute; a `meta` element is not that, with or without `refines`.

## Question

The package has `<meta property="rendition:align-x-center" refines="#content">true</meta>`. It is not a global setting, but it is not a spine override either. Does a validator reject it?

## Clause

EPUB 3.3, [`align-x-center`](https://www.w3.org/TR/epub-33/#align-x-center):

> The property MUST NOT be set globally for all EPUB content documents (i.e., in a meta element without a refines attribute). It is only available as a spine override for individual EPUB content documents via the itemref element's properties attribute.

## Expected result

Invalid. The property "is only available as a spine override" through the `itemref` element's `properties` attribute; a `meta` element is not that, with or without `refines`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i align-x-center-refines.epub -u --advisory` | ERROR OPF-027; INVALID | `align-x-center-refines.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck align-x-center-refines.epub -u` | ERROR OPF-027; INVALID | `align-x-center-refines.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report OPF-027, an undefined property, as for the global form: the rendering vocabulary defines `rendition:align-x-center` only as a spine override.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:align-x-center" refines="#content">true</meta>` is added to the metadata.

## History

- 2026-11-11: First version.
