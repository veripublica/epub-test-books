# A `META-INF/rights.xml` with a namespace-qualified root (valid)

- Book: `rights-xml-namespaced.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.6/rights-xml-namespaced/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/rights.xml, an empty ext:rights element in its own namespace. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. rights.xml is optional; this one is well-formed and namespace-qualified.

## Question

The container also holds `META-INF/rights.xml`, an empty `ext:rights` element in its own namespace. Does a validator accept the book?

## Clause

OCF 2.0.1, [section 3.5.6](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Rights Management – META-INF/rights.xml (Optional); Recommended Specification, 4 September 2010):

> If the “META-INF/rights.xml” file exists, it MUST be a well-formed XML document which uses and conforms to XML Namespaces it uses, and its contents SHOULD be valid XML with namespace-qualified elements to avoid collision with future versions of OCF that MAY specify a particular format this file.

## Expected result

Valid. `rights.xml` is optional; this one is well-formed and namespace-qualified.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i rights-xml-namespaced.epub -u --advisory` | no findings; VALID | `rights-xml-namespaced.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck rights-xml-namespaced.epub -u` | no findings; VALID | `rights-xml-namespaced.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/rights.xml`: an empty `<ext:rights>`.

## History

- 2026-11-12: First version.
