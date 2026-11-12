# A data URL as a manifest `href`

- Book: `data-url-item-href.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-data-urls/data-url-item-href/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#138](https://github.com/veripublica/epub-test-books/issues/138)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A manifest item has a data URL as its href. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Data URLs are not allowed in manifest `href` attributes.

## Question

A manifest item's `href` is a data URL. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-data-urls`](https://www.w3.org/TR/epub-33/#sec-data-urls):

> EPUB creators MUST NOT use data URLs in the following scenarios where they can result in a top-level content document or top-level browsing context [html]:

> in href attributes in the package document — this applies both to manifest item elements and metadata link elements;

## Expected result

Invalid. Data URLs are not allowed in manifest `href` attributes.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i data-url-item-href.epub -u --advisory` | ERROR RSC-029, USAGE OPF-097; INVALID | `data-url-item-href.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck data-url-item-href.epub -u` | ERROR RSC-029, USAGE OPF-097; INVALID | `data-url-item-href.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, an `item` with `href="data:text/plain,hello"` is added.

## History

- 2026-11-09: First version.
