# A file name with a space

- Book: `filename-space.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-filenames/filename-space/build.py`
- Origin: built here
- Expected: valid, with a warning for the space
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#12](https://github.com/veripublica/epub-test-books/issues/12)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document is named con tent.xhtml: its name contains a space (U+0020). The specification discourages this but does not forbid it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid, because this is a SHOULD NOT, not a MUST NOT. A validator that reports recommendations should warn about it.

## Question

The content document is named `con tent.xhtml`. A space is discouraged, not forbidden. What does a validator report?

## Clause

EPUB 3.3, [`sec-container-filenames`](https://www.w3.org/TR/epub-33/#sec-container-filenames):

> For compatibility with older reading systems, file names SHOULD NOT contain SPACE (U+0020) characters.

## Expected result

Valid, because this is a SHOULD NOT, not a MUST NOT. A validator that reports recommendations should warn about it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i filename-space.epub -u --advisory` | WARNING PKG-010; valid | `filename-space.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-space.epub -u` | WARNING PKG-010; valid | `filename-space.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` becomes `OEBPS/con tent.xhtml`; the manifest and navigation document refer to `con%20tent.xhtml`.

## History

- 2026-11-08: First version.
