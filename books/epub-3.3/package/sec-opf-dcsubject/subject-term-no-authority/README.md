# A subject with a `term` and no `authority`

- Book: `subject-term-no-authority.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-opf-dcsubject/subject-term-no-authority/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#88](https://github.com/veripublica/epub-test-books/issues/88)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:subject element is refined by term, and no authority refines it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The element specifies no scheme, so it must not have a `term`.

## Question

A `dc:subject` is refined by `term`, and no `authority` refines it. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-opf-dcsubject`](https://www.w3.org/TR/epub-33/#sec-opf-dcsubject):

> The term property MUST NOT be associated with a dc:subject element that does not specify a scheme.

## Expected result

Invalid. The element specifies no scheme, so it must not have a `term`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i subject-term-no-authority.epub -u --advisory` | ERROR RSC-005; INVALID | `subject-term-no-authority.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck subject-term-no-authority.epub -u` | ERROR RSC-005; INVALID | `subject-term-no-authority.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:subject` gets an `id` and a `meta` with `property="term"` refines it.

## History

- 2026-11-09: First version.
