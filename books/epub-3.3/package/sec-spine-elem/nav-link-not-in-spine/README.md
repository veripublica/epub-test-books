# A navigation entry for a document not in the spine

- Book: `nav-link-not-in-spine.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-spine-elem/nav-link-not-in-spine/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#81](https://github.com/veripublica/epub-test-books/issues/81)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The navigation document links to an XHTML document that is in the manifest but not in the spine. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The linked document must be in the spine.

## Question

The navigation document links to an XHTML document that is in the manifest but not in the spine. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-spine-elem`](https://www.w3.org/TR/epub-33/#sec-spine-elem):

> EPUB creators also MUST list in the spine all EPUB and foreign content documents hyperlinked to from the EPUB navigation document

## Expected result

Invalid. The linked document must be in the spine.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i nav-link-not-in-spine.epub -u --advisory` | ERROR RSC-011, USAGE OPF-097; INVALID | `nav-link-not-in-spine.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck nav-link-not-in-spine.epub -u` | USAGE OPF-097, ERROR RSC-011; INVALID | `nav-link-not-in-spine.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/extra.xhtml` is added to the manifest only, and `nav.xhtml` links to it.

## History

- 2026-11-09: First version.
