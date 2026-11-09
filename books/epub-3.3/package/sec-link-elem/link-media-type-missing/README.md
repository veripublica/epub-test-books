# A `link` into the container without `media-type`

- Book: `link-media-type-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-link-elem/link-media-type-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#67](https://github.com/veripublica/epub-test-books/issues/67)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A link element points to a file in the container and has no media-type attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The target is in the container, so the attribute is required.

## Question

A `link` element points to a file in the container and has no `media-type`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-link-elem`](https://www.w3.org/TR/epub-33/#sec-link-elem):

> EPUB creators MUST specify the attribute for all linked resources within the EPUB container.

## Expected result

Invalid. The target is in the container, so the attribute is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i link-media-type-missing.epub -u --advisory` | ERROR OPF-093; INVALID | `link-media-type-missing.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck link-media-type-missing.epub -u` | ERROR OPF-093; INVALID | `link-media-type-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/record.xml` is added, not in the manifest, and `<link rel="record" href="record.xml"/>` is added to the metadata.

## History

- 2026-11-09: First version.
