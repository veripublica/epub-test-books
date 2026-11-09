# A manifest item that is its own fallback

- Book: `fallback-self.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-manifest-fallbacks/fallback-self/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#130](https://github.com/veripublica/epub-test-books/issues/130)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A manifest item names itself as fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. This is a self-reference.

## Question

A manifest item names itself as `fallback`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-manifest-fallbacks`](https://www.w3.org/TR/epub-33/#sec-manifest-fallbacks):

> Regardless of the type of manifest fallback specified, fallback chains MUST NOT contain self-references or circular references to item elements in the chain.

## Expected result

Invalid. This is a self-reference.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i fallback-self.epub -u --advisory` | ERROR OPF-045, USAGE OPF-097; INVALID | `fallback-self.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck fallback-self.epub -u` | ERROR OPF-045, USAGE OPF-097; INVALID | `fallback-self.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP is added to the manifest with its own `id` as `fallback`.

## History

- 2026-11-09: First version.
