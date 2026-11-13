# `rendition:spread` set to the deprecated `portrait`

- Book: `spread-portrait-deprecated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/layout/spread/spread-portrait-deprecated/build.py`
- Origin: built here
- Expected: valid, with a warning for the deprecated value
- Marks: none
- Asked for by: the maintainer, to start the fixed layouts section
- Issue: [#249](https://github.com/veripublica/epub-test-books/issues/249)
- Other clauses: `deprecated`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:spread to portrait, a deprecated value. Everything else is the fixed-layout form of the EPUB 3 template (rendition:layout set to pre-paginated, and a viewport of width=1200, height=600 in each document), which raises no finding.

Expected result: Valid, because using a deprecated feature is a SHOULD NOT, not a MUST NOT. A validator should warn about it: EPUB 3.3 says conformance checkers should alert EPUB creators to deprecated features.

## Question

The package sets `rendition:spread` to `portrait`, a deprecated value. What does a validator report?

## Clause

EPUB 3.3, [`spread`](https://www.w3.org/TR/epub-33/#spread):

> EPUB creators MUST use one of the following values with the rendition:spread property: none […] landscape […] portrait (deprecated) […] both […] auto […]

> The use of spreads only in portrait orientation is deprecated. EPUB creators should use the value "both" instead, as spreads that are readable in portrait orientation are also readable in landscape.

EPUB 3.3, [`deprecated`](https://www.w3.org/TR/epub-33/#deprecated):

> If this specification designates a feature as deprecated, EPUB creators SHOULD NOT use the feature in their EPUB publications.

## Expected result

Valid, because using a deprecated feature is a SHOULD NOT, not a MUST NOT. A validator should warn about it: EPUB 3.3 says conformance checkers should alert EPUB creators to deprecated features.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i spread-portrait-deprecated.epub -u --advisory` | WARNING OPF-086, USAGE OBS-001; VALID | `spread-portrait-deprecated.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck spread-portrait-deprecated.epub -u` | USAGE OBS-001, WARNING OPF-086; VALID | `spread-portrait-deprecated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-086 is the alert for the deprecated value. USAGE OBS-001 says the `rendition:spread` property is outdated. EPUB 3.3 deprecates only its `portrait` value, but the EPUB 3.4 draft lists the property as outdated (change log, 18 December 2025); the message is at usage level, so it does not change the verdict.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The fixed-layout form of the template (`scripts/lib/layoutvariants.py`: `rendition:layout` `pre-paginated` in the metadata, `<meta name="viewport" content="width=1200, height=600"/>` in `about.xhtml` and `content.xhtml`), and `<meta property="rendition:spread">portrait</meta>`.

## History

- 2026-11-11: First version.
