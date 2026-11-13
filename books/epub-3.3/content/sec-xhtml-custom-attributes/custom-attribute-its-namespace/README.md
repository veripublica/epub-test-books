# An ITS attribute in the ITS namespace

- Book: `custom-attribute-its-namespace.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-custom-attributes/custom-attribute-its-namespace/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 comparison (2026-11-13)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p element has its:translate="no", an attribute in the ITS namespace http://www.w3.org/2005/11/its. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The ITS namespace is at w3.org, so the attribute is not a custom attribute, and HTML does not define it.

## Question

A `p` element has `its:translate="no"`, in the ITS namespace `http://www.w3.org/2005/11/its`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-custom-attributes`](https://www.w3.org/TR/epub-33/#sec-xhtml-custom-attributes):

> XHTML content documents MAY contain custom attributes, which are prefixed [xml-names] attributes whose namespace URL does not include either of the following strings in its domain [url]: w3.org idpf.org

The EPUB 3.4 draft says the same about this namespace in so many words. EPUB 3.4 (Candidate Recommendation Draft, 13 November 2026), [`sec-xhtml-its`](https://www.w3.org/TR/epub-34/#sec-xhtml-its):

> ITS attributes MUST only be used as defined in Using ITS markup in HTML [its20] (i.e., EPUB 3 does not support the namespaced attributes).

## Expected result

Invalid. The ITS namespace is at w3.org, so the attribute is not a custom attribute, and HTML does not define it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i custom-attribute-its-namespace.epub -u --advisory` | ERROR HTM_054; INVALID | `custom-attribute-its-namespace.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck custom-attribute-its-namespace.epub -u` | ERROR HTM_054; INVALID | `custom-attribute-its-namespace.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `p` with `xmlns:its="http://www.w3.org/2005/11/its"` and `its:translate="no"` is added. `custom-attribute-w3-domain` does the same with a made-up namespace at w3.org, which both verifiers reject. ITS attributes in their HTML form (`its-loc-note` and the like) are a different case: EPUB 3.4 allows them, EPUB 3.3 does not mention them, and there is no set for them yet.

## History

- 2026-11-13: First version.
