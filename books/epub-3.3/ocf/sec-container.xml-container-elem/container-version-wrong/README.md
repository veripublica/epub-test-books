# container.xml with version="2.0"

- Book: `container-version-wrong.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container.xml-container-elem/container-version-wrong/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending

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
| epubveri 0.37.1+1a33152 | `epubveri -i container-version-wrong.epub -u --advisory` | ERROR RSC-005; INVALID | `container-version-wrong.epubveri-0.37.1+1a33152.txt` |
| epubcheck 5.4.0 | `epubcheck container-version-wrong.epub -u` | ERROR RSC-005; INVALID | `container-version-wrong.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

Preview: the epubveri output comes from an unreleased build (commit 1a33152). The released epubveri 0.37.1 gives no finding and calls this book VALID; the fix comes with its next release. Before this set ships, the output is regenerated with that release and this note goes.

## Build

In `META-INF/container.xml`, `<container version="1.0"` becomes `<container version="2.0"`. The XML declaration is not changed.

## History

- 2026-11-08: First version.
