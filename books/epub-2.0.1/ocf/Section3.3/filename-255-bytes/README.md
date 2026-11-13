# A file name of 255 bytes (valid)

- Book: `filename-255-bytes.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.3/filename-255-bytes/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#515](https://github.com/veripublica/epub-test-books/issues/515)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is renamed to a name of 255 bytes (249 as and .xhtml), and the manifest and NCX point to it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The name is exactly 255 bytes, the most allowed.

## Question

`OEBPS/content.xhtml` is renamed to a name of 255 bytes (249 `a`s and `.xhtml`), and the manifest and NCX point to it. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (File Names; Recommended Specification, 4 September 2010):

> When represented as UTF-8, File Names MUST NOT exceed 255 bytes

## Expected result

Valid. The name is exactly 255 bytes, the most allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i filename-255-bytes.epub -u --advisory` | no findings; VALID | `filename-255-bytes.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-255-bytes.epub -u` | no findings; VALID | `filename-255-bytes.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry is renamed `OEBPS/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.xhtml`; its `href` in the manifest and its `src` in the NCX become `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.xhtml`.

## History

- 2026-11-12: First version.
