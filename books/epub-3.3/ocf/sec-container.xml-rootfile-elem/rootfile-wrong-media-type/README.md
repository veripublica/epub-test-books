# Rootfile with the wrong media type

- Book: `rootfile-wrong-media-type.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container.xml-rootfile-elem/rootfile-wrong-media-type/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rootfile element in META-INF/container.xml points to the right package document, but its media-type attribute says application/xml. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The only allowed value is `application/oebps-package+xml`, so no package document is declared.

## Question

The `rootfile` element in container.xml says `media-type="application/xml"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container.xml-rootfile-elem`](https://www.w3.org/TR/epub-33/#sec-container.xml-rootfile-elem):

> media-type [required] Identifies the media type of the package document. The value of the attribute MUST be "application/oebps-package+xml".

## Expected result

Invalid. The only allowed value is `application/oebps-package+xml`, so no package document is declared.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i rootfile-wrong-media-type.epub -u --advisory` | ERROR RSC-003; INVALID | `rootfile-wrong-media-type.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-wrong-media-type.epub -u` | ERROR RSC-003; INVALID | `rootfile-wrong-media-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `META-INF/container.xml`, `media-type="application/oebps-package+xml"` becomes `media-type="application/xml"`.

## History

- 2026-11-08: First version.
