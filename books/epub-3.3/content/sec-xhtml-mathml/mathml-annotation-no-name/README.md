# A Content MathML annotation without `name`

- Book: `mathml-annotation-no-name.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-mathml/mathml-annotation-no-name/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#159](https://github.com/veripublica/epub-test-books/issues/159)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An annotation-xml holding Content MathML has no name attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The `name` attribute must be `contentequiv`.

## Question

An `annotation-xml` holding Content MathML has no `name` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-mathml`](https://www.w3.org/TR/epub-33/#sec-xhtml-mathml):

> When EPUB creators include Content MathML per the previous condition, they MUST set the given annotation-xml element's encoding attribute to either of the functionally-equivalent values MathML-Content or application/mathml-content+xml, and the name attribute to contentequiv.

## Expected result

Invalid. The `name` attribute must be `contentequiv`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i mathml-annotation-no-name.epub -u --advisory` | ERROR RSC-005; INVALID | `mathml-annotation-no-name.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck mathml-annotation-no-name.epub -u` | ERROR RSC-005; INVALID | `mathml-annotation-no-name.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `math` element with an `annotation-xml` without `name` is added, and the manifest item gets the `mathml` property.

## History

- 2026-11-09: First version.
