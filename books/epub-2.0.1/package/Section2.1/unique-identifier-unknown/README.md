# `unique-identifier` naming no element

- Book: `unique-identifier-unknown.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.1/unique-identifier-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#183](https://github.com/veripublica/epub-test-books/issues/183)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The unique-identifier attribute names an id that no element has. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The attribute must specify a Dublin Core identifier element, and this value specifies none.

## Question

The `unique-identifier` attribute names an `id` that no element has. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.1):

> specifies which Dublin Core identifier element

## Expected result

Invalid. The attribute must specify a Dublin Core identifier element, and this value specifies none.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i unique-identifier-unknown.epub -u --advisory` | ERROR OPF-030; INVALID | `unique-identifier-unknown.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck unique-identifier-unknown.epub -u` | ERROR OPF-030; INVALID | `unique-identifier-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `unique-identifier` becomes `nope`.

## History

- 2026-11-09: First version.
