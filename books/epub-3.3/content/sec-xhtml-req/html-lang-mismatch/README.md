# `lang` and `xml:lang` that differ

- Book: `html-lang-mismatch.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/html-lang-mismatch/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#178](https://github.com/veripublica/epub-test-books/issues/178)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p element has lang="en" and xml:lang="fr". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. HTML requires the two to have the same value.

## Question

A `p` element has `lang="en"` and `xml:lang="fr"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

## Expected result

Invalid. HTML requires the two to have the same value.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i html-lang-mismatch.epub -u --advisory` | ERROR RSC-005; INVALID | `html-lang-mismatch.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck html-lang-mismatch.epub -u` | ERROR RSC-005; INVALID | `html-lang-mismatch.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `p` with different `lang` and `xml:lang` is added.

## History

- 2026-11-09: First version.
