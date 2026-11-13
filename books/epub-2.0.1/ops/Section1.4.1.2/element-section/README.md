# An HTML5 `section` in a content document

- Book: `element-section.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/element-section/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#298](https://github.com/veripublica/epub-test-books/issues/298)
- Other clauses: `Section2.2.1`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a section element, which HTML5 added. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. `section` is not an XHTML 1.1 element, so it cannot be in the OPS subset.

## Question

`content.xhtml` has a `section` element, which HTML5 added. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> all XHTML elements and attributes not contained in an Inline XML Island are drawn from the XHTML subset identified in this document.

## Expected result

Invalid. `section` is not an XHTML 1.1 element, so it cannot be in the OPS subset.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i element-section.epub -u --advisory` | ERROR RSC-005; INVALID | `element-section.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck element-section.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `element-section.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<section><p>x</p></section>`.

## History

- 2026-11-11: First version.
