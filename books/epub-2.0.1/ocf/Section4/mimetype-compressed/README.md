# A Flate-compressed `mimetype` file

- Book: `mimetype-compressed.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/mimetype-compressed/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype entry is Flate-compressed (method 8). Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The mimetype file must not be compressed.

## Question

The `mimetype` entry is Flate-compressed (method 8). Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> The first file in the ZIP Container MUST be a file by the ASCII name of ‘mimetype’ which holds the MIME type for the ZIP Container (i.e., “application/epub+zip” as an ASCII string; no padding, white-space or case change). The file MUST be neither compressed nor encrypted and there MUST NOT be an extra field in its ZIP header.

## Expected result

Invalid. The `mimetype` file must not be compressed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i mimetype-compressed.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-compressed.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-compressed.epub -u` | no findings; VALID | `mimetype-compressed.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The `mimetype` entry uses compression method 8; its content is still `application/epub+zip`.

## History

- 2026-11-13: First version.
