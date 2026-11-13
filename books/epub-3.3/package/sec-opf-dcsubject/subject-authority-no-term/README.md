# A subject with an `authority` and no `term`

- Book: `subject-authority-no-term.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-opf-dcsubject/subject-authority-no-term/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#87](https://github.com/veripublica/epub-test-books/issues/87)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The dc:subject element is refined by authority, and no term refines it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A scheme is identified, so a `term` is required.

## Question

A `dc:subject` is refined by `authority`, and no `term` refines it. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-opf-dcsubject`](https://www.w3.org/TR/epub-33/#sec-opf-dcsubject):

> When a scheme is identified, EPUB creators MUST associate a subject code using the term property.

## Expected result

Invalid. A scheme is identified, so a `term` is required.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i subject-authority-no-term.epub -u --advisory` | ERROR RSC-005; INVALID | `subject-authority-no-term.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck subject-authority-no-term.epub -u` | ERROR RSC-005; INVALID | `subject-authority-no-term.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `dc:subject` gets an `id` and a `meta` with `property="authority"` refines it.

## History

- 2026-11-09: First version.
