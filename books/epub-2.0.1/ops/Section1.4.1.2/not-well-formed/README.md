# A content document that is not well-formed

- Book: `not-well-formed.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/not-well-formed/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#293](https://github.com/veripublica/epub-test-books/issues/293)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

In content.xhtml, a p element is never closed. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The document is not well-formed XML.

## Question

In `content.xhtml`, a `p` element is never closed. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> it is a well-formed XML document (as defined by XML 1.0); and

## Expected result

Invalid. The document is not well-formed XML.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i not-well-formed.epub -u --advisory` | FATAL RSC-016; INVALID | `not-well-formed.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck not-well-formed.epub -u` | FATAL RSC-016; INVALID | `not-well-formed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the paragraph is written as `<p>Open paragraph.` with no end tag.

## History

- 2026-11-11: First version.
