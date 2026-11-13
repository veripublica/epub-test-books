# An RDFa prefix attribute with no colon

- Book: `rdfa-prefix-no-colon.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-no-colon/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with prefix="dc http://purl.org/dc/terms/", with no colon after dc, and a p inside with property="dc:title". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. RDFa's prefix attribute takes pairs of the form NCName ':' ' '+ IRI, and here the colon is missing.

## Question

`content.xhtml` has `prefix="dc http://purl.org/dc/terms/"`, with no colon. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> The [html-rdfa] specification defines a set of attributes that EPUB creators MAY use in XHTML content documents to semantically enrich the content. The use of these attributes MUST conform to the requirements defined in [html-rdfa].

RDFa Core 1.1, [`s_syntax`](https://www.w3.org/TR/rdfa-core/#s_syntax) (5. Attributes and Syntax; W3C Recommendation):

> prefix a white space separated list of prefix-name IRI pairs of the form NCName ':' ' '+ xsd:anyURI

## Expected result

Invalid. RDFa's prefix attribute takes pairs of the form NCName ':' ' '+ IRI, and here the colon is missing.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i rdfa-prefix-no-colon.epub -u --advisory` | no findings; VALID | `rdfa-prefix-no-colon.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck rdfa-prefix-no-colon.epub -u` | ERROR RSC-005; INVALID | `rdfa-prefix-no-colon.epubcheck-5.4.0.txt` |

epubcheck agrees with the expected result. epubveri does not: it gives no finding.

- **epubveri: missed.** epubveri issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div prefix="dc http://purl.org/dc/terms/"><p property="dc:title">A test book.</p></div>`.

## History

- 2026-11-13: First version.
