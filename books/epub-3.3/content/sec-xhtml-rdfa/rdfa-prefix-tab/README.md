# An RDFa prefix attribute with a tab after the colon

- Book: `rdfa-prefix-tab.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/rdfa-prefix-tab/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after its 0.42.0 fixes
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with prefix="dc:&#9;http://purl.org/dc/terms/", a tab written as a character reference after the colon, and a p inside with property="dc:title". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only spaces (' '+) may follow the colon. A tab is white space between pairs, not between a prefix and its IRI.

## Question

`content.xhtml` has `prefix="dc:&#9;http://purl.org/dc/terms/"`, a tab after the colon. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> The [html-rdfa] specification defines a set of attributes that EPUB creators MAY use in XHTML content documents to semantically enrich the content. The use of these attributes MUST conform to the requirements defined in [html-rdfa].

RDFa Core 1.1, [`s_syntax`](https://www.w3.org/TR/rdfa-core/#s_syntax) (5. Attributes and Syntax; W3C Recommendation):

> prefix a white space separated list of prefix-name IRI pairs of the form NCName ':' ' '+ xsd:anyURI

RDFa Core 1.1, [`white_space`](https://www.w3.org/TR/rdfa-core/#white_space) (5.2 White space within attribute values; W3C Recommendation):

> This specification defines white space as: whitespace ::= (#x20 | #x9 | #xD | #xA)+

## Expected result

Invalid. Only spaces (' '+) may follow the colon. A tab is white space between pairs, not between a prefix and its IRI.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i rdfa-prefix-tab.epub -u --advisory` | ERROR RSC-005; INVALID | `rdfa-prefix-tab.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck rdfa-prefix-tab.epub -u` | ERROR RSC-005; INVALID | `rdfa-prefix-tab.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div prefix="dc:&#9;http://purl.org/dc/terms/"><p property="dc:title">A test book.</p></div>`. The tab is the character reference `&#9;`: a literal tab would become a space under XML attribute-value normalization.

## History

- 2026-11-13: First version.
