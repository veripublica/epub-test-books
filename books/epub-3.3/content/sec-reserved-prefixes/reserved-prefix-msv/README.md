# The reserved prefix msv used without a declaration (valid)

- Book: `reserved-prefix-msv.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-reserved-prefixes/reserved-prefix-msv/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#571](https://github.com/veripublica/epub-test-books/issues/571)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml uses epub:type="msv:article" and declares no prefix. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. msv is one of the two prefixes reserved for epub:type, so it needs no declaration.

## Question

`content.xhtml` uses `epub:type="msv:article"` without declaring `msv`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-reserved-prefixes`](https://www.w3.org/TR/epub-33/#sec-reserved-prefixes):

> EPUB creators MAY use reserved prefixes in attributes that expect a property value without declaring them in a prefix attribute.
>
> EPUB creators MAY use the following reserved prefixes in the epub:type attribute without having to declare them.
>
> | Prefix | URL |
> |---|---|
> | msv | http://www.idpf.org/epub/vocab/structure/magazine/# |
> | prism | http://www.prismstandard.org/specifications/3.0/PRISM_CV_Spec_3.0.htm# |

## Expected result

Valid. msv is one of the two prefixes reserved for epub:type, so it needs no declaration.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i reserved-prefix-msv.epub -u --advisory` | WARNING OPF-086c; VALID | `reserved-prefix-msv.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck reserved-prefix-msv.epub -u` | WARNING OPF-086c; VALID | `reserved-prefix-msv.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-086c does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p epub:type="msv:article">Content.</p>`. No `epub:prefix` is added.

## History

- 2026-11-13: First version.
