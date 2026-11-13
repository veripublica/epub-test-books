# An epub:switch without a default

- Book: `switch-no-default.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-content-switch/switch-no-default/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an epub:switch with one case and no default element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The content model asks for exactly one default after the cases.

## Question

`content.xhtml` has an `epub:switch` with no `epub:default`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-content-switch`](https://www.w3.org/TR/epub-33/#sec-xhtml-content-switch):

> Use of the element is deprecated. Refer to the switch element definition in [epubcontentdocs-301] for more information.

EPUB Content Documents 3.0.1, [2.1.3.3.2.1 The epub:switch Element](https://idpf.org/epub/301/spec/epub-contentdocs.html) (Recommended Specification, 26 June 2014):

> Content Model In this order: case [1 or more], default [exactly 1].

## Expected result

Invalid. The content model asks for exactly one default after the cases.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i switch-no-default.epub -u --advisory` | ERROR RSC-005, WARNING RSC-017, USAGE ACC-009; INVALID | `switch-no-default.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-no-default.epub -u` | USAGE ACC-009, ERROR RSC-005, WARNING RSC-017; INVALID | `switch-no-default.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE ACC-009, WARNING RSC-017 do not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an `epub:switch` with one `epub:case` holding a MathML `math` element and `required-namespace`, and no `epub:default`, and its manifest item `properties="mathml switch"`.

## History

- 2026-11-13: First version.
