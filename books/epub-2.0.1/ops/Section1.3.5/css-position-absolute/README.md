# `position: absolute` in a stylesheet (valid)

- Book: `css-position-absolute.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.3.5/css-position-absolute/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A linked stylesheet sets position: absolute on p, which OPS 2.0.1 strongly discourages. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Absolute positioning is discouraged, not forbidden. A warning would fit.

## Question

A linked stylesheet sets `position: absolute` on `p`. OPS 2.0.1 strongly discourages it. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section1.3.5`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.3.5):

> Use of the CSS position property values to achieve absolute positioning (i.e. absolute and fixed) is strongly discouraged.

## Expected result

Valid. Absolute positioning is discouraged, not forbidden. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i css-position-absolute.epub -u --advisory` | no findings; VALID | `css-position-absolute.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck css-position-absolute.epub -u` | no findings; VALID | `css-position-absolute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` holds `p { position: absolute; top: 0; }`; `content.xhtml` links to it.

## History

- 2026-11-11: First version.
