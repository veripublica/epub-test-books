# `rendition:align-x-center` set globally

- Book: `align-x-center-global.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/align-x-center/align-x-center-global/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#290](https://github.com/veripublica/epub-test-books/issues/290)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package has a meta element with property rendition:align-x-center and the value true, with no refines attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The property must not be set globally in a `meta` element without `refines`.

## Question

The package has `<meta property="rendition:align-x-center">true</meta>`, with no `refines`. Does a validator reject it?

## Clause

EPUB 3.3, [`align-x-center`](https://www.w3.org/TR/epub-33/#align-x-center):

> The property MUST NOT be set globally for all EPUB content documents (i.e., in a meta element without a refines attribute). It is only available as a spine override for individual EPUB content documents via the itemref element's properties attribute.

## Expected result

Invalid. The property must not be set globally in a `meta` element without `refines`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i align-x-center-global.epub -u --advisory` | ERROR OPF-027; INVALID | `align-x-center-global.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck align-x-center-global.epub -u` | ERROR OPF-027; INVALID | `align-x-center-global.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Both report OPF-027, an undefined property: neither knows `rendition:align-x-center` as a metadata property, since the rendering vocabulary defines it only as a spine override. The message names the vocabulary, not this clause, and the verdict is the same.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:align-x-center">true</meta>` is added to the metadata.

## History

- 2026-11-11: First version.
