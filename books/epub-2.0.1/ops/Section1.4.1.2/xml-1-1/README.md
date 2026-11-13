# A content document that declares XML 1.1

- Book: `xml-1-1.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.4.1.2/xml-1-1/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets
- Issue: [#346](https://github.com/veripublica/epub-test-books/issues/346)
- Other clauses: OPS 2.0.1 `Section1.2`, `Section1.3.1`; XML 1.0 (Fourth Edition) `sec-prolog-dtd`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares version="1.1" in its XML declaration. Nothing else in it differs from the template. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A content document must be well-formed XML 1.0, and OPS 2.0.1 means XML 1.0 (Fourth Edition), where the version number can only be 1.0. Section 1.3.1 lets reading systems support XML 1.1; it does not let a content document use it.

## Question

`content.xhtml` starts with `<?xml version="1.1" encoding="UTF-8"?>`. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section1.4.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.4.1.2):

> A conformant XHTML Content Document must meet these conditions:

> it is a well-formed XML document (as defined by XML 1.0); and

OPS 2.0.1, [`Section1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.2):

> An XML Document is a complete and valid XML document as defined in XML 1.0 (Fourth Edition) (http://www.w3.org/TR/2006/REC-xml-20060816/).

[XML 1.0 (Fourth Edition), 2.8 Prolog and Document Type Declaration](https://www.w3.org/TR/2006/REC-xml-20060816/#sec-prolog-dtd):

> [26] VersionNum ::= '1.0'

OPS 2.0.1, [`Section1.3.1`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.3.1):

> Reading Systems may support XML 1.1, but this feature is deprecated in version 2.0.1 (in favor of XML 1.0). Support for XML 1.1 will be removed in the next version of the specification.

## Expected result

Invalid. A content document must be well-formed XML 1.0, and OPS 2.0.1 means XML 1.0 (Fourth Edition), where the version number can only be `1.0`. Section 1.3.1 lets reading systems support XML 1.1; it does not let a content document use it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i xml-1-1.epub -u --advisory` | ERROR HTM-001; INVALID | `xml-1-1.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck xml-1-1.epub -u` | ERROR HTM-001; INVALID | `xml-1-1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, `<?xml version="1.0"` is changed to `<?xml version="1.1"`.

## History

- 2026-11-12: First version.
