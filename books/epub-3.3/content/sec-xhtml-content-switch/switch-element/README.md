# An epub:switch element (valid)

- Book: `switch-element.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-content-switch/switch-element/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#577](https://github.com/veripublica/epub-test-books/issues/577)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an epub:switch with one case (MathML, with required-namespace) and a default. Its manifest item has the mathml and switch properties. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The element is deprecated, which is a SHOULD NOT, and this one follows the EPUB 3.0.1 content model. A warning would fit.

## Question

`content.xhtml` has a well-formed `epub:switch` and the `switch` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-content-switch`](https://www.w3.org/TR/epub-33/#sec-xhtml-content-switch):

> Use of the element is deprecated. Refer to the switch element definition in [epubcontentdocs-301] for more information.

EPUB 3.3, [`deprecated`](https://www.w3.org/TR/epub-33/#deprecated):

> If this specification designates a feature as deprecated, EPUB creators SHOULD NOT use the feature in their EPUB publications.

EPUB Content Documents 3.0.1, [2.1.3.3.2.1 The epub:switch Element](https://idpf.org/epub/301/spec/epub-contentdocs.html) (Recommended Specification, 26 June 2014):

> Content Model In this order: case [1 or more], default [exactly 1].

## Expected result

Valid. The element is deprecated, which is a SHOULD NOT, and this one follows the EPUB 3.0.1 content model. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i switch-element.epub -u --advisory` | WARNING RSC-017, USAGE ACC-009; VALID | `switch-element.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-element.epub -u` | USAGE ACC-009, WARNING RSC-017; VALID | `switch-element.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE ACC-009, WARNING RSC-017 do not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an `epub:switch` with one `epub:case` holding a MathML `math` element and `required-namespace`, and an `epub:default` with a `p`, and its manifest item `properties="mathml switch"`.

## History

- 2026-11-13: First version.
