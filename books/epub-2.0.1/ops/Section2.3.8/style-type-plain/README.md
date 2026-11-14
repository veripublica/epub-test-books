# A `style` element of type `text/plain`

- Book: `style-type-plain.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.8/style-type-plain/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets; parked on 2026-11-11 while both verifiers missed it, shipped after epubveri reports it
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The head of content.xhtml has a style element whose type is text/plain. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The type of a style element must be text/css or text/x-oeb1-css.

## Question

The head of `content.xhtml` has `<style type="text/plain">`. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.8`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.8):

> The type attribute of the style element is required (per XHTML 1.1 requirements) and must be given the value of text/css or the deprecated text/x-oeb1-css.

## Expected result

Invalid. The `type` of a `style` element must be `text/css` or `text/x-oeb1-css`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.43.0 | `epubveri -i style-type-plain.epub -u --advisory` | ERROR RSC-005; INVALID | `style-type-plain.epubveri-0.43.0.txt` |
| epubcheck 5.4.0 | `epubcheck style-type-plain.epub -u` | no findings; VALID | `style-type-plain.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The head of `content.xhtml` holds `<style type="text/plain">p { margin: 0; }</style>`.

## History

- 2026-11-11: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
