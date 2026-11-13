# An NCX `dtb:uid` that differs from the package

- Book: `ncx-uid-mismatch.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.2/ncx-uid-mismatch/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#206](https://github.com/veripublica/epub-test-books/issues/206)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The NCX dtb:uid differs from the package's unique identifier. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The meta must carry the OPF unique ID.

## Question

The NCX `dtb:uid` differs from the package's unique identifier. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.2):

> the only required meta is that which contains a content reference to the OPF unique ID.

## Expected result

Invalid. The meta must carry the OPF unique ID.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i ncx-uid-mismatch.epub -u --advisory` | ERROR NCX-001; INVALID | `ncx-uid-mismatch.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-uid-mismatch.epub -u` | ERROR NCX-001; INVALID | `ncx-uid-mismatch.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/toc.ncx`, `dtb:uid` is given a different value.

## History

- 2026-11-09: First version.
