# `<bdo>` with no `dir`

- Book: `bdo-no-dir.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/bdo-no-dir/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#425](https://github.com/veripublica/epub-test-books/issues/425)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The paragraph of content.xhtml is wrapped in <bdo>. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. bdo must have a dir attribute.

## Question

The paragraph of `content.xhtml` is wrapped in `<bdo>`. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-bdo-element`](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element) (4.5.25 The bdo element; checked 2026-11-12):

> Authors must specify the dir attribute on this element, with the value ltr to specify a left-to-right override and with the value rtl to specify a right-to-left override. The auto value must not be specified.

## Expected result

Invalid. `bdo` must have a `dir` attribute.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i bdo-no-dir.epub -u --advisory` | ERROR RSC-005; INVALID | `bdo-no-dir.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck bdo-no-dir.epub -u` | ERROR RSC-005; INVALID | `bdo-no-dir.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the paragraph's text is wrapped in `<bdo>`.

## History

- 2026-11-12: First version.
