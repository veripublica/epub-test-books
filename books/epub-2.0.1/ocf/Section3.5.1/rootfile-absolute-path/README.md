# A rootfile `full-path` that starts with `/`

- Book: `rootfile-absolute-path.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/rootfile-absolute-path/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rootfile has full-path="/OEBPS/package.opf". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A path that starts with / is path-absolute, not path-rootless.

## Question

The `rootfile` has `full-path="/OEBPS/package.opf"`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The values of the full-path attributes MUST contain a “path component” (as defined by RFC3986) which MUST only take the form of a “path-rootless” (as defined by RFC3986).

## Expected result

Invalid. A path that starts with `/` is path-absolute, not path-rootless.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i rootfile-absolute-path.epub -u --advisory` | FATAL OPF-002; INVALID | `rootfile-absolute-path.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-absolute-path.epub -u` | ERROR RSC-026; INVALID | `rootfile-absolute-path.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, `full-path` becomes `/OEBPS/package.opf`.

## History

- 2026-11-12: First version.
