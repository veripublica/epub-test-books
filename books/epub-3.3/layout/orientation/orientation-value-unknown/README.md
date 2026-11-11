# `rendition:orientation` with an unknown value

- Book: `orientation-value-unknown.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/orientation/orientation-value-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:orientation to vertical, which is not one of its values. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. `vertical` is not `landscape`, `portrait` or `auto`.

## Question

The package sets `rendition:orientation` to `vertical`, which is not one of its values. Does a validator reject it?

## Clause

EPUB 3.3, [`orientation`](https://www.w3.org/TR/epub-33/#orientation):

> EPUB creators MUST use one of the following values with the rendition:orientation property: landscape […] portrait […] auto […]

## Expected result

Invalid. `vertical` is not `landscape`, `portrait` or `auto`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i orientation-value-unknown.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001; INVALID | `orientation-value-unknown.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck orientation-value-unknown.epub -u` | USAGE OBS-001, ERROR RSC-005; INVALID | `orientation-value-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:orientation` property is outdated. EPUB 3.3 does not deprecate it; it is the feature this book uses, not a defect, and the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `<meta property="rendition:orientation">vertical</meta>`.

## History

- 2026-11-11: First version.
