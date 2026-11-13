# A `META-INF/metadata.xml` with namespace-qualified elements (valid)

- Book: `metadata-xml-namespaced.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.3/metadata-xml-namespaced/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: [#503](https://github.com/veripublica/epub-test-books/issues/503)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/metadata.xml, whose elements are in their own namespace. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. metadata.xml is optional, and its elements are namespace-qualified.

## Question

The container also holds `META-INF/metadata.xml`, whose elements are in their own namespace. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.5.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Metadata – META-INF/metadata.xml (Optional); Recommended Specification, 4 September 2010):

> If the “META-INF/metadata.xml” file exists, its contents MUST be valid XML with namespace-qualified elements to avoid collision with future versions of OCF that MAY specify a particular grammar and namespace for elements and attributes within this file.

## Expected result

Valid. `metadata.xml` is optional, and its elements are namespace-qualified.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i metadata-xml-namespaced.epub -u --advisory` | no findings; VALID | `metadata-xml-namespaced.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck metadata-xml-namespaced.epub -u` | no findings; VALID | `metadata-xml-namespaced.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/metadata.xml`: `<ext:metadata>` holding one `<ext:note>`.

## History

- 2026-11-12: First version.
