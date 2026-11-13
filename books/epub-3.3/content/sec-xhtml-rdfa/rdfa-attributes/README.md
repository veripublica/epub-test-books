# RDFa attributes (valid)

- Book: `rdfa-attributes.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/rdfa-attributes/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with vocab="https://schema.org/" and typeof="Book", and a p inside with property="name". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. RDFa attributes may be used, and these follow RDFa.

## Question

`content.xhtml` has RDFa `vocab`, `typeof` and `property` attributes. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> The [html-rdfa] specification defines a set of attributes that EPUB creators MAY use in XHTML content documents to semantically enrich the content. The use of these attributes MUST conform to the requirements defined in [html-rdfa].

## Expected result

Valid. RDFa attributes may be used, and these follow RDFa.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i rdfa-attributes.epub -u --advisory` | no findings; VALID | `rdfa-attributes.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck rdfa-attributes.epub -u` | no findings; VALID | `rdfa-attributes.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div vocab="https://schema.org/" typeof="Book"><p property="name">A test book.</p></div>`.

## History

- 2026-11-13: First version.
