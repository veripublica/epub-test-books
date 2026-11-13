# An NCX item with a `fallback`

- Book: `ncx-with-fallback.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/package/Section2.4.1.2/ncx-with-fallback/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to start the EPUB 2.0.1 sets; parked on 2026-11-09 until #27's comments had their time, built on 2026-11-13 for the release after 15 November
- Issue: [#609](https://github.com/veripublica/epub-test-books/issues/609)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest item for the NCX has a fallback attribute. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The NCX item must carry no fallback information.

## Question

The manifest item for the NCX has a `fallback`. Does a validator reject it?

## Clause

OPF 2.0.1, [`Section2.4.1.2`](https://idpf.org/epub/20/spec/OPF_2.0.1_draft.htm#Section2.4.1.2):

> The NCX-referencing item must not contain any fallback information

## Expected result

Invalid. The NCX item must carry no fallback information.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i ncx-with-fallback.epub -u --advisory` | ERROR SPEC-003; INVALID | `ncx-with-fallback.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck ncx-with-fallback.epub -u` | no findings; VALID | `ncx-with-fallback.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it gives no finding.

- **epubcheck: missed.** [w3c/epubcheck#1761](https://github.com/w3c/epubcheck/issues/1761).

SPEC-003 is epubveri's id for a specification rule that epubcheck has no id for. It is in epubveri's default output, not an `--advisory` finding. Every epubveri finding here is in its default output.

## Build

In `OEBPS/package.opf`, the NCX item gets `fallback="content"`.

## History

- 2026-11-09: First version, parked.
- 2026-11-13: Measured on epubveri 0.42.0 and added to the library.
