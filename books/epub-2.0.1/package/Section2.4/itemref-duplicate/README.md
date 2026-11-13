# One manifest item in the spine twice

- Book: `itemref-duplicate.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4/itemref-duplicate/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#199](https://github.com/veripublica/epub-test-books/issues/199)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The spine references the content document twice. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. An item may appear once.

## Question

The spine references the content document twice. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4):

> a specific spine item (from the perspective of its id attribute value in manifest) must not appear more than once in spine.

## Expected result

Invalid. An item may appear once.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i itemref-duplicate.epub -u --advisory` | ERROR OPF-034; INVALID | `itemref-duplicate.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck itemref-duplicate.epub -u` | ERROR OPF-034; INVALID | `itemref-duplicate.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, a second `itemref` for the content document is added.

## History

- 2026-11-09: First version.
