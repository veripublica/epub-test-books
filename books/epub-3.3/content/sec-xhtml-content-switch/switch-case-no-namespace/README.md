# An epub:case without required-namespace

- Book: `switch-case-no-namespace.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-content-switch/switch-case-no-namespace/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an epub:switch whose case element has no required-namespace attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. required-namespace is a required attribute of case.

## Question

`content.xhtml` has an `epub:case` without `required-namespace`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-content-switch`](https://www.w3.org/TR/epub-33/#sec-xhtml-content-switch):

> Use of the element is deprecated. Refer to the switch element definition in [epubcontentdocs-301] for more information.

EPUB Content Documents 3.0.1, [2.1.3.3.2.2 The epub:case Element](https://idpf.org/epub/301/spec/epub-contentdocs.html) (Recommended Specification, 26 June 2014):

> required-namespace [required] An extension identifier in URI form [RFC2046] that identifies the XML vocabulary or extension that the Reading System must support in order to process the content of the case element.

## Expected result

Invalid. required-namespace is a required attribute of case.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i switch-case-no-namespace.epub -u --advisory` | ERROR RSC-005, WARNING RSC-017, USAGE ACC-009; INVALID | `switch-case-no-namespace.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-case-no-namespace.epub -u` | ERROR RSC-005, USAGE ACC-009, WARNING RSC-017; INVALID | `switch-case-no-namespace.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE ACC-009, WARNING RSC-017 do not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an `epub:switch` with one `epub:case` holding a MathML `math` element and no `required-namespace`, and an `epub:default` with a `p`, and its manifest item `properties="mathml switch"`.

## History

- 2026-11-13: First version.
