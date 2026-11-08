# Rootfiles with no rootfile

- Book: `no-rootfile.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-container.xml-rootfiles-elem/no-rootfile/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#17](https://github.com/veripublica/epub-test-books/issues/17)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

META-INF/container.xml has an empty rootfiles element, so it declares no package document. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. `rootfiles` must hold at least one `rootfile`.

## Question

container.xml has an empty `rootfiles` element. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-container.xml-rootfiles-elem`](https://www.w3.org/TR/epub-33/#sec-container.xml-rootfiles-elem):

> Content Model: rootfile [1 or more]

## Expected result

Invalid. `rootfiles` must hold at least one `rootfile`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i no-rootfile.epub -u --advisory` | ERROR RSC-003; INVALID | `no-rootfile.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck no-rootfile.epub -u` | ERROR RSC-003; INVALID | `no-rootfile.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The `rootfile` element is removed from `META-INF/container.xml`, leaving `<rootfiles>` empty.

## History

- 2026-11-08: First version.
