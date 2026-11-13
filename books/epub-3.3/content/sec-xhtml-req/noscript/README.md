# A noscript element in an XHTML content document

- Book: `noscript.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-req/noscript/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an inline script and a noscript element after it. Its manifest item has the scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. HTML does not allow noscript in XML documents, and an XHTML content document is one.

## Question

`content.xhtml` has a `noscript` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-req`](https://www.w3.org/TR/epub-33/#sec-xhtml-req):

> MUST conform to the conformance criteria for all document constructs defined by [html] unless explicitly overridden in 6.1.4 HTML deviations and constraints.

HTML Living Standard, [`the-noscript-element`](https://html.spec.whatwg.org/multipage/scripting.html#the-noscript-element) (4.12.2 The noscript element):

> The noscript element must not be used in XML documents.

## Expected result

Invalid. HTML does not allow noscript in XML documents, and an XHTML content document is one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i noscript.epub -u --advisory` | ERROR RSC-005; INVALID | `noscript.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck noscript.epub -u` | ERROR RSC-005; INVALID | `noscript.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script>let a = 1;</script>` and then `<noscript><p>Scripting is off.</p></noscript>`, and its manifest item `properties="scripted"`.

## History

- 2026-11-13: First version.
