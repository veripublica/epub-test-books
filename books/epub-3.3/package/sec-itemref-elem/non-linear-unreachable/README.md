# Non-linear content nothing links to

- Book: `non-linear-unreachable.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-itemref-elem/non-linear-unreachable/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#86](https://github.com/veripublica/epub-test-books/issues/86)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A non-linear document is in the spine, and no link leads to it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Nothing gives access to the document.

## Question

A non-linear document is in the spine, and no link leads to it. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-itemref-elem`](https://www.w3.org/TR/epub-33/#sec-itemref-elem):

> EPUB creators MUST provide a means of accessing all non-linear content (e.g., hyperlinks in the content or from the EPUB navigation document).

## Expected result

Invalid. Nothing gives access to the document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i non-linear-unreachable.epub -u --advisory` | ERROR OPF-096; INVALID | `non-linear-unreachable.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck non-linear-unreachable.epub -u` | ERROR OPF-096; INVALID | `non-linear-unreachable.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.xhtml` is added to the manifest, and `<itemref idref="extra" linear="no"/>` is added at the end of the spine.

## History

- 2026-11-09: First version.
