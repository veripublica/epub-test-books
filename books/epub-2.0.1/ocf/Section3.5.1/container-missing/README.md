# No `META-INF/container.xml`

- Book: `container-missing.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/container-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container has no META-INF/container.xml. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. container.xml is required.

## Question

The container has no `META-INF/container.xml`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> All valid OCF Containers MUST include a file called “container.xml” within the “META-INF” directory at the root level of the container file system.

## Expected result

Invalid. `container.xml` is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i container-missing.epub -u --advisory` | FATAL RSC-002; INVALID | `container-missing.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck container-missing.epub -u` | FATAL RSC-002; INVALID | `container-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The `META-INF/container.xml` entry is left out.

## History

- 2026-11-12: First version.
