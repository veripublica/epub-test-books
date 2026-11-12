# A `container` element with no `version`

- Book: `container-no-version.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/container-no-version/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container element of container.xml has no version attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. version="1.0" must be included.

## Question

The `container` element of `container.xml` has no `version` attribute. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The “version="1.0"” attribute MUST be included for all containers that conform to this version of the specification.

## Expected result

Invalid. `version="1.0"` must be included.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i container-no-version.epub -u --advisory` | ERROR RSC-005; INVALID | `container-no-version.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck container-no-version.epub -u` | ERROR RSC-005; INVALID | `container-no-version.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, `version="1.0"` is removed from `container`.

## History

- 2026-11-12: First version.
