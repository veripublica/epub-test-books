# A circular fallback chain

- Book: `fallback-circular.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.3.1.1/fallback-circular/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets
- Issue: [#193](https://github.com/veripublica/epub-test-books/issues/193)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two manifest items name each other as fallback. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The chain does not terminate.

## Question

Two manifest items name each other as `fallback`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.3.1.1`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.3.1.1):

> Fallback chains must terminate; circular references are not permitted.

## Expected result

Invalid. The chain does not terminate.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i fallback-circular.epub -u --advisory` | ERROR OPF-045, USAGE ADV-010, USAGE ADV-010; INVALID | `fallback-circular.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck fallback-circular.epub -u` | ERROR OPF-045; INVALID | `fallback-circular.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE ADV-010 is an `--advisory` finding from epubveri: it says no document uses the item. Every other epubveri finding here is in its default output.

## Build

Two XHTML documents are added to the manifest, each with the other as its `fallback`.

## History

- 2026-11-09: First version.
