# An RDFa prefix attribute with two spaces after the colon (valid)

- Book: `rdfa-prefix-two-spaces.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-two-spaces/build.py`
- Origin: built here, suggested by epubveri
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: epubveri, after its 0.42.0 fixes
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with prefix="dc:  http://purl.org/dc/terms/", with two spaces after the colon, and a p inside with property="dc:title". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. RDFa's prefix attribute takes pairs of the form NCName ':' ' '+ IRI, so one or more spaces may follow the colon.

## Question

`content.xhtml` has `prefix="dc:  http://purl.org/dc/terms/"`, with two spaces after the colon. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> The [html-rdfa] specification defines a set of attributes that EPUB creators MAY use in XHTML content documents to semantically enrich the content. The use of these attributes MUST conform to the requirements defined in [html-rdfa].

RDFa Core 1.1, [`s_syntax`](https://www.w3.org/TR/rdfa-core/#s_syntax) (5. Attributes and Syntax; W3C Recommendation):

> prefix a white space separated list of prefix-name IRI pairs of the form NCName ':' ' '+ xsd:anyURI

## Expected result

Valid. RDFa's prefix attribute takes pairs of the form NCName ':' ' '+ IRI, so one or more spaces may follow the colon.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i rdfa-prefix-two-spaces.epub -u --advisory` | no findings; VALID | `rdfa-prefix-two-spaces.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck rdfa-prefix-two-spaces.epub -u` | ERROR RSC-005; INVALID | `rdfa-prefix-two-spaces.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports the prefix value as a schema error (RSC-005), as its pattern allows exactly one space after the colon.

- **epubcheck: wrong error.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div prefix="dc:  http://purl.org/dc/terms/"><p property="dc:title">A test book.</p></div>`.

## History

- 2026-11-13: First version.
