# A `meta` with `itemprop` and `content` inside an item (valid)

- Book: `meta-itemprop-in-item.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/meta-itemprop-in-item/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after MobileRead 374286 #394 (veripublica/epubveri#147)
- Issue: [#692](https://github.com/veripublica/epub-test-books/issues/692)
- Other clauses: EPUB 3.3 `sec-xhtml-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has <div itemscope="" itemtype="https://schema.org/Book"><meta itemprop="name" content="A test book."/></div> in its body. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The meta has one key attribute, itemprop, with content, inside an item.

## Question

`content.xhtml` has `<div itemscope="" itemtype="https://schema.org/Book"><meta itemprop="name" content="A test book."/></div>` in its body. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> EPUB creators can also specify microdata attributes [html] and linked data [json-ld11] in XHTML content documents as both are natively supported.

HTML Living Standard, [`the-meta-element`](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) (4.2.5 The meta element; checked 2026-11-21):

> Exactly one of the name, http-equiv, charset, and itemprop attributes must be specified. If either name, http-equiv, or itemprop is specified, then the content attribute must also be specified. Otherwise, it must be omitted.

## Expected result

Valid. The `meta` has exactly one of the four key attributes, `itemprop`, and the `content` that `itemprop` asks for. It sits inside an element with `itemscope`, so it adds a property to that item.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i meta-itemprop-in-item.epub -u --advisory` | no findings; VALID | `meta-itemprop-in-item.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-itemprop-in-item.epub -u` | no findings; VALID | `meta-itemprop-in-item.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div itemscope="" itemtype="https://schema.org/Book"><meta itemprop="name" content="A test book."/></div>` in its body.

## History

- 2026-11-21: First version.
