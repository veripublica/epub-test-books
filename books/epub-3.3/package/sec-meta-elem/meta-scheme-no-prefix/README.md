# A `scheme` value with no prefix

- Book: `meta-scheme-no-prefix.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-meta-elem/meta-scheme-no-prefix/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#89](https://github.com/veripublica/epub-test-books/issues/89)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One extra meta element has a scheme attribute with no prefix. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The value has no prefix.

## Question

A `meta` element's `scheme` attribute is `nope`, with no prefix. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-meta-elem`](https://www.w3.org/TR/epub-33/#sec-meta-elem):

> The scheme attribute does not have a default vocabulary (i.e., all values require a prefix).

## Expected result

Invalid. The value has no prefix.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i meta-scheme-no-prefix.epub -u --advisory` | ERROR OPF-027; INVALID | `meta-scheme-no-prefix.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck meta-scheme-no-prefix.epub -u` | ERROR OPF-027; INVALID | `meta-scheme-no-prefix.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a `meta` with `scheme="nope"` is added to the metadata.

## History

- 2026-11-09: First version.
