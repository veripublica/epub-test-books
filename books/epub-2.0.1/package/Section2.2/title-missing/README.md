# No `dc:title`

- Book: `title-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.2/title-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#184](https://github.com/veripublica/epub-test-books/issues/184)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The metadata has no dc:title element. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The element is required.

## Question

The metadata has no `dc:title`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.2):

> At least one of each of Dublin Core title, identifier and language must be included in the metadata element.

## Expected result

Invalid. The element is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i title-missing.epub -u --advisory` | ERROR RSC-005; INVALID | `title-missing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck title-missing.epub -u` | ERROR RSC-005; INVALID | `title-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:title` is removed.

## History

- 2026-11-09: First version.
