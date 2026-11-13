# The prefix z3998 used without a declaration

- Book: `z3998-undeclared.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-reserved-prefixes/z3998-undeclared/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml uses epub:type="z3998:fiction" and declares no prefix. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Only msv and prism are reserved for epub:type, so z3998 must be declared.

## Question

`content.xhtml` uses `epub:type="z3998:fiction"` without declaring `z3998`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-reserved-prefixes`](https://www.w3.org/TR/epub-33/#sec-reserved-prefixes):

> EPUB creators MAY use the following reserved prefixes in the epub:type attribute without having to declare them.
>
> | Prefix | URL |
> |---|---|
> | msv | http://www.idpf.org/epub/vocab/structure/magazine/# |
> | prism | http://www.prismstandard.org/specifications/3.0/PRISM_CV_Spec_3.0.htm# |

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr):

> With the exception of reserved prefixes, EPUB creators MUST declare all prefixes used in a document.

## Expected result

Invalid. Only msv and prism are reserved for epub:type, so z3998 must be declared.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i z3998-undeclared.epub -u --advisory` | ERROR OPF-028; INVALID | `z3998-undeclared.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck z3998-undeclared.epub -u` | ERROR OPF-028; INVALID | `z3998-undeclared.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p epub:type="z3998:fiction">Content.</p>`. No `epub:prefix` is added.

## History

- 2026-11-13: First version.
