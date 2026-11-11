# A content document with no namespace on its root

- Book: `root-no-namespace.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.3.2/root-no-namespace/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#292](https://github.com/veripublica/epub-test-books/issues/292)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The html element of content.xhtml has no xmlns attribute, so it is in no namespace. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The root element must declare the XHTML namespace.

## Question

The `html` element of `content.xhtml` has no `xmlns` attribute, so it is in no namespace. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section1.3.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.3.2):

> The root element of all OPS Content Documents must explicitly specify the namespace of the document. For the XHTML Preferred Vocabulary, this namespace is http://www.w3.org/1999/xhtml.

## Expected result

Invalid. The root element must declare the XHTML namespace.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i root-no-namespace.epub -u --advisory` | ERROR RSC-005; INVALID | `root-no-namespace.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck root-no-namespace.epub -u` | ERROR RSC-005; INVALID | `root-no-namespace.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `xmlns="http://www.w3.org/1999/xhtml"` is removed from `html`.

## History

- 2026-11-11: First version.
