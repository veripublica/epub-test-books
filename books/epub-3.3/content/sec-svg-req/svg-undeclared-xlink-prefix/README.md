# An SVG content document that uses the xlink prefix without declaring it

- Book: `svg-undeclared-xlink-prefix.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-svg-req/svg-undeclared-xlink-prefix/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/picture.svg has a use element with xlink:href, and the xlink prefix is not declared. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. An undeclared prefix makes the file not namespace-well-formed, so it is not a conformant XML 1.0 document under Namespaces in XML.

## Question

`picture.svg`, in the spine, uses `xlink:href` without declaring `xlink`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xml-constraints`](https://www.w3.org/TR/epub-33/#sec-xml-constraints):

> MUST be a conformant XML 1.0 Document as defined in Conformance of Documents [xml-names].

EPUB 3.3, [`sec-svg-req`](https://www.w3.org/TR/epub-33/#sec-svg-req):

> An SVG content document MUST be a conforming SVG stand-alone file [svg] and conform to all content conformance constraints expressed in 6.2.3 Restrictions on SVG.

## Expected result

Invalid. An undeclared prefix makes the file not namespace-well-formed, so it is not a conformant XML 1.0 document under Namespaces in XML.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-undeclared-xlink-prefix.epub -u --advisory` | FATAL RSC-016; INVALID | `svg-undeclared-xlink-prefix.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-undeclared-xlink-prefix.epub -u` | FATAL RSC-016; INVALID | `svg-undeclared-xlink-prefix.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is in the manifest as `image/svg+xml` and last in the spine. It holds the same picture as `svg-document`, plus `<use xlink:href="#r"/>` with no `xmlns:xlink`.

## History

- 2026-11-13: First version.
