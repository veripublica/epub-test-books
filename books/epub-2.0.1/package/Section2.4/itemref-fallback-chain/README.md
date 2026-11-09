# A spine item with a fallback to XHTML (valid)

- Book: `itemref-fallback-chain.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/itemref-fallback-chain/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#201](https://github.com/veripublica/epub-test-books/issues/201)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A plain text file in the spine has an XHTML document as its fallback. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The fallback chain includes an OPS Content Document.

## Question

A plain text file in the spine has an XHTML document as its `fallback`. Does a validator accept it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> Each itemref in spine must not reference media types other than OPS Content Documents (or documents whose fallback chain includes an OPS Content Document).

## Expected result

Valid. The fallback chain includes an OPS Content Document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i itemref-fallback-chain.epub -u --advisory` | no findings; VALID | `itemref-fallback-chain.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-fallback-chain.epub -u` | no findings; VALID | `itemref-fallback-chain.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.txt` and `OEBPS/extra2.xhtml` are added, the text file's `fallback` names the document, and the text file is added to the end of the spine.

## History

- 2026-11-09: First version.
