# A file compressed with BZIP2

- Book: `compression-bzip2.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/compression-bzip2/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#519](https://github.com/veripublica/epub-test-books/issues/519)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is compressed with BZIP2 (method 12). Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. Only stored or Flate-compressed files are allowed.

## Question

`OEBPS/content.xhtml` is compressed with BZIP2 (method 12). Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> Conforming OCF ZIP Containers MUST only include uncompressed files or Flate-compressed files within the ZIP archive.

## Expected result

Invalid. Only stored or Flate-compressed files are allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i compression-bzip2.epub -u --advisory` | FATAL PKG-027; INVALID | `compression-bzip2.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck compression-bzip2.epub -u` | FATAL PKG-027; INVALID | `compression-bzip2.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry uses compression method 12, version needed 46.

## History

- 2026-11-12: First version.
