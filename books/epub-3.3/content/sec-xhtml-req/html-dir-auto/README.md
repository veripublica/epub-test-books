# `dir="auto"` on `html` (valid)

- Book: `html-dir-auto.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-dir-auto/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The html element of content.xhtml has dir="auto". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. auto is a keyword of the dir attribute.

## Question

The `html` element of `content.xhtml` has `dir="auto"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-dir-attribute`](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) (3.2.6.4 The dir attribute; checked 2026-11-12):

> The dir attribute is an enumerated attribute with the following keywords and states:

## Expected result

Valid. `auto` is a keyword of the `dir` attribute.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i html-dir-auto.epub -u --advisory` | no findings; VALID | `html-dir-auto.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck html-dir-auto.epub -u` | no findings; VALID | `html-dir-auto.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `html` gets `dir="auto"`.

## History

- 2026-11-12: First version.
