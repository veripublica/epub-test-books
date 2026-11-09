# A linked record that is also in the manifest

- Book: `linked-record-in-manifest.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-link-elem/linked-record-in-manifest/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#46](https://github.com/veripublica/epub-test-books/issues/46)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A link element points to a standalone XML record, and the manifest lists that record too. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The record is not a publication resource, so it must not be listed.

## Question

A `link` element points to a standalone XML record in the container, and the manifest lists that record too. The record is not in the spine or embedded in a content document. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-link-elem`](https://www.w3.org/TR/epub-33/#sec-link-elem):

> In all other cases (e.g., when linking to standalone [onix] records), the resources referenced are not publication resources (i.e., are not subject to core media type requirements) and EPUB creators MUST NOT list them in the manifest.

## Expected result

Invalid. The record is not a publication resource, so it must not be listed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i linked-record-in-manifest.epub -u --advisory` | ERROR OPF-067, USAGE OPF-097; INVALID | `linked-record-in-manifest.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck linked-record-in-manifest.epub -u` | ERROR OPF-067, USAGE OPF-097; INVALID | `linked-record-in-manifest.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references the record. That is true of a standalone record and is not a second defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/record.xml` is added and listed in the manifest as `application/xml`, and `<link rel="record" href="record.xml" media-type="application/xml"/>` is added to the metadata.

## History

- 2026-11-09: First version.
