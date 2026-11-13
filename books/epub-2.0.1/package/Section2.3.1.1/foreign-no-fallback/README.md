# A foreign item with no fallback

- Book: `foreign-no-fallback.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3.1.1/foreign-no-fallback/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets; parked on 2026-11-09 until #27's comments had their time, built on 2026-11-13 for the release after 15 November
- Issue: [#607](https://github.com/veripublica/epub-test-books/issues/607)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A plain text file is in the manifest with no fallback. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A resource that is not a core media type needs a fallback.

## Question

A plain text file is in the manifest with no `fallback`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3.1.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3.1.1):

> An item that specifies a resource that is not an OPS Core Media Type (e.g. a non-core image type, a text file, a PDF file) must have a fallback specified

## Expected result

Invalid. A resource that is not a core media type needs a fallback.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i foreign-no-fallback.epub -u --advisory` | ERROR SPEC-002, USAGE ADV-010; INVALID | `foreign-no-fallback.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck foreign-no-fallback.epub -u` | no findings; VALID | `foreign-no-fallback.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1761](https://github.com/w3c/epubcheck/issues/1761).

SPEC-002 is epubveri's id for a specification rule that epubcheck has no id for. It is in epubveri's default output, not an `--advisory` finding. ADV-010 is an `--advisory` finding, and as a USAGE it does not change the verdict.

## Build

`OEBPS/extra.txt` is added to the manifest as `text/plain`.

## History

- 2026-11-09: First version, parked.
- 2026-11-13: Measured on epubveri 0.42.0 and added to the library.
