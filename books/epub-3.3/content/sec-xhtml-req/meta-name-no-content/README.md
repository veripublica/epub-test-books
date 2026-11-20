# A `meta` with `name` and no `content`

- Book: `meta-name-no-content.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/meta-name-no-content/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed
- Asked for by: epubveri, after MobileRead 374286 #394 (veripublica/epubveri#147)
- Issue: [#690](https://github.com/veripublica/epub-test-books/issues/690)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has <meta name="author"/> in its head. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A meta with name must also have content.

## Question

`content.xhtml` has `<meta name="author"/>` in its head. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-meta-element`](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) (4.2.5 The meta element; checked 2026-11-21):

> Exactly one of the name, http-equiv, charset, and itemprop attributes must be specified. If either name, http-equiv, or itemprop is specified, then the content attribute must also be specified. Otherwise, it must be omitted.

## Expected result

Invalid. HTML says that a `meta` with `name` must also have `content`. This one has none.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i meta-name-no-content.epub -u --advisory` | no findings; VALID | `meta-name-no-content.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-name-no-content.epub -u` | ERROR RSC-005; INVALID | `meta-name-no-content.epubcheck-5.4.0.txt` |

epubcheck agrees with the expected result. epubveri does not: it gives no finding.

- **epubveri: missed.** epubveri issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<meta name="author"/>` in its head.

## History

- 2026-11-21: First version.
