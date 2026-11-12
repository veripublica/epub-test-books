# A `collection` element

- Book: `collection-element.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.0/collection-element/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#211](https://github.com/veripublica/epub-test-books/issues/211)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package document has a collection element, which belongs to EPUB 3. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The schema in Appendix A has no such element.

## Question

The package document has a `collection` element, which belongs to EPUB 3. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.0`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.0):

> An OPF Package Document must be a valid XML document conforming to the OPF Package schema

## Expected result

Invalid. The schema in Appendix A has no such element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i collection-element.epub -u --advisory` | ERROR RSC-005; INVALID | `collection-element.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck collection-element.epub -u` | ERROR RSC-005; INVALID | `collection-element.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `collection` element is added after `spine`.

## History

- 2026-11-09: First version.
