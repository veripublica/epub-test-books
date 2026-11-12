# A link into META-INF

- Book: `link-into-meta-inf.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container-file-and-dir-structure/link-into-meta-inf/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#34](https://github.com/veripublica/epub-test-books/issues/34)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The content document has a hyperlink to META-INF/container.xml, which is in the container. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A publication must not reference files in META-INF, and an existing target does not make the link allowed.

## Question

The content document links to `META-INF/container.xml`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container-file-and-dir-structure`](https://www.w3.org/TR/epub-33/#sec-container-file-and-dir-structure):

> EPUB creators MUST NOT reference files in the META-INF directory from an EPUB publication.

## Expected result

Invalid. A publication must not reference files in META-INF, and an existing target does not make the link allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i link-into-meta-inf.epub -u --advisory` | ERROR RSC-008; INVALID | `link-into-meta-inf.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck link-into-meta-inf.epub -u` | ERROR RSC-008; INVALID | `link-into-meta-inf.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

epubveri 0.37.1 gave no finding here and called this book VALID. 0.38.0 is the first release with the fix.

## Build

`OEBPS/content.xhtml` gains `<a href="../META-INF/container.xml">A link</a>` at the end of its paragraph.

## History

- 2026-11-08: First version.
