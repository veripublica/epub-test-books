# Every `itemref` non-linear

- Book: `no-primary-itemref.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/no-primary-itemref/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#202](https://github.com/veripublica/epub-test-books/issues/202)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Every itemref in the spine has linear="no". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. At least one must be primary.

## Question

Every `itemref` in the spine has `linear="no"`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> At least one itemref in spine must be declared primary.

## Expected result

Invalid. At least one must be primary.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i no-primary-itemref.epub -u --advisory` | ERROR OPF-033; INVALID | `no-primary-itemref.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck no-primary-itemref.epub -u` | ERROR OPF-033; INVALID | `no-primary-itemref.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, every `itemref` gets `linear="no"`.

## History

- 2026-11-09: First version.
