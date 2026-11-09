# A stylesheet in the spine

- Book: `itemref-not-content.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-itemref-elem/itemref-not-content/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#84](https://github.com/veripublica/epub-test-books/issues/84)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A CSS file with no fallback is in the spine. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A stylesheet is neither, and it has no fallback.

## Question

A CSS file with no fallback is in the spine. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-itemref-elem`](https://www.w3.org/TR/epub-33/#sec-itemref-elem):

> Each referenced manifest item MUST be either a) an EPUB content document or b) a foreign content document that includes an EPUB content document in its manifest fallback chain.

## Expected result

Invalid. A stylesheet is neither, and it has no fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i itemref-not-content.epub -u --advisory` | ERROR OPF-043; INVALID | `itemref-not-content.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-not-content.epub -u` | ERROR OPF-043; INVALID | `itemref-not-content.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.css` is added to the manifest, and an `itemref` for it is added at the end of the spine.

## History

- 2026-11-09: First version.
