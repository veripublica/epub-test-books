# A file URL as a manifest `href`

- Book: `file-url-item-href.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-file-urls/file-url-item-href/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#144](https://github.com/veripublica/epub-test-books/issues/144)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A manifest item has a file URL as its href. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. File URLs are not allowed.

## Question

A manifest item's `href` is a file URL. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-file-urls`](https://www.w3.org/TR/epub-33/#sec-file-urls):

> EPUB creators MUST NOT use file URLs in EPUB publications.

## Expected result

Invalid. File URLs are not allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i file-url-item-href.epub -u --advisory` | ERROR RSC-030, ERROR RSC-006; INVALID | `file-url-item-href.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck file-url-item-href.epub -u` | ERROR RSC-030, ERROR RSC-006, USAGE OPF-097; INVALID | `file-url-item-href.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

RSC-006 comes from the same URL: the tools also treat it as a remote resource.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, an `item` with a `file:` URL is added.

## History

- 2026-11-09: First version.
