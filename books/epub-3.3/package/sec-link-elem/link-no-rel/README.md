# A link element without rel

- Book: `link-no-rel.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-link-elem/link-no-rel/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#215](https://github.com/veripublica/epub-test-books/issues/215)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has a link element to an external record, with no rel attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

The metadata has a `link` element to an external record, with no `rel` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-link-elem`](https://www.w3.org/TR/epub-33/#sec-link-elem):

> The REQUIRED rel attribute takes a space-separated list of property values that establish the relationship the linked resource has with the EPUB publication.

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i link-no-rel.epub -u --advisory` | ERROR RSC-005; INVALID | `link-no-rel.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck link-no-rel.epub -u` | ERROR RSC-005; INVALID | `link-no-rel.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `link` with `href` and `media-type` and no `rel` is added to the metadata.

## History

- 2026-11-09: First version.
