# A stylesheet in UTF-16 with a byte order mark (valid)

- Book: `css-utf-16-bom.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.5/css-utf-16-bom/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#300](https://github.com/veripublica/epub-test-books/issues/300)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A linked stylesheet is UTF-16, little-endian, with a byte order mark. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. UTF-16 is allowed, and it has the byte order mark it must have.

## Question

A linked stylesheet is UTF-16 (little-endian) with a byte order mark. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section1.4.1.5`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.5):

> External CSS stylesheets referenced by OPS documents must use UTF-8 or UTF-16 encoding. Inclusion of Byte Order Mark (BOM) is mandatory for UTF-16 encoding and optional for UTF-8 encoding.

## Expected result

Valid. UTF-16 is allowed, and it has the byte order mark it must have.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i css-utf-16-bom.epub -u --advisory` | WARNING CSS-003; VALID | `css-utf-16-bom.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck css-utf-16-bom.epub -u` | WARNING CSS-003; VALID | `css-utf-16-bom.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING CSS-003 recommends UTF-8. OPS 2.0.1 makes no such recommendation, but a warning does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` holds `p { margin: 0; }` in UTF-16LE after a byte order mark; `content.xhtml` links to it.

## History

- 2026-11-11: First version.
