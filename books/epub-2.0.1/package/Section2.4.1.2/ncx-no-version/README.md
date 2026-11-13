# An NCX without `version`

- Book: `ncx-no-version.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/ncx-no-version/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets; parked on 2026-11-09 until #27's comments had their time, built on 2026-11-13 for the release after 15 November
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The ncx element has no version attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The attribute must be specified.

## Question

The `ncx` element has no `version` attribute. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> The version and xmlns attributes on the ncx element must be explicitly specified in the document instance

## Expected result

Invalid. The attribute must be specified.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i ncx-no-version.epub -u --advisory` | ERROR RSC-005; INVALID | `ncx-no-version.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-no-version.epub -u` | no findings; VALID | `ncx-no-version.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1761](https://github.com/w3c/epubcheck/issues/1761).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/toc.ncx`, `version` is removed from `ncx`.

## History

- 2026-11-09: First version, parked.
- 2026-11-13: Measured on epubveri 0.42.0 and added to the library.
