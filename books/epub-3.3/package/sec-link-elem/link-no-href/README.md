# A link element without href

- Book: `link-no-href.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-link-elem/link-no-href/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#216](https://github.com/veripublica/epub-test-books/issues/216)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has a link element with rel and media-type, and no href attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

The metadata has a `link` element with `rel` and `media-type`, and no `href` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-link-elem`](https://www.w3.org/TR/epub-33/#sec-link-elem):

> The metadata element MAY contain zero or more link elements, each of which identifies the location of a publication resource or a linked resource in its REQUIRED href attribute.

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i link-no-href.epub -u --advisory` | ERROR RSC-005; INVALID | `link-no-href.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck link-no-href.epub -u` | ERROR RSC-005; INVALID | `link-no-href.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<link rel="record" media-type="application/xml"/>` is added to the metadata.

## History

- 2026-11-09: First version.
