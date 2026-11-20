# A `meta` with `content` and no `name` or `http-equiv` in an EPUB 2 content document (valid)

- Book: `meta-content-only.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/meta-content-only/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after MobileRead 374286 #394 (veripublica/epubveri#147): the EPUB 2 control
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has <meta content="true"/> in its head. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. In XHTML 1.1, meta requires only content, and content is given.

## Question

`content.xhtml` has `<meta content="true"/>` in its head. Does a validator accept the book?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> all XHTML elements and attributes not contained in an Inline XML Island are drawn from the XHTML subset identified in this document.

XHTML Modularization 1.1, [`s_metamodule`](https://www.w3.org/TR/xhtml-modularization/abstract_modules.html#s_metamodule) (5.15. Metainformation Module; Recommendation, 29 July 2010, Second Edition), gives `meta` the attributes I18N, `content*` (CDATA), `http-equiv` (NMTOKEN), `id` (ID), `name` (NMTOKEN) and `scheme` (CDATA). Its [`sec_4.1.`](https://www.w3.org/TR/xhtml-modularization/abstraction.html#sec_4.1.) (4.1. Syntactic Conventions) says what the asterisk means:

> When an element requires the definition of an attribute, that attribute name is followed by an asterisk (*).

## Expected result

Valid. OPS 2.0.1 content documents use XHTML 1.1, whose `meta` requires only `content`. `name` and `http-equiv` are optional there. HTML's rule of exactly one key attribute does not apply to EPUB 2.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i meta-content-only.epub -u --advisory` | no findings; VALID | `meta-content-only.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-content-only.epub -u` | no findings; VALID | `meta-content-only.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<meta content="true"/>` in its head.

## History

- 2026-11-21: First version.
