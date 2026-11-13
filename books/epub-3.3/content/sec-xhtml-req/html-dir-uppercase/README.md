# `dir="RTL"` on `html` (valid)

- Book: `html-dir-uppercase.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-dir-uppercase/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#421](https://github.com/veripublica/epub-test-books/issues/421)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The html element of content.xhtml has dir="RTL". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. dir is an enumerated attribute, and its value only has to be an ASCII case-insensitive match for a keyword, so RTL is rtl.

## Question

The `html` element of `content.xhtml` has `dir="RTL"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-dir-attribute`](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) (3.2.6.4 The dir attribute; checked 2026-11-12):

> The dir attribute is an enumerated attribute with the following keywords and states:

HTML Living Standard, [`keywords-and-enumerated-attributes`](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#keywords-and-enumerated-attributes) (2.3.3 Keywords and enumerated attributes; checked 2026-11-12):

> For authoring conformance purposes, if an enumerated attribute is specified, the attribute's value must be one of: An ASCII case-insensitive match for one of the conforming keywords for that attribute, with no leading or trailing whitespace.The empty string and the attribute must have an empty value default defined.

## Expected result

Valid. `dir` is an enumerated attribute, and its value only has to be an ASCII case-insensitive match for a keyword, so `RTL` is `rtl`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i html-dir-uppercase.epub -u --advisory` | no findings; VALID | `html-dir-uppercase.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck html-dir-uppercase.epub -u` | no findings; VALID | `html-dir-uppercase.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `html` gets `dir="RTL"`.

## History

- 2026-11-12: First version.
