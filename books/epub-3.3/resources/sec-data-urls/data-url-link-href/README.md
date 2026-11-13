# A data URL as a metadata link `href`

- Book: `data-url-link-href.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-data-urls/data-url-link-href/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#139](https://github.com/veripublica/epub-test-books/issues/139)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A metadata link element has a data URL as its href. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Data URLs are not allowed in metadata `link` `href` attributes.

## Question

A metadata `link` element's `href` is a data URL. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-data-urls`](https://www.w3.org/TR/epub-33/#sec-data-urls):

> EPUB creators MUST NOT use data URLs in the following scenarios where they can result in a top-level content document or top-level browsing context [html]:

> in href attributes in the package document — this applies both to manifest item elements and metadata link elements;

## Expected result

Invalid. Data URLs are not allowed in metadata `link` `href` attributes.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i data-url-link-href.epub -u --advisory` | ERROR RSC-029; INVALID | `data-url-link-href.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck data-url-link-href.epub -u` | ERROR RSC-029; INVALID | `data-url-link-href.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `link` with a data URL is added to the metadata.

## History

- 2026-11-09: First version.
