# A `META-INF/metadata.xml` with elements in no namespace

- Book: `metadata-xml-unqualified.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.3/metadata-xml-unqualified/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/metadata.xml, whose elements are in no namespace. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The elements of metadata.xml must be namespace-qualified.

## Question

The container also holds `META-INF/metadata.xml`, whose elements are in no namespace. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.3](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Metadata – META-INF/metadata.xml (Optional); Recommended Specification, 4 September 2010):

> If the “META-INF/metadata.xml” file exists, its contents MUST be valid XML with namespace-qualified elements to avoid collision with future versions of OCF that MAY specify a particular grammar and namespace for elements and attributes within this file.

## Expected result

Invalid. The elements of `metadata.xml` must be namespace-qualified.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i metadata-xml-unqualified.epub -u --advisory` | ERROR RSC-005; INVALID | `metadata-xml-unqualified.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck metadata-xml-unqualified.epub -u` | no findings; VALID | `metadata-xml-unqualified.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** w3c/epubcheck issue pending.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/metadata.xml`: `<metadata>` holding one `<note>`, in no namespace.

## History

- 2026-11-13: First version.
