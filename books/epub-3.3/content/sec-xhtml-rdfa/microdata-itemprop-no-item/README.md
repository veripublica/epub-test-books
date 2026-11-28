# An itemprop on an element that is in no item

- Book: `microdata-itemprop-no-item.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/microdata-itemprop-no-item/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubveri: missed; epubcheck: missed
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions; parked on 2026-11-13 while both verifiers missed it, built on 2026-11-20
- Issue: [#678](https://github.com/veripublica/epub-test-books/issues/678)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p with itemprop="name". No ancestor of it has itemscope, and no itemref names it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. HTML allows itemprop only where it adds a property to an item, and this p is in no item.

## Question

`content.xhtml` has `itemprop` on a `p` that is in no item: no `itemscope` on it or on any ancestor, and no `itemref` pointing at it. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> EPUB creators can also specify microdata attributes [html] and linked data [json-ld11] in XHTML content documents as both are natively supported.

HTML Living Standard, [`names:-the-itemprop-attribute`](https://html.spec.whatwg.org/multipage/microdata.html#names:-the-itemprop-attribute) (5.2.3 Names: the itemprop attribute; checked 2026-11-20):

> Every HTML element may have an itemprop attribute specified, if doing so adds one or more properties to one or more items (as defined below).

## Expected result

Invalid. HTML allows `itemprop` only where it adds a property to an item. This `p` is in no item: no ancestor has `itemscope`, and no `itemref` names it. So the attribute adds no property, and the document does not conform to HTML.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i microdata-itemprop-no-item.epub -u --advisory` | ERROR RSC-005; INVALID | `microdata-itemprop-no-item.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck microdata-itemprop-no-item.epub -u` | no findings; VALID | `microdata-itemprop-no-item.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1775](https://github.com/w3c/epubcheck/issues/1775).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p itemprop="name">A test book.</p>`.

## History

- 2026-11-20: First version.
