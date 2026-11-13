# `hreflang` with an underscore

- Book: `link-hreflang-malformed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-link-elem/link-hreflang-malformed/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#68](https://github.com/veripublica/epub-test-books/issues/68)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A link element has the hreflang en_US. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `en_US` is not a well-formed BCP 47 tag.

## Question

A `link` element's `hreflang` is `en_US`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-link-elem`](https://www.w3.org/TR/epub-33/#sec-link-elem):

> The value MUST be a well-formed language tag [bcp47].

## Expected result

Invalid. `en_US` is not a well-formed BCP 47 tag.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i link-hreflang-malformed.epub -u --advisory` | ERROR OPF-092, ERROR RSC-005; INVALID | `link-hreflang-malformed.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck link-hreflang-malformed.epub -u` | ERROR RSC-005, ERROR OPF-092; INVALID | `link-hreflang-malformed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `link` with `hreflang="en_US"` is added to the metadata.

## History

- 2026-11-09: First version.
