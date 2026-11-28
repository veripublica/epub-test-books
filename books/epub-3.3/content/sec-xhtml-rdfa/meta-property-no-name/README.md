# A `meta` with RDFa `property` and `content` and no `name` (valid)

- Book: `meta-property-no-name.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-rdfa/meta-property-no-name/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after MobileRead 374286 #394 (veripublica/epubveri#147)
- Issue: [#691](https://github.com/veripublica/epub-test-books/issues/691)
- Other clauses: EPUB 3.3 `sec-xhtml-req`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has <meta property="dcterms:title" content="A test book."/> in its head. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. With RDFa property on a meta, name is not required, and content is given.

## Question

`content.xhtml` has `<meta property="dcterms:title" content="A test book."/>` in its head. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-rdfa`](https://www.w3.org/TR/epub-33/#sec-xhtml-rdfa):

> The [html-rdfa] specification defines a set of attributes that EPUB creators MAY use in XHTML content documents to semantically enrich the content. The use of these attributes MUST conform to the requirements defined in [html-rdfa].

HTML+RDFa 1.1, [`extensions-to-the-html5-syntax`](https://www.w3.org/TR/html-rdfa/#extensions-to-the-html5-syntax) (4. Extensions to the HTML5 Syntax; Recommendation, 17 March 2015):

> If the RDFa @property attribute is present on the meta element, neither the @name, @http-equiv, nor @charset attributes are required and the @content attribute MUST be specified.

HTML Living Standard, [`the-meta-element`](https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element) (4.2.5 The meta element; checked 2026-11-21):

> Exactly one of the name, http-equiv, charset, and itemprop attributes must be specified. If either name, http-equiv, or itemprop is specified, then the content attribute must also be specified. Otherwise, it must be omitted.

## Expected result

Valid. HTML+RDFa says that when `property` is on a `meta`, `name`, `http-equiv` and `charset` are not required, and `content` must be given. It is given. `dcterms` is a prefix of the RDFa initial context, so it needs no `prefix` declaration.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i meta-property-no-name.epub -u --advisory` | no findings; VALID | `meta-property-no-name.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-property-no-name.epub -u` | no findings; VALID | `meta-property-no-name.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<meta property="dcterms:title" content="A test book."/>` in its head.

## History

- 2026-11-21: First version.
