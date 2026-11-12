# container.xml with version="2.0"

- Book: `container-version-wrong.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container.xml-container-elem/container-version-wrong/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#35](https://github.com/veripublica/epub-test-books/issues/35)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container element in META-INF/container.xml has version="2.0" instead of "1.0". The XML declaration still says version 1.0. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The only allowed value of the `version` attribute is `1.0`.

## Question

The `container` element in `META-INF/container.xml` says `version="2.0"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container.xml-container-elem`](https://www.w3.org/TR/epub-33/#sec-container.xml-container-elem):

> version [required] This attribute MUST have the value "1.0".

## Expected result

Invalid. The only allowed value of the `version` attribute is `1.0`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i container-version-wrong.epub -u --advisory` | ERROR RSC-005; INVALID | `container-version-wrong.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck container-version-wrong.epub -u` | ERROR RSC-005; INVALID | `container-version-wrong.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

epubveri 0.37.1 gave no finding here and called this book VALID. 0.38.0 is the first release with the fix.

## Build

In `META-INF/container.xml`, `<container version="1.0"` becomes `<container version="2.0"`. The XML declaration is not changed.

## History

- 2026-11-08: First version.
