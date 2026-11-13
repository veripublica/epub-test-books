# A rootfile that points to a file that does not exist

- Book: `rootfile-missing-target.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.1/rootfile-missing-target/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#493](https://github.com/veripublica/epub-test-books/issues/493)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rootfile has full-path="OEBPS/missing.opf". Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. container.xml must give the path to the rootfile, and there is no file at that path.

## Question

The `rootfile` has `full-path="OEBPS/missing.opf"`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> The container.xml file MUST identify the MIME type of, and path to, the rootfile for the OPF/OPS version of the publication and any OPTIONAL alternate renditions included within the container.

## Expected result

Invalid. `container.xml` must give the path to the rootfile, and there is no file at that path.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i rootfile-missing-target.epub -u --advisory` | FATAL OPF-002; INVALID | `rootfile-missing-target.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck rootfile-missing-target.epub -u` | FATAL OPF-002; INVALID | `rootfile-missing-target.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. In `META-INF/container.xml`, `full-path` becomes `OEBPS/missing.opf`.

## History

- 2026-11-12: First version.
