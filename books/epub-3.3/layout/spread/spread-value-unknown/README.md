# `rendition:spread` with an unknown value

- Book: `spread-value-unknown.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/spread/spread-value-unknown/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#248](https://github.com/veripublica/epub-test-books/issues/248)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:spread to always, which is not one of its values. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Invalid. `always` is not one of `none`, `landscape`, `portrait`, `both` or `auto`.

## Question

The package sets `rendition:spread` to `always`, which is not one of its values. Does a validator reject it?

## Clause

EPUB 3.3, [`spread`](https://www.w3.org/TR/epub-33/#spread):

> EPUB creators MUST use one of the following values with the rendition:spread property: none […] landscape […] portrait (deprecated) […] both […] auto […]

## Expected result

Invalid. `always` is not one of `none`, `landscape`, `portrait`, `both` or `auto`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i spread-value-unknown.epub -u --advisory` | ERROR RSC-005, USAGE OBS-001; INVALID | `spread-value-unknown.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck spread-value-unknown.epub -u` | USAGE OBS-001, ERROR RSC-005; INVALID | `spread-value-unknown.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OBS-001 says the `rendition:spread` property is outdated. EPUB 3.3 deprecates only its `portrait` value, but the EPUB 3.4 draft lists the property as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `<meta property="rendition:spread">always</meta>`.

## History

- 2026-11-11: First version.
