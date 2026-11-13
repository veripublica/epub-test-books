# A `META-INF/signatures.xml` whose root is not `signatures`

- Book: `signatures-xml-wrong-root.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section3.5.4/signatures-xml-wrong-root/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the OCF 2.0.1 sets
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The container also holds META-INF/signatures.xml, whose root element is sigs. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The root element of signatures.xml must be signatures.

## Question

The container also holds `META-INF/signatures.xml`, whose root element is `sigs`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 3.5.4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Digital Signatures – META-INF/signatures.xml (Optional); Recommended Specification, 4 September 2010):

> This file is an XML document whose root element is <signatures>.

OCF 2.0.1, [section 3.5.4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (Digital Signatures – META-INF/signatures.xml (Optional); Recommended Specification, 4 September 2010):

> A RELAX NG OCF schema describing the <signature> element that MUST be the root element of signatures.xml can be found in the Appendix A.

## Expected result

Invalid. The root element of `signatures.xml` must be `signatures`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i signatures-xml-wrong-root.epub -u --advisory` | ERROR RSC-005; INVALID | `signatures-xml-wrong-root.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck signatures-xml-wrong-root.epub -u` | ERROR RSC-005; INVALID | `signatures-xml-wrong-root.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. An entry `META-INF/signatures.xml`: an empty `<sigs>` in the container namespace.

## History

- 2026-11-12: First version.
