# A `style` element with no `type`

- Book: `style-no-type.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.8/style-no-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#311](https://github.com/veripublica/epub-test-books/issues/311)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The head of content.xhtml has a style element with no type attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The `type` attribute is required.

## Question

The `head` of `content.xhtml` has a `style` element with no `type` attribute. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.8`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.8):

> The type attribute of the style element is required (per XHTML 1.1 requirements) and must be given the value of text/css or the deprecated text/x-oeb1-css.

## Expected result

Invalid. The `type` attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i style-no-type.epub -u --advisory` | ERROR RSC-005; INVALID | `style-no-type.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck style-no-type.epub -u` | ERROR RSC-005; INVALID | `style-no-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `<style>p { margin: 0; }</style>` is added to `head`.

## History

- 2026-11-11: First version.
