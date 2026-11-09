# A meta element that refines itself

- Book: `refines-self.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/attrdef-refines/refines-self/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the package document section
- Issue: [#44](https://github.com/veripublica/epub-test-books/issues/44)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

One meta element has a refines attribute that points to its own id. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. This is a self-reference. The property is a `schema:` one, like those already in the template, so EPUB puts no limit on what it may refine and the reference is the only defect.

## Question

A `meta` element's `refines` attribute points to that element's own `id`. Does a validator reject it?

## Clause

EPUB 3.3, [`attrdef-refines`](https://www.w3.org/TR/epub-33/#attrdef-refines):

> Refinement chains MUST NOT contain circular references or self-references.

## Expected result

Invalid. This is a self-reference. The property is a `schema:` one, like those already in the template, so EPUB puts no limit on what it may refine and the reference is the only defect.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.38.0 | `epubveri -i refines-self.epub -u --advisory` | ERROR OPF-065; INVALID | `refines-self.epubveri-0.38.0.txt` |
| epubcheck 5.4.0 | `epubcheck refines-self.epub -u` | ERROR OPF-065; INVALID | `refines-self.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `OEBPS/package.opf`, `<meta id="self" refines="#self" property="schema:alternateName">A test book</meta>` is added to the metadata.

## History

- 2026-11-09: First version.
