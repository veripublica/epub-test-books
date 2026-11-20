# `<bdo dir="auto">`

- Book: `bdo-dir-auto.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/bdo-dir-auto/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28); parked on 2026-11-12 while both verifiers missed it, shipped after epubveri reports it
- Issue: [#618](https://github.com/veripublica/epub-test-books/issues/618)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The paragraph of content.xhtml is wrapped in <bdo dir="auto">. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. auto is a keyword of dir, but HTML says it must not be specified on bdo.

## Question

The paragraph of `content.xhtml` is wrapped in `<bdo dir="auto">`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-bdo-element`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element) (4.5.25 The bdo element; checked 2026-11-12):

> Authors must specify the dir attribute on this element, with the value ltr to specify a left-to-right override and with the value rtl to specify a right-to-left override. The auto value must not be specified.

## Expected result

Invalid. `auto` is a keyword of `dir`, but HTML says it must not be specified on `bdo`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i bdo-dir-auto.epub -u --advisory` | ERROR RSC-005; INVALID | `bdo-dir-auto.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck bdo-dir-auto.epub -u` | no findings; VALID | `bdo-dir-auto.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1769](https://github.com/w3c/epubcheck/issues/1769).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the paragraph's text is wrapped in `<bdo dir="auto">`.

## History

- 2026-11-12: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
