# Two file names that differ only in case

- Book: `filename-case-duplicate.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.3/filename-case-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#516](https://github.com/veripublica/epub-test-books/issues/516)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/ holds content.xhtml and Content.xhtml, both in the manifest and the spine. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. Two names in the same directory that differ only in case are not allowed.

## Question

`OEBPS/` holds `content.xhtml` and `Content.xhtml`, both in the manifest and the spine. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (File Names; Recommended Specification, 4 September 2010):

> Two File Names within the same directory MUST NOT map to the same string following case normalization […]

> Two File Names that differ only in case are disallowed within the same directory.

## Expected result

Invalid. Two names in the same directory that differ only in case are not allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i filename-case-duplicate.epub -u --advisory` | ERROR OPF-060; INVALID | `filename-case-duplicate.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-case-duplicate.epub -u` | ERROR OPF-060; INVALID | `filename-case-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. A second content document, `OEBPS/Content.xhtml`, is added to the manifest and the spine.

## History

- 2026-11-12: First version.
