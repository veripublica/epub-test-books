# A file at the root of the container that the manifest does not list (valid)

- Book: `extra-file-in-root.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.1/extra-file-in-root/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#501](https://github.com/veripublica/epub-test-books/issues/501)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds README.txt at its root. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Other files may be anywhere under the root directory, and an unlisted file is only not used for the publication.

## Question

The container also holds `README.txt` at its root. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (File and Directory Structure; Recommended Specification, 4 September 2010):

> All other files used by the publication rendition(s) within the Abstract Container MAY be in any location descendant from the root directory except for “mimetype” at the root level or within the META-INF directory.

OCF 2.0.1, [section 3.5.1](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Container – META-INF/container.xml (Required); Recommended Specification, 4 September 2010):

> Any extra files in the ZIP archive (i.e., files within the ZIP archive that are not listed within the package files’ <manifest> element, such as META-INF files or alternate derived renditions of the publication) MUST NOT be used in the processing of the OPS publication.

## Expected result

Valid. Other files may be anywhere under the root directory, and an unlisted file is only not used for the publication.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i extra-file-in-root.epub -u --advisory` | USAGE OPF-003; VALID | `extra-file-in-root.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck extra-file-in-root.epub -u` | USAGE OPF-003; VALID | `extra-file-in-root.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `README.txt` with one line of text is added.

## History

- 2026-11-12: First version.
