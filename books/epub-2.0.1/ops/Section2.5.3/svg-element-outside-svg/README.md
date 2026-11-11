# An SVG `rect` outside an `svg` element

- Book: `svg-element-outside-svg.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.5.3/svg-element-outside-svg/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an SVG rect element directly inside an XHTML div, with no svg element around it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. SVG elements other than `svg` must be inside an `svg` element.

## Question

`content.xhtml` has an SVG `rect` element directly inside an XHTML `div`, with no `svg` around it. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.5.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.5.3):

> Other SVG elements may only be used as svg element descendants.

## Expected result

Invalid. SVG elements other than `svg` must be inside an `svg` element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i svg-element-outside-svg.epub -u --advisory` | ERROR RSC-005; INVALID | `svg-element-outside-svg.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-element-outside-svg.epub -u` | ERROR RSC-005; INVALID | `svg-element-outside-svg.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<rect xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="gray"/>` in a `div`.

## History

- 2026-11-11: First version.
