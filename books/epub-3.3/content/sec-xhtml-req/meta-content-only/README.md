# A `meta` with `content` and no `name`, `http-equiv`, `charset` or `itemprop`

- Book: `meta-content-only.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/meta-content-only/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after MobileRead 374286 #394 (veripublica/epubveri#147)
- Issue: [#687](https://github.com/veripublica/epub-test-books/issues/687)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has <meta content="true"/> in its head. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A meta needs exactly one of name, http-equiv, charset and itemprop, and this one has none.

## Question

`content.xhtml` has `<meta content="true"/>` in its head. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-meta-element`](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) (4.2.5 The meta element; checked 2026-11-21):

> Exactly one of the name, http-equiv, charset, and itemprop attributes must be specified. If either name, http-equiv, or itemprop is specified, then the content attribute must also be specified. Otherwise, it must be omitted.

HTML+RDFa 1.1, [`extensions-to-the-html5-syntax`](https://www.w3.org/TR/html-rdfa/#extensions-to-the-html5-syntax) (4. Extensions to the HTML5 Syntax; Recommendation, 17 March 2015):

> If the RDFa @property attribute is present on the meta element, neither the @name, @http-equiv, nor @charset attributes are required and the @content attribute MUST be specified.

## Expected result

Invalid. HTML asks for exactly one of `name`, `http-equiv`, `charset` and `itemprop` on every `meta`. This one has none of them, and no `property` either, which HTML+RDFa lets stand in for `name`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i meta-content-only.epub -u --advisory` | ERROR RSC-005; INVALID | `meta-content-only.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-content-only.epub -u` | ERROR RSC-005; INVALID | `meta-content-only.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<meta content="true"/>` in its head.

## History

- 2026-11-21: First version.
