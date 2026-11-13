# An `itemref` naming no item

- Book: `itemref-unknown.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-itemref-elem/itemref-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#82](https://github.com/veripublica/epub-test-books/issues/82)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One extra itemref has an idref that no manifest item has. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The reference resolves to nothing.

## Question

One extra `itemref` has an `idref` that no manifest item has. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-itemref-elem`](https://www.w3.org/TR/epub-33/#sec-itemref-elem):

> Each itemref element MUST reference the ID [xml] of an item in the manifest via the IDREF [xml] in its idref attribute.

## Expected result

Invalid. The reference resolves to nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i itemref-unknown.epub -u --advisory` | ERROR RSC-005, ERROR OPF-049; INVALID | `itemref-unknown.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-unknown.epub -u` | ERROR OPF-049, ERROR RSC-005; INVALID | `itemref-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<itemref idref="nope"/>` is added at the end of the spine.

## History

- 2026-11-09: First version.
