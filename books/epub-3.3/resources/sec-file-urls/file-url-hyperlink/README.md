# A file URL as a hyperlink

- Book: `file-url-hyperlink.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-file-urls/file-url-hyperlink/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#143](https://github.com/veripublica/epub-test-books/issues/143)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An a element in the content document has a file URL as its href. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. File URLs are not allowed.

## Question

An `a` element in the content document has a file URL as its `href`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-file-urls`](https://www.w3.org/TR/epub-33/#sec-file-urls):

> EPUB creators MUST NOT use file URLs in EPUB publications.

## Expected result

Invalid. File URLs are not allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i file-url-hyperlink.epub -u --advisory` | ERROR RSC-030; INVALID | `file-url-hyperlink.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck file-url-hyperlink.epub -u` | ERROR RSC-030; INVALID | `file-url-hyperlink.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `a` with a `file:` URL is added.

## History

- 2026-11-09: First version.
