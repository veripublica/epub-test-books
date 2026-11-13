# A manifest item whose file is not in the ZIP archive

- Book: `manifest-file-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/manifest-file-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#499](https://github.com/veripublica/epub-test-books/issues/499)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container has no OEBPS/content.xhtml, which the manifest lists. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. Every item in the manifest must be in the ZIP archive.

## Question

The container has no `OEBPS/content.xhtml`, which the manifest lists. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The <manifest> element contained within the OPF root package file specifies the one and only manifest used for OPS processing; all items referenced in this manifest MUST be included in the ZIP archive.

## Expected result

Invalid. Every item in the manifest must be in the ZIP archive.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i manifest-file-missing.epub -u --advisory` | ERROR RSC-001; INVALID | `manifest-file-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck manifest-file-missing.epub -u` | ERROR RSC-001; INVALID | `manifest-file-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The `OEBPS/content.xhtml` entry is left out.

## History

- 2026-11-12: First version.
