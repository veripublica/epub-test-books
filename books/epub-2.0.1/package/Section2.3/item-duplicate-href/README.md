# One resource listed twice in the manifest

- Book: `item-duplicate-href.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3/item-duplicate-href/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#192](https://github.com/veripublica/epub-test-books/issues/192)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two manifest items have the same href. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. A resource may be listed once.

## Question

Two manifest items have the same `href`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3):

> A single resource (href) must not be listed in the manifest more than once.

## Expected result

Invalid. A resource may be listed once.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i item-duplicate-href.epub -u --advisory` | ERROR OPF-074, USAGE ADV-010; INVALID | `item-duplicate-href.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck item-duplicate-href.epub -u` | ERROR OPF-074; INVALID | `item-duplicate-href.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, a second `item` for `content.xhtml` is added.

## History

- 2026-11-09: First version.
