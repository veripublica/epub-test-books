# A microdata itemref without itemscope

- Book: `microdata-itemref-no-itemscope.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/microdata-itemref-no-itemscope/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri, after its 0.42.0 fixes
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with itemref="title" and no itemscope; the p with id="title" follows it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. itemref must not be specified on an element that has no itemscope attribute.

## Question

`content.xhtml` has `itemref` on a `div` with no `itemscope`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> EPUB creators can also specify microdata attributes [html] and linked data [json-ld11] in XHTML content documents as both are natively supported.

HTML Living Standard, [`items`](https://html.spec.whatwg.org/multipage/microdata.html#items) (5.2.2 Items):

> The itemref attribute must not be specified on elements that do not have an itemscope attribute specified.

## Expected result

Invalid. itemref must not be specified on an element that has no itemscope attribute.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i microdata-itemref-no-itemscope.epub -u --advisory` | ERROR RSC-005; INVALID | `microdata-itemref-no-itemscope.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck microdata-itemref-no-itemscope.epub -u` | no findings; VALID | `microdata-itemref-no-itemscope.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div itemref="title"><p>A test book.</p></div>` and then `<p id="title">Content.</p>`.

## History

- 2026-11-13: First version.
