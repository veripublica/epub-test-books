# `epub:type` on `head`

- Book: `epub-type-on-head.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-on-head/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#153](https://github.com/veripublica/epub-test-books/issues/153)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The head element has an epub:type attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The attribute is not allowed on `head`.

## Question

The `head` element has an `epub:type` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-structural-semantics`](https://www.w3.org/TR/epub-33/#sec-xhtml-structural-semantics):

> The attribute MUST NOT be used on the head element or metadata content [html].

## Expected result

Invalid. The attribute is not allowed on `head`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-type-on-head.epub -u --advisory` | ERROR RSC-005; INVALID | `epub-type-on-head.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-on-head.epub -u` | ERROR RSC-005; INVALID | `epub-type-on-head.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `head` gets `epub:type="chapter"`.

## History

- 2026-11-09: First version.
