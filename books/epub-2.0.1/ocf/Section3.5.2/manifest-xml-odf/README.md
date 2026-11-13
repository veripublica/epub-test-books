# A `META-INF/manifest.xml` in the ODF manifest format (valid)

- Book: `manifest-xml-odf.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.2/manifest-xml-odf/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#502](https://github.com/veripublica/epub-test-books/issues/502)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/manifest.xml, an ODF 1.0 manifest with one file-entry. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. manifest.xml is optional, and this one follows the ODF 1.0 manifest schema.

## Question

The container also holds `META-INF/manifest.xml`, an ODF 1.0 manifest with one `file-entry`. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.5.2](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Manifest – META-INF/manifest.xml (Optional); Recommended Specification, 4 September 2010):

> If present, the file’s content MUST be as defined in the ODF 1.0 manifest schema

## Expected result

Valid. `manifest.xml` is optional, and this one follows the ODF 1.0 manifest schema.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i manifest-xml-odf.epub -u --advisory` | no findings; VALID | `manifest-xml-odf.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck manifest-xml-odf.epub -u` | no findings; VALID | `manifest-xml-odf.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/manifest.xml`: `manifest:manifest` with one `manifest:file-entry` for `/`.

## History

- 2026-11-12: First version.
