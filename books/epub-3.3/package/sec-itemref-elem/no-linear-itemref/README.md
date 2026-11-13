# Every `itemref` non-linear

- Book: `no-linear-itemref.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-itemref-elem/no-linear-itemref/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#85](https://github.com/veripublica/epub-test-books/issues/85)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Every itemref in the spine has linear="no". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. No itemref is linear. Both documents can still be reached from the navigation document.

## Question

Every `itemref` in the spine has `linear="no"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-itemref-elem`](https://www.w3.org/TR/epub-33/#sec-itemref-elem):

> The spine MUST contain at least one linear itemref element.

## Expected result

Invalid. No itemref is linear. Both documents can still be reached from the navigation document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i no-linear-itemref.epub -u --advisory` | ERROR OPF-033; INVALID | `no-linear-itemref.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck no-linear-itemref.epub -u` | ERROR OPF-033; INVALID | `no-linear-itemref.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, every `itemref` gets `linear="no"`.

## History

- 2026-11-09: First version.
