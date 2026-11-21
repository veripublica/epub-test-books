# The `mimetype` file listed in the manifest

- Book: `mimetype-in-manifest.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-file-and-dir-structure/mimetype-in-manifest/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to complete the OCF section; parked on 2026-11-08 while both verifiers missed it, shipped once epubveri reports it
- Issue: [#621](https://github.com/veripublica/epub-test-books/issues/621)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest of the package document lists the mimetype file as an item. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The mimetype file must not be in the manifest.

## Question

The package document's manifest lists the `mimetype` file as an item (`href="../mimetype"`). Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-file-and-dir-structure`](https://www.w3.org/TR/epub-33/#sec-container-file-and-dir-structure):

> Files in the META-INF directory and the mimetype file are not publication resources so MUST NOT be listed in the manifest.

## Expected result

Invalid. The `mimetype` file must not be in the manifest. `container-in-manifest`, beside this set, does the same with `META-INF/container.xml`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i mimetype-in-manifest.epub -u --advisory` | ERROR SPEC-006, USAGE OPF-097; INVALID | `mimetype-in-manifest.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-in-manifest.epub -u` | USAGE OPF-097; VALID | `mimetype-in-manifest.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports only USAGE OPF-097, and the book stays valid.

- **epubcheck: missed.** [w3c/epubcheck#1779](https://github.com/w3c/epubcheck/issues/1779).

USAGE OPF-097 is a side effect of the defect, not a second defect: the manifest now lists a file that nothing in the book references.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The manifest gains `<item id="mimetype" href="../mimetype" media-type="text/plain"/>`.

## History

- 2026-11-15: First version. The case was parked on 2026-11-08 while both verifiers missed it.
