# Two manifest URLs equal after parsing

- Book: `item-duplicate-after-parsing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-elem/item-duplicate-after-parsing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#70](https://github.com/veripublica/epub-test-books/issues/70)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two manifest items have the href values content.xhtml and ./content.xhtml. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Both strings parse to the same URL.

## Question

Two manifest items have the `href` values `content.xhtml` and `./content.xhtml`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-elem`](https://www.w3.org/TR/epub-33/#sec-item-elem):

> EPUB creators MUST ensure each URL is unique within the manifest scope after parsing.

## Expected result

Invalid. Both strings parse to the same URL.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i item-duplicate-after-parsing.epub -u --advisory` | ERROR OPF-074, USAGE OPF-097; INVALID | `item-duplicate-after-parsing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck item-duplicate-after-parsing.epub -u` | ERROR OPF-074, USAGE OPF-097; INVALID | `item-duplicate-after-parsing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, an `item` with `href="./content.xhtml"` is added to the manifest.

## History

- 2026-11-09: First version.
