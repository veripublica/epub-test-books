# Content MathML in an annotation (valid)

- Book: `mathml-annotation-content.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-mathml/mathml-annotation-content/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the content documents section
- Issue: [#158](https://github.com/veripublica/epub-test-books/issues/158)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A math element holds Content MathML in an annotation-xml with the required encoding and name. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is the form the clause requires.

## Question

A `math` element holds Content MathML in an `annotation-xml` with the required `encoding` and `name`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-xhtml-mathml`](https://www.w3.org/TR/epub-33/#sec-xhtml-mathml):

> When EPUB creators include Content MathML per the previous condition, they MUST set the given annotation-xml element's encoding attribute to either of the functionally-equivalent values MathML-Content or application/mathml-content+xml, and the name attribute to contentequiv.

## Expected result

Valid. This is the form the clause requires.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i mathml-annotation-content.epub -u --advisory` | no findings; VALID | `mathml-annotation-content.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck mathml-annotation-content.epub -u` | no findings; VALID | `mathml-annotation-content.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, a `math` element with `semantics` and `annotation-xml` is added, and the manifest item gets the `mathml` property.

## History

- 2026-11-09: First version.
