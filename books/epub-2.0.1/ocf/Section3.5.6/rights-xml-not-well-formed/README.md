# A `META-INF/rights.xml` that is not well-formed

- Book: `rights-xml-not-well-formed.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.6/rights-xml-not-well-formed/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer; parked on 2026-11-12 while both verifiers missed it, shipped after epubveri 0.42.0 reports it
- Issue: [#597](https://github.com/veripublica/epub-test-books/issues/597)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/rights.xml, whose root element is never closed. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. rights.xml must be a well-formed XML document.

## Question

The container also holds `META-INF/rights.xml`, whose root element is never closed. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.6](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Rights Management – META-INF/rights.xml (Optional); Recommended Specification, 4 September 2010):

> If the “META-INF/rights.xml” file exists, it MUST be a well-formed XML document which uses and conforms to XML Namespaces it uses, and its contents SHOULD be valid XML with namespace-qualified elements to avoid collision with future versions of OCF that MAY specify a particular format this file.

## Expected result

Invalid. `rights.xml` must be a well-formed XML document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i rights-xml-not-well-formed.epub -u --advisory` | ERROR RSC-005; INVALID | `rights-xml-not-well-formed.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck rights-xml-not-well-formed.epub -u` | no findings; VALID | `rights-xml-not-well-formed.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1777](https://github.com/w3c/epubcheck/issues/1777).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/rights.xml`: an `<ext:rights>` start tag in its own namespace, with no end tag.

## History

- 2026-11-13: First version.
