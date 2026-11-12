# Two `meta` elements refining each other

- Book: `refines-cycle.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-refines/refines-cycle/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to continue the package document section
- Issue: [#64](https://github.com/veripublica/epub-test-books/issues/64)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

Two meta elements refine each other. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. This is a circular reference.

## Question

Two `meta` elements refine each other. Does a validator reject it?

## Clause

EPUB 3.3, [`attrdef-refines`](https://www.w3.org/TR/epub-33/#attrdef-refines):

> Refinement chains MUST NOT contain circular references or self-references.

## Expected result

Invalid. This is a circular reference.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i refines-cycle.epub -u --advisory` | ERROR OPF-065; INVALID | `refines-cycle.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck refines-cycle.epub -u` | ERROR OPF-065; INVALID | `refines-cycle.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, two `meta` elements are added with `refines` pointing at each other.

## History

- 2026-11-09: First version.
