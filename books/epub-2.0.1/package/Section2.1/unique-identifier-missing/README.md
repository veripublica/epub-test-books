# No `unique-identifier`

- Book: `unique-identifier-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.1/unique-identifier-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#182](https://github.com/veripublica/epub-test-books/issues/182)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package element has no unique-identifier attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The attribute is required.

## Question

The `package` element has no `unique-identifier` attribute. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.1):

> The package element must specify a value for its unique-identifier attribute.

## Expected result

Invalid. The attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i unique-identifier-missing.epub -u --advisory` | ERROR RSC-005, ERROR OPF-048, ERROR OPF-030; INVALID | `unique-identifier-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck unique-identifier-missing.epub -u` | ERROR RSC-005, ERROR OPF-048, ERROR OPF-030; INVALID | `unique-identifier-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `unique-identifier` is removed from `package`.

## History

- 2026-11-09: First version.
