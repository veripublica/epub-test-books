# A script inside inline SVG, without the scripted property

- Book: `property-scripted-inline-svg-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-inline-svg-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#543](https://github.com/veripublica/epub-test-books/issues/543)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an inline svg element with a script element inside it. Its manifest item has the svg property, but not scripted. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The script in the embedded SVG is scripting in content.xhtml, so its manifest item must have the scripted property.

## Question

`content.xhtml` has inline SVG with a `script` element, and the `svg` property but not `scripted`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`scripted`](https://www.w3.org/TR/epub-33/#scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or [html] form elements).

## Expected result

Invalid. The script in the embedded SVG is scripting in content.xhtml, so its manifest item must have the scripted property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-scripted-inline-svg-missing.epub -u --advisory` | ERROR OPF-014, USAGE RSC-025; INVALID | `property-scripted-inline-svg-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-inline-svg-missing.epub -u` | ERROR OPF-014; INVALID | `property-scripted-inline-svg-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE RSC-025 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets an inline 40 by 40 `svg` with a gray `rect` and `<script>let a = 1;</script>`, and its manifest item `properties="svg"`.

## History

- 2026-11-13: First version.
