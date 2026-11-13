# An itemref without idref

- Book: `itemref-no-idref.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-itemref-elem/itemref-no-idref/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#50](https://github.com/veripublica/epub-test-books/issues/50)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine has one extra itemref with no idref attribute. The other itemrefs are unchanged. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. This `itemref` references nothing.

## Question

The spine has one extra `itemref` with no `idref` attribute. The template's two itemrefs stay, so every document is still in the spine. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-itemref-elem`](https://www.w3.org/TR/epub-33/#sec-itemref-elem):

> Each itemref element MUST reference the ID [xml] of an item in the manifest via the IDREF [xml] in its idref attribute.

## Expected result

Invalid. This `itemref` references nothing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i itemref-no-idref.epub -u --advisory` | ERROR RSC-005; INVALID | `itemref-no-idref.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-no-idref.epub -u` | ERROR RSC-005; INVALID | `itemref-no-idref.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<itemref/>` is added at the end of the spine.

## History

- 2026-11-09: First version.
