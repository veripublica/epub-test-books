# A microdata itemid on an item with no itemtype

- Book: `microdata-itemid-no-itemtype.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/microdata-itemid-no-itemtype/build.py`
- Origin: built here, suggested by epubveri
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: epubveri, after its 0.42.0 fixes
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a div with itemscope and itemid="urn:isbn:9780306406157", but no itemtype, and a p inside with itemprop="name". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. itemid must not be specified on an element that does not have both itemscope and itemtype; this one has no itemtype.

## Question

`content.xhtml` has `itemid` on an item with `itemscope` and no `itemtype`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> EPUB creators can also specify microdata attributes [html] and linked data [json-ld11] in XHTML content documents as both are natively supported.

HTML Living Standard, [`items`](https://html.spec.whatwg.org/multipage/microdata.html#items) (5.2.2 Items):

> The itemid attribute must not be specified on elements that do not have both an itemscope attribute and an itemtype attribute specified

## Expected result

Invalid. itemid must not be specified on an element that does not have both itemscope and itemtype; this one has no itemtype.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i microdata-itemid-no-itemtype.epub -u --advisory` | ERROR RSC-005; INVALID | `microdata-itemid-no-itemtype.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck microdata-itemid-no-itemtype.epub -u` | no findings; VALID | `microdata-itemid-no-itemtype.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div itemscope="" itemid="urn:isbn:9780306406157"><p itemprop="name">A test book.</p></div>`.

## History

- 2026-11-13: First version.
