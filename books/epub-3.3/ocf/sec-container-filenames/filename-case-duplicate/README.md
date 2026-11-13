# Two file names that differ only in case

- Book: `filename-case-duplicate.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-filenames/filename-case-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#9](https://github.com/veripublica/epub-test-books/issues/9)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The OEBPS folder holds content.xhtml and Content.xhtml. Both are in the manifest and the spine. On a case-insensitive file system they are the same file. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. After case folding the two names are equal.

## Question

The same folder holds `content.xhtml` and `Content.xhtml`, both in the manifest and the spine. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-filenames`](https://www.w3.org/TR/epub-33/#sec-container-filenames):

> All file names within the same directory MUST be unique following Unicode canonical normalization [uax15] and then full case folding [unicode].

## Expected result

Invalid. After case folding the two names are equal.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i filename-case-duplicate.epub -u --advisory` | ERROR OPF-060; INVALID | `filename-case-duplicate.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-case-duplicate.epub -u` | ERROR OPF-060; INVALID | `filename-case-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A second document `OEBPS/Content.xhtml` (heading "Second") is added to the ZIP, the manifest and the spine.

## History

- 2026-11-08: First version.
