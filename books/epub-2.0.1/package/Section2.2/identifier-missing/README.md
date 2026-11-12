# No `dc:identifier`

- Book: `identifier-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.2/identifier-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#185](https://github.com/veripublica/epub-test-books/issues/185)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has no dc:identifier element. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The element is required. `unique-identifier` then points to nothing, which follows from the same defect.

## Question

The metadata has no `dc:identifier`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2):

> At least one of each of Dublin Core title, identifier and language must be included in the metadata element.

## Expected result

Invalid. The element is required. `unique-identifier` then points to nothing, which follows from the same defect.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i identifier-missing.epub -u --advisory` | ERROR OPF-030, ERROR RSC-005; INVALID | `identifier-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck identifier-missing.epub -u` | ERROR RSC-005, ERROR OPF-030; INVALID | `identifier-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:identifier` is removed.

## History

- 2026-11-09: First version.
