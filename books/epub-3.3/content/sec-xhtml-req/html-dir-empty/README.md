# An empty `dir` on `html`

- Book: `html-dir-empty.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-dir-empty/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The html element of content.xhtml has dir="". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An empty value is conforming only for an attribute with an empty value default, and dir has none.

## Question

The `html` element of `content.xhtml` has `dir=""`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`keywords-and-enumerated-attributes`](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#keywords-and-enumerated-attributes) (2.3.3 Keywords and enumerated attributes; checked 2026-11-12):

> For authoring conformance purposes, if an enumerated attribute is specified, the attribute's value must be one of: An ASCII case-insensitive match for one of the conforming keywords for that attribute, with no leading or trailing whitespace.The empty string and the attribute must have an empty value default defined.

HTML Living Standard, [`the-dir-attribute`](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) (3.2.6.4 The dir attribute; checked 2026-11-12):

> The attribute's missing value default and invalid value default are both the Undefined state.

## Expected result

Invalid. An empty value is conforming only for an attribute with an empty value default, and `dir` has none.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i html-dir-empty.epub -u --advisory` | ERROR RSC-005; INVALID | `html-dir-empty.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck html-dir-empty.epub -u` | ERROR RSC-005; INVALID | `html-dir-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `html` gets `dir=""`.

## History

- 2026-11-12: First version.
