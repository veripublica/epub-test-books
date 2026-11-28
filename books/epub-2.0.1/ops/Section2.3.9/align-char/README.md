# A table cell with `align="char"`

- Book: `align-char.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.9/align-char/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets; parked on 2026-11-11 while both verifiers missed it, shipped after epubveri reports it
- Issue: [#615](https://github.com/veripublica/epub-test-books/issues/615)
- Other clauses: OPS 2.0.1 `Section1.4.1.2`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a table whose only cell has align="char". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. char is not a value of align in the OPS XHTML subset, and content documents must keep to that subset. The XHTML 1.1 DTD allows it, but OPS 2.0.1 takes it out.

## Question

In `content.xhtml`, a table cell has `align="char"`. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.9`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.9):

> The value of char for the align attribute is not included in the OPS XHTML subset.

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> all XHTML elements and attributes not contained in an Inline XML Island are drawn from the XHTML subset identified in this document.

## Expected result

Invalid. `char` is not a value of `align` in the OPS XHTML subset, and content documents must keep to that subset. The XHTML 1.1 DTD allows it, but OPS 2.0.1 takes it out.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i align-char.epub -u --advisory` | ERROR RSC-005; INVALID | `align-char.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck align-char.epub -u` | no findings; VALID | `align-char.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1780](https://github.com/w3c/epubcheck/issues/1780).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<table><tr><td align="char">1.5</td></tr></table>`.

## History

- 2026-11-11: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
