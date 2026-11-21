# A `meta` with both `name` and `http-equiv`

- Book: `meta-name-and-http-equiv.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/meta-name-and-http-equiv/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after MobileRead 374286 #394 (veripublica/epubveri#147)
- Issue: [#689](https://github.com/veripublica/epub-test-books/issues/689)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has <meta name="author" http-equiv="X-UA-Compatible" content="IE=edge"/> in its head. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A meta must have exactly one of name, http-equiv, charset and itemprop, and this one has two.

## Question

`content.xhtml` has `<meta name="author" http-equiv="X-UA-Compatible" content="IE=edge"/>` in its head. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-meta-element`](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) (4.2.5 The meta element; checked 2026-11-21):

> Exactly one of the name, http-equiv, charset, and itemprop attributes must be specified. If either name, http-equiv, or itemprop is specified, then the content attribute must also be specified. Otherwise, it must be omitted.

## Expected result

Invalid. HTML asks for exactly one of `name`, `http-equiv`, `charset` and `itemprop` on every `meta`. This one has two, `name` and `http-equiv`. Each on its own would be conforming: `X-UA-Compatible` is an HTML pragma whose `content` must be `IE=edge`. The template's head already has `<meta charset="UTF-8"/>`, so the book uses `http-equiv` rather than a second `charset`, which would break a different rule.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i meta-name-and-http-equiv.epub -u --advisory` | ERROR RSC-005; INVALID | `meta-name-and-http-equiv.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-name-and-http-equiv.epub -u` | ERROR RSC-005; INVALID | `meta-name-and-http-equiv.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<meta name="author" http-equiv="X-UA-Compatible" content="IE=edge"/>` in its head.

## History

- 2026-11-21: First version.
