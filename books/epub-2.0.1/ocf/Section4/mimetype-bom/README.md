# A `mimetype` file that starts with a byte order mark

- Book: `mimetype-bom.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ocf/Section4/mimetype-bom/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubsana, to test its repair of these books (note of 2026-11-22)
- Issue: [#695](https://github.com/veripublica/epub-test-books/issues/695)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype file starts with the UTF-8 byte order mark (EF BB BF), then application/epub+zip. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The file must hold the ASCII string and nothing else. The byte order mark is three bytes outside ASCII, before it.

## Question

The `mimetype` file starts with the UTF-8 byte order mark, then `application/epub+zip`. Does a validator reject the book?

## Clause

OCF 2.0.1, [section 4](https://idpf.org/epub/20/spec/OCF_2.0.1_draft.doc) (ZIP Container; Recommended Specification, 4 September 2010):

> The first file in the ZIP Container MUST be a file by the ASCII name of ‘mimetype’ which holds the MIME type for the ZIP Container (i.e., “application/epub+zip” as an ASCII string; no padding, white-space or case change). The file MUST be neither compressed nor encrypted and there MUST NOT be an extra field in its ZIP header.

OCF 2.0.1 does not name the byte order mark, as EPUB 3.3 does (`sec-zip-container-mime`). The expected result follows from "as an ASCII string; no padding".

## Expected result

Invalid. The file must hold the ASCII string and nothing else. The byte order mark is three bytes outside ASCII, before it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i mimetype-bom.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-bom.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-bom.epub -u` | ERROR PKG-007; INVALID | `mimetype-bom.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 2 template's files, written as a container by `scripts/lib/ocf2variants.py`. The `mimetype` entry holds `EF BB BF` and then `application/epub+zip` (23 bytes), stored, first in the container.

## History

- 2026-11-22: First version.
