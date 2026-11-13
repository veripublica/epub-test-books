# A file name that is not UTF-8

- Book: `filename-not-utf8.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/filename-not-utf8/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document's name in the ZIP is OEBPS/c\x81ntent.xhtml, with the UTF-8 flag clear. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. File names must be encoded in UTF-8.

## Question

The content document's name in the ZIP is `OEBPS/c\x81ntent.xhtml`, with the UTF-8 flag clear. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> Conforming OCF ZIP Containers MUST encode File System Names using UTF-8.

## Expected result

Invalid. File names must be encoded in UTF-8.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i filename-not-utf8.epub -u --advisory` | FATAL PKG-027; INVALID | `filename-not-utf8.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-not-utf8.epub -u` | FATAL PKG-027; INVALID | `filename-not-utf8.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry name is the bytes `OEBPS/c\x81ntent.xhtml` (0x81 is ü in CP437), with bit 11 of the flags clear; the manifest and NCX use `c%C3%BCntent.xhtml`.

## History

- 2026-11-12: First version.
