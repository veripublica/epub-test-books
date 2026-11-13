# A file name of 256 bytes

- Book: `filename-256-bytes.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.3/filename-256-bytes/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: [#593](https://github.com/veripublica/epub-test-books/issues/593)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is renamed to a name of 256 bytes (250 as and .xhtml), and the manifest and NCX point to it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The name is one byte longer than the 255 allowed.

## Question

`OEBPS/content.xhtml` is renamed to a name of 256 bytes (250 `a`s and `.xhtml`), and the manifest and NCX point to it. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (File Names; Recommended Specification, 4 September 2010):

> When represented as UTF-8, File Names MUST NOT exceed 255 bytes

## Expected result

Invalid. The name is one byte longer than the 255 allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i filename-256-bytes.epub -u --advisory` | ERROR SPEC-005; INVALID | `filename-256-bytes.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-256-bytes.epub -u` | no findings; VALID | `filename-256-bytes.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1777](https://github.com/w3c/epubcheck/issues/1777).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry is renamed `OEBPS/` + 250 `a`s + `.xhtml`; its `href` in the manifest and its `src` in the NCX become that name.

## History

- 2026-11-13: First version.
