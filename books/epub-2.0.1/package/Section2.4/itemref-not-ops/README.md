# A plain text file in the spine

- Book: `itemref-not-ops.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/itemref-not-ops/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#200](https://github.com/veripublica/epub-test-books/issues/200)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A plain text file with no fallback is in the spine. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The item is not an OPS Content Document and has no fallback chain to one.

## Question

A plain text file with no fallback is in the spine. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> Each itemref in spine must not reference media types other than OPS Content Documents (or documents whose fallback chain includes an OPS Content Document).

## Expected result

Invalid. The item is not an OPS Content Document and has no fallback chain to one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i itemref-not-ops.epub -u --advisory` | ERROR OPF-043; INVALID | `itemref-not-ops.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-not-ops.epub -u` | ERROR OPF-043; INVALID | `itemref-not-ops.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.txt` is added to the manifest as `text/plain` and to the end of the spine.

## History

- 2026-11-09: First version.
