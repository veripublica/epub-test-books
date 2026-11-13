# A file name with a space (valid)

- Book: `filename-space.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.3/filename-space/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#510](https://github.com/veripublica/epub-test-books/issues/510)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/content.xhtml is renamed OEBPS/con tent.xhtml, and the manifest and NCX point to it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. A space is not one of the characters OCF 2.0.1 forbids.

## Question

`OEBPS/content.xhtml` is renamed `OEBPS/con tent.xhtml`, and the manifest and NCX point to it. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (File Names; Recommended Specification, 4 September 2010):

> File Names MUST NOT use the following characters (Reason: these characters may not be supported always across commonly used operating systems):

> Slash: / (ASCII 0x2F)

> Double quote: " (ASCII 0x22)

> Asterisk: * (ASCII 0x2A)

> Period as the last character: . (ASCII 0x3A)

> Colon : : (ASCII 0x3A)

> Less than: < (ASCII 0x3C)

> Greater than: > (ASCII 0x3E)

> Question mark: ? (ASCII 0x3F)

> Back slash : \ (ASCII 0x5C)

## Expected result

Valid. A space is not one of the characters OCF 2.0.1 forbids.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i filename-space.epub -u --advisory` | WARNING PKG-010; VALID | `filename-space.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck filename-space.epub -u` | WARNING PKG-010; VALID | `filename-space.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING PKG-010 is a warning, which does not make the book invalid.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The content document's entry is renamed `OEBPS/con tent.xhtml`; its `href` in the manifest and its `src` in the NCX become `con%20tent.xhtml`.

## History

- 2026-11-12: First version.
