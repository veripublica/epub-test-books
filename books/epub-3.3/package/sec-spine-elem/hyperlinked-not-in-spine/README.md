# A linked document not in the spine

- Book: `hyperlinked-not-in-spine.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-spine-elem/hyperlinked-not-in-spine/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#80](https://github.com/veripublica/epub-test-books/issues/80)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document links to another XHTML document that is in the manifest but not in the spine. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The linked document must be in the spine.

## Question

The content document links to another XHTML document that is in the manifest but not in the spine. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-spine-elem`](https://www.w3.org/TR/epub-33/#sec-spine-elem):

> EPUB creators MUST list in the spine all EPUB and foreign content documents that are hyperlinked to from publication resources in the spine

## Expected result

Invalid. The linked document must be in the spine.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i hyperlinked-not-in-spine.epub -u --advisory` | ERROR RSC-011, USAGE OPF-097; INVALID | `hyperlinked-not-in-spine.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck hyperlinked-not-in-spine.epub -u` | USAGE OPF-097, ERROR RSC-011; INVALID | `hyperlinked-not-in-spine.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.xhtml` is added to the manifest only, and `content.xhtml` links to it.

## History

- 2026-11-09: First version.
