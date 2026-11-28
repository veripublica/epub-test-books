# `dir=" rtl"` on `html`, with a leading space

- Book: `html-dir-padded.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-dir-padded/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28); parked on 2026-11-12 while both verifiers missed it, shipped after epubveri reports it
- Issue: [#619](https://github.com/veripublica/epub-test-books/issues/619)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The html element of content.xhtml has dir=" rtl", with a space before rtl. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. dir is an enumerated attribute, and its value must match a keyword with no leading or trailing whitespace.

## Question

The `html` element of `content.xhtml` has `dir=" rtl"`, with a space before `rtl`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-dir-attribute`](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) (3.2.6.4 The dir attribute; checked 2026-11-12):

> The dir attribute is an enumerated attribute with the following keywords and states:

HTML Living Standard, [`keywords-and-enumerated-attributes`](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#keywords-and-enumerated-attributes) (2.3.3 Keywords and enumerated attributes; checked 2026-11-12):

> For authoring conformance purposes, if an enumerated attribute is specified, the attribute's value must be one of: An ASCII case-insensitive match for one of the conforming keywords for that attribute, with no leading or trailing whitespace.The empty string and the attribute must have an empty value default defined.

## Expected result

Invalid. `dir` is an enumerated attribute, and its value must match a keyword with no leading or trailing whitespace.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i html-dir-padded.epub -u --advisory` | ERROR RSC-005; INVALID | `html-dir-padded.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck html-dir-padded.epub -u` | no findings; VALID | `html-dir-padded.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1769](https://github.com/w3c/epubcheck/issues/1769).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `html` gets `dir=" rtl"`.

## History

- 2026-11-12: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
