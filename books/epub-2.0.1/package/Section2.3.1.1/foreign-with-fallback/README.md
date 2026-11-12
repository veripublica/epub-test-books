# A foreign item with a fallback (valid)

- Book: `foreign-with-fallback.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3.1.1/foreign-with-fallback/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#195](https://github.com/veripublica/epub-test-books/issues/195)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A plain text file in the manifest has a fallback to an XHTML document. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The fallback the clause asks for is there.

## Question

A plain text file in the manifest has a `fallback` to an XHTML document. Does a validator accept it?

## Clause

OPF 2.0.1, [`Section2.3.1.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3.1.1):

> An item that specifies a resource that is not an OPS Core Media Type (e.g. a non-core image type, a text file, a PDF file) must have a fallback specified

## Expected result

Valid. The fallback the clause asks for is there.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i foreign-with-fallback.epub -u --advisory` | USAGE ADV-010; VALID | `foreign-with-fallback.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck foreign-with-fallback.epub -u` | no findings; VALID | `foreign-with-fallback.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

`OEBPS/extra.txt` is added to the manifest as `text/plain`, with `fallback="content"`.

## History

- 2026-11-09: First version.
