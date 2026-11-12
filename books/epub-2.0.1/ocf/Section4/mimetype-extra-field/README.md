# A `mimetype` entry with an extra field

- Book: `mimetype-extra-field.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/mimetype-extra-field/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The ZIP headers of mimetype have an extra field. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. There must be no extra field in its ZIP header.

## Question

The ZIP headers of `mimetype` have an extra field. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> The first file in the ZIP Container MUST be a file by the ASCII name of ‘mimetype’ which holds the MIME type for the ZIP Container (i.e., “application/epub+zip” as an ASCII string; no padding, white-space or case change). The file MUST be neither compressed nor encrypted and there MUST NOT be an extra field in its ZIP header.

## Expected result

Invalid. There must be no extra field in its ZIP header.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i mimetype-extra-field.epub -u --advisory` | ERROR PKG-005; INVALID | `mimetype-extra-field.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-extra-field.epub -u` | ERROR PKG-005; INVALID | `mimetype-extra-field.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The `mimetype` entry's local and central headers carry a four-byte extra field (header ID 0xCAFE, no data).

## History

- 2026-11-12: First version.
