# `rendition:flow` set to `paginated` (valid)

- Book: `flow-paginated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/flow/flow-paginated/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the reflowable layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:flow to paginated. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. `paginated` is one of the four values.

## Question

The package sets `rendition:flow` to `paginated`. Does a validator accept it?

## Clause

EPUB 3.3, [`flow`](https://www.w3.org/TR/epub-33/#flow):

> EPUB creators MUST use one of the following values with the rendition:flow property: paginated […] scrolled-continuous […] scrolled-doc […] auto […]

## Expected result

Valid. `paginated` is one of the four values.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i flow-paginated.epub -u --advisory` | USAGE OBS-001; VALID | `flow-paginated.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck flow-paginated.epub -u` | USAGE OBS-001; VALID | `flow-paginated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:flow` property is outdated. EPUB 3.3 does not deprecate it, but the EPUB 3.4 draft lists it as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

In the EPUB 3 template, `<meta property="rendition:flow">paginated</meta>` is added to the metadata.

## History

- 2026-11-11: First version.
