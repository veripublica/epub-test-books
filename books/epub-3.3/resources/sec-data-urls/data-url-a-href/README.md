# A data URL as a hyperlink

- Book: `data-url-a-href.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-data-urls/data-url-a-href/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#140](https://github.com/veripublica/epub-test-books/issues/140)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An a element in the content document has a data URL as its href. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Data URLs are not allowed on `a` elements outside an `iframe`.

## Question

An `a` element in the content document has a data URL as its `href`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-data-urls`](https://www.w3.org/TR/epub-33/#sec-data-urls):

> EPUB creators MUST NOT use data URLs in the following scenarios where they can result in a top-level content document or top-level browsing context [html]:

> in the href attribute on [html] or [svg] a elements, except when inside an iframe element [html];

## Expected result

Invalid. Data URLs are not allowed on `a` elements outside an `iframe`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i data-url-a-href.epub -u --advisory` | ERROR RSC-029, ERROR RSC-011; INVALID | `data-url-a-href.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck data-url-a-href.epub -u` | ERROR RSC-029, ERROR RSC-011; INVALID | `data-url-a-href.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

RSC-011 follows from the same link: its target is not in the spine.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, an `a` with `href="data:text/html,hello"` is added.

## History

- 2026-11-09: First version.
