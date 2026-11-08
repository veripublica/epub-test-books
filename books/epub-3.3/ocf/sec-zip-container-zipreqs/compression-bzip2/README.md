# An entry compressed with bzip2

- Book: `compression-bzip2.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/compression-bzip2/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#25](https://github.com/veripublica/epub-test-books/issues/25)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One entry, OEBPS/content.xhtml, is compressed with bzip2 (ZIP compression method 12) instead of Deflate. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only stored (0) and Deflate (8) are allowed.

## Question

One entry, the content document, is compressed with bzip2 (ZIP method 12) instead of Deflate. Does a validator reject the container?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> OCF ZIP containers MUST include only stored (uncompressed) and Deflate-compressed ZIP entries within the ZIP archive.

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> In the local file header table, EPUB creators MUST set the compression method field to the values 0 or 8.

## Expected result

Invalid. Only stored (0) and Deflate (8) are allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i compression-bzip2.epub -u --advisory` | FATAL PKG-027; INVALID | `compression-bzip2.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck compression-bzip2.epub -u` | FATAL PKG-027; INVALID | `compression-bzip2.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/content.xhtml` is written with method 12 (bzip2, level 9) and version needed 46; every other entry is as in the template.

## History

- 2026-11-08: First version.
