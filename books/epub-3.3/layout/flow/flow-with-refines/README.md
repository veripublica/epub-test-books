# `rendition:flow` with `refines`

- Book: `flow-with-refines.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/flow/flow-with-refines/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: [#285](https://github.com/veripublica/epub-test-books/issues/285)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The rendition:flow meta element has refines="#content", pointing at the content document's manifest item. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The property must not be declared with the `refines` attribute; a spine override is the way to set it for one document.

## Question

The `rendition:flow` meta element has `refines="#content"`, pointing at the content document's manifest item. Does a validator reject it?

## Clause

EPUB 3.3, [`flow`](https://www.w3.org/TR/epub-33/#flow):

> EPUB creators MUST NOT declare the rendition:flow property more than once. They also MUST NOT declare the property using the refines attribute.

## Expected result

Invalid. The property must not be declared with the `refines` attribute; a spine override is the way to set it for one document.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i flow-with-refines.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001; INVALID | `flow-with-refines.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck flow-with-refines.epub -u` | USAGE OBS-001, ERROR RSC-005; INVALID | `flow-with-refines.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:flow` property is outdated. EPUB 3.3 does not deprecate it, but the EPUB 3.4 draft lists it as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:flow" refines="#content">paginated</meta>` is added to the metadata.

## History

- 2026-11-11: First version.
