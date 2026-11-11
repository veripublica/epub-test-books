# A stylesheet in ISO-8859-1

- Book: `css-iso-8859-1.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.5/css-iso-8859-1/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A linked stylesheet is encoded in ISO-8859-1 and says so with @charset. It contains the letter é. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A stylesheet must be UTF-8 or UTF-16.

## Question

A linked stylesheet is encoded in ISO-8859-1 and says so with `@charset`. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section1.4.1.5`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.5):

> External CSS stylesheets referenced by OPS documents must use UTF-8 or UTF-16 encoding. Inclusion of Byte Order Mark (BOM) is mandatory for UTF-16 encoding and optional for UTF-8 encoding.

## Expected result

Invalid. A stylesheet must be UTF-8 or UTF-16.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i css-iso-8859-1.epub -u --advisory` | ERROR CSS-004; INVALID | `css-iso-8859-1.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck css-iso-8859-1.epub -u` | ERROR CSS-004; INVALID | `css-iso-8859-1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` holds `@charset "ISO-8859-1";` and a rule with `é`, written in ISO-8859-1; `content.xhtml` links to it.

## History

- 2026-11-11: First version.
