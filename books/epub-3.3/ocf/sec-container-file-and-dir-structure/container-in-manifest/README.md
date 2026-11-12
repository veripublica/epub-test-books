# META-INF/container.xml listed in the manifest

- Book: `container-in-manifest.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-file-and-dir-structure/container-in-manifest/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#8](https://github.com/veripublica/epub-test-books/issues/8)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest of the package document lists META-INF/container.xml as an item. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Files in META-INF must not be in the manifest.

## Question

The package document's manifest lists `META-INF/container.xml` as an item. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-file-and-dir-structure`](https://www.w3.org/TR/epub-33/#sec-container-file-and-dir-structure):

> Files in the META-INF directory and the mimetype file are not publication resources so MUST NOT be listed in the manifest.

## Expected result

Invalid. Files in META-INF must not be in the manifest.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i container-in-manifest.epub -u --advisory` | ERROR PKG-025, USAGE OPF-097; INVALID | `container-in-manifest.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck container-in-manifest.epub -u` | ERROR PKG-025, USAGE OPF-097; INVALID | `container-in-manifest.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 is a side effect of the defect, not a second defect: the manifest now lists a file that nothing in the book references.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The manifest gains `<item id="container" href="../META-INF/container.xml" media-type="application/xml"/>`.

## History

- 2026-11-08: First version.
