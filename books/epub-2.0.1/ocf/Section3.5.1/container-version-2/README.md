# A `container` element with `version="2.0"`

- Book: `container-version-2.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/container-version-2/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: [#594](https://github.com/veripublica/epub-test-books/issues/594)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container element of container.xml has version="2.0". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. version="1.0" must be included, and here it is 2.0.

## Question

The `container` element of `container.xml` has `version="2.0"`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The “version="1.0"” attribute MUST be included for all containers that conform to this version of the specification.

## Expected result

Invalid. `version="1.0"` must be included, and here it is `2.0`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i container-version-2.epub -u --advisory` | ERROR RSC-005; INVALID | `container-version-2.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck container-version-2.epub -u` | no findings; VALID | `container-version-2.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1777](https://github.com/w3c/epubcheck/issues/1777).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, `version="1.0"` becomes `version="2.0"`.

## History

- 2026-11-13: First version.
