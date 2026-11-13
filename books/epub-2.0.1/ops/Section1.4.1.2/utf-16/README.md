# A content document in UTF-16 (valid)

- Book: `utf-16.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/utf-16/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets
- Issue: [#345](https://github.com/veripublica/epub-test-books/issues/345)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml is encoded in UTF-16LE with a byte order mark, and its XML declaration and charset meta element say so. It contains the letter é. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. A content document may be UTF-8 or UTF-16, and OPS 2.0.1 does not recommend one over the other.

## Question

`content.xhtml` is encoded in UTF-16LE with a byte order mark, and declares it. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> it is encoded in UTF-8 or UTF-16; and

## Expected result

Valid. A content document may be UTF-8 or UTF-16, and OPS 2.0.1 does not recommend one over the other.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i utf-16.epub -u --advisory` | no findings; VALID | `utf-16.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck utf-16.epub -u` | ERROR HTM_058; INVALID | `utf-16.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports that HTML documents must be encoded in UTF-8 (HTM_058), which OPS 2.0.1 does not require.

- **epubcheck: wrong error.** [w3c/epubcheck#1772](https://github.com/w3c/epubcheck/issues/1772).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<p>Café.</p>`, declares `encoding="UTF-16"` and `charset=utf-16`, and is written in UTF-16LE after a byte order mark (FF FE).

## History

- 2026-11-12: First version.
