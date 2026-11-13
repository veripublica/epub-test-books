# A content document in ISO-8859-1

- Book: `iso-8859-1.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/iso-8859-1/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#294](https://github.com/veripublica/epub-test-books/issues/294)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml is encoded in ISO-8859-1, and its XML declaration and charset meta element say so. It contains the letter é. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A content document must be UTF-8 or UTF-16.

## Question

`content.xhtml` is encoded in ISO-8859-1 and declares it. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> it is encoded in UTF-8 or UTF-16; and

## Expected result

Invalid. A content document must be UTF-8 or UTF-16.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i iso-8859-1.epub -u --advisory` | ERROR RSC-028; INVALID | `iso-8859-1.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck iso-8859-1.epub -u` | ERROR RSC-028; INVALID | `iso-8859-1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds `<p>Café.</p>`, declares `encoding="ISO-8859-1"` and `charset=iso-8859-1`, and is written in ISO-8859-1.

## History

- 2026-11-11: First version.
