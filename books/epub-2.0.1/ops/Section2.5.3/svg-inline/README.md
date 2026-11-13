# SVG inside a content document (valid)

- Book: `svg-inline.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.5.3/svg-inline/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#313](https://github.com/veripublica/epub-test-books/issues/313)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an svg element, in the SVG namespace, inside a div. It draws a gray square. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Inline SVG is allowed in XHTML content documents.

## Question

`content.xhtml` has an `svg` element, in the SVG namespace, inside a `div`. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.5.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.5.3):

> The SVG root element (svg) must be considered replaced by its content in the CSS layout, so svg elements may be used anywhere XHTML img elements could be used. Other SVG elements may only be used as svg element descendants.

## Expected result

Valid. Inline SVG is allowed in XHTML content documents.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-inline.epub -u --advisory` | no findings; VALID | `svg-inline.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-inline.epub -u` | no findings; VALID | `svg-inline.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"><rect width="40" height="40" fill="gray"/></svg>` in a `div`.

## History

- 2026-11-11: First version.
