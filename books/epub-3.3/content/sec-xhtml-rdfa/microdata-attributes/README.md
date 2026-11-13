# Microdata attributes (valid)

- Book: `microdata-attributes.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/microdata-attributes/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with itemscope and itemtype="https://schema.org/Book", and a p inside with itemprop="name". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Microdata is natively supported in XHTML content documents.

## Question

`content.xhtml` has microdata `itemscope`, `itemtype` and `itemprop` attributes. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> EPUB creators can also specify microdata attributes [html] and linked data [json-ld11] in XHTML content documents as both are natively supported.

## Expected result

Valid. Microdata is natively supported in XHTML content documents.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i microdata-attributes.epub -u --advisory` | no findings; VALID | `microdata-attributes.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck microdata-attributes.epub -u` | no findings; VALID | `microdata-attributes.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div itemscope="" itemtype="https://schema.org/Book"><p itemprop="name">A test book.</p></div>`.

## History

- 2026-11-13: First version.
