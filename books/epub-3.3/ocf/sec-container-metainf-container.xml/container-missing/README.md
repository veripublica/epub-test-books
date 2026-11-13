# No META-INF/container.xml

- Book: `container-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-metainf-container.xml/container-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#14](https://github.com/veripublica/epub-test-books/issues/14)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container has no META-INF/container.xml, so nothing says where the package document is. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid, at the level that stops the check: without container.xml no package document can be found.

## Question

The container has no `META-INF/container.xml`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-metainf-container.xml`](https://www.w3.org/TR/epub-33/#sec-container-metainf-container.xml):

> The REQUIRED container.xml file in the META-INF directory identifies the package documents available in the OCF abstract container.

## Expected result

Invalid, at the level that stops the check: without container.xml no package document can be found.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i container-missing.epub -u --advisory` | FATAL RSC-002; INVALID | `container-missing.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck container-missing.epub -u` | FATAL RSC-002; INVALID | `container-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The template's entries are written without `META-INF/container.xml`.

## History

- 2026-11-08: First version.
