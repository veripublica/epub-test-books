# A file name with a vertical line

- Book: `filename-forbidden-char.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-filenames/filename-forbidden-char/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#10](https://github.com/veripublica/epub-test-books/issues/10)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document is named con|tent.xhtml: its name contains a vertical line (U+007C). Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. U+007C is on the list of forbidden characters.

## Question

The content document is named `con|tent.xhtml`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-filenames`](https://www.w3.org/TR/epub-33/#sec-container-filenames):

> File names MUST NOT use the following [unicode] characters, as commonly used operating systems may not support these characters consistently: […] VERTICAL LINE: | (U+007C)

## Expected result

Invalid. U+007C is on the list of forbidden characters.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i filename-forbidden-char.epub -u --advisory` | ERROR PKG-009; INVALID | `filename-forbidden-char.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck filename-forbidden-char.epub -u` | ERROR PKG-009; INVALID | `filename-forbidden-char.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` becomes `OEBPS/con|tent.xhtml`; the manifest and navigation document refer to `con%7Ctent.xhtml`.

## History

- 2026-11-08: First version.
