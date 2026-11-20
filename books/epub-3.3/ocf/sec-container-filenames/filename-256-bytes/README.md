# A file name of 256 bytes

- Book: `filename-256-bytes.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-filenames/filename-256-bytes/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to complete the OCF section; parked on 2026-11-08 while both verifiers missed it, shipped once epubveri reports it
- Issue: [#622](https://github.com/veripublica/epub-test-books/issues/622)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is renamed to a name of 256 bytes (250 letters a and .xhtml), and the manifest and the navigation document point to it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The name is one byte longer than the 255 allowed.

## Question

`OEBPS/content.xhtml` is renamed to a name of 256 bytes (250 `a`s and `.xhtml`), and the manifest and the navigation document point to it. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-container-filenames`](https://www.w3.org/TR/epub-33/#sec-container-filenames):

> File names MUST NOT exceed 255 bytes.

## Expected result

Invalid. The name is one byte longer than the 255 allowed. EPUB 2.0.1 has the same case: `books/epub-2.0.1/ocf/Section3.3/filename-256-bytes`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i filename-256-bytes.epub -u --advisory` | ERROR SPEC-005; INVALID | `filename-256-bytes.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-256-bytes.epub -u` | no findings; VALID | `filename-256-bytes.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1779](https://github.com/w3c/epubcheck/issues/1779).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The template's files, written as a container by `scripts/lib/ocfvariants.py` `filename_256_bytes()`. The content document's entry is renamed `OEBPS/` + 250 `a`s + `.xhtml`; its `href` in the manifest and in the navigation document become that name.

## History

- 2026-11-15: First version. The case was parked on 2026-11-08 while both verifiers missed it.
