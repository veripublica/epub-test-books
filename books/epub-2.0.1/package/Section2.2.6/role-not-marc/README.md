# A creator role that is not a MARC code

- Book: `role-not-marc.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.2.6/role-not-marc/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#187](https://github.com/veripublica/epub-test-books/issues/187)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A dc:creator has opf:role="writer", which is neither a MARC code nor an oth. value. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A value that is not a MARC code must begin with `oth.`.

## Question

A `dc:creator` has `opf:role="writer"`, which is neither a MARC code nor an `oth.` value. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.2.6`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2.6):

> When roles are specified, the 3-character registered MARC values must be used when applicable.

> Such values must begin with oth.

## Expected result

Invalid. A value that is not a MARC code must begin with `oth.`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i role-not-marc.epub -u --advisory` | ERROR OPF-052; INVALID | `role-not-marc.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck role-not-marc.epub -u` | ERROR OPF-052; INVALID | `role-not-marc.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:creator` gets `opf:role="writer"`.

## History

- 2026-11-09: First version.
