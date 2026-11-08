# Rootfile points to a file that does not exist

- Book: `rootfile-missing-target.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container.xml-rootfile-elem/rootfile-missing-target/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: pending
- Also touches: [`sec-container-iri`](https://www.w3.org/TR/epub-33/#sec-container-iri)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rootfile element in META-INF/container.xml has full-path OEBPS/missing.opf, a file that is not in the container. The real package document is still there, at OEBPS/package.opf. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid, at the level that stops the check: the declared package document does not exist.

## Question

The `rootfile` element's `full-path` is `OEBPS/missing.opf`, which is not in the container. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container.xml-rootfile-elem`](https://www.w3.org/TR/epub-33/#sec-container.xml-rootfile-elem):

> full-path [required] Identifies the location of a package document.

EPUB 3.3, [`sec-container-iri`](https://www.w3.org/TR/epub-33/#sec-container-iri):

> In addition, all relative-URL-with-fragment strings [url] MUST, after parsing, be equal to the content URL of an existing file in the OCF abstract container.

## Expected result

Invalid, at the level that stops the check: the declared package document does not exist.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.37.1 | `epubveri -i rootfile-missing-target.epub -u --advisory` | FATAL OPF-002; INVALID | `rootfile-missing-target.epubveri-0.37.1.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-missing-target.epub -u` | FATAL OPF-002; INVALID | `rootfile-missing-target.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `META-INF/container.xml`, `full-path="OEBPS/package.opf"` becomes `full-path="OEBPS/missing.opf"`.

## History

- 2026-11-08: First version.
