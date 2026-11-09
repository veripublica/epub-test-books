# A circular fallback chain

- Book: `fallback-chain-circular.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-manifest-fallbacks/fallback-chain-circular/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#129](https://github.com/veripublica/epub-test-books/issues/129)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two manifest items name each other as fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The chain is circular.

## Question

Two manifest items name each other as `fallback`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-manifest-fallbacks`](https://www.w3.org/TR/epub-33/#sec-manifest-fallbacks):

> Regardless of the type of manifest fallback specified, fallback chains MUST NOT contain self-references or circular references to item elements in the chain.

## Expected result

Invalid. The chain is circular.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i fallback-chain-circular.epub -u --advisory` | ERROR OPF-045, USAGE OPF-097, USAGE OPF-097; INVALID | `fallback-chain-circular.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck fallback-chain-circular.epub -u` | ERROR OPF-045, USAGE OPF-097, USAGE OPF-097; INVALID | `fallback-chain-circular.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and JPEG are added to the manifest, each with the other as its `fallback`. Nothing references them.

## History

- 2026-11-09: First version.
