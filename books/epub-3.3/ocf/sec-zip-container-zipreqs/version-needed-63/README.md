# A file whose 'version needed to extract' is 63

- Book: `version-needed-63.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-zipreqs/version-needed-63/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to complete the OCF section; parked on 2026-11-08 while both verifiers missed it, shipped once epubveri reports it
- Issue: [#629](https://github.com/veripublica/epub-test-books/issues/629)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The ZIP headers of OEBPS/content.xhtml give 63 as the version needed to extract. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The version needed to extract must be 10, 20 or 45.

## Question

The ZIP headers of `OEBPS/content.xhtml` give 63 as the version needed to extract. Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-zip-container-zipreqs`](https://www.w3.org/TR/epub-33/#sec-zip-container-zipreqs):

> In the local file header table, EPUB creators MUST set the version needed to extract fields to the values 10, 20 or 45 to match the maximum version level needed by the given file (e.g., 20 for Deflate, 45 for ZIP64).

## Expected result

Invalid. The version needed to extract must be 10, 20 or 45. EPUB 2.0.1 has the same case: `books/epub-2.0.1/ocf/Section4/version-needed-63`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i version-needed-63.epub -u --advisory` | ERROR SPEC-004; INVALID | `version-needed-63.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck version-needed-63.epub -u` | no findings; VALID | `version-needed-63.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1779](https://github.com/w3c/epubcheck/issues/1779).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The template's files, written as a container by `scripts/lib/ocfvariants.py` `version_needed_63()`. The content document's entry gives version needed 63 in its local and central headers; it is still deflated.

## History

- 2026-11-15: First version. The case was parked on 2026-11-08 while both verifiers missed it.
