# `rendition:flow` declared twice

- Book: `flow-twice.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/flow/flow-twice/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#284](https://github.com/veripublica/epub-test-books/issues/284)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package declares rendition:flow twice, as paginated and as scrolled-doc. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The property is declared more than once.

## Question

The package declares `rendition:flow` twice, as `paginated` and as `scrolled-doc`. Does a validator reject it?

## Clause

EPUB 3.3, [`flow`](https://www.w3.org/TR/epub-33/#flow):

> EPUB creators MUST NOT declare the rendition:flow property more than once. They also MUST NOT declare the property using the refines attribute.

## Expected result

Invalid. The property is declared more than once.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i flow-twice.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001, USAGE OBS-001; INVALID | `flow-twice.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck flow-twice.epub -u` | USAGE OBS-001, USAGE OBS-001, ERROR RSC-005; INVALID | `flow-twice.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 (once for each element) says the `rendition:flow` property is outdated. EPUB 3.3 does not deprecate it, but the EPUB 3.4 draft lists it as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, two `rendition:flow` meta elements, `paginated` and `scrolled-doc`, are added to the metadata.

## History

- 2026-11-11: First version.
