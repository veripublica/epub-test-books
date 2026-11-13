# An SVG content document with a script, without the scripted property

- Book: `property-scripted-svg-document-missing.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-svg-document-missing/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#542](https://github.com/veripublica/epub-test-books/issues/542)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/picture.svg, an SVG content document in the spine, has a script element, and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The SVG content document contains scripting, so its manifest item must have the scripted property.

## Question

The SVG content document `picture.svg` has a `script` element and no `scripted` property. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`scripted`](https://www.w3.org/TR/epub-33/#scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or [html] form elements).

## Expected result

Invalid. The SVG content document contains scripting, so its manifest item must have the scripted property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-scripted-svg-document-missing.epub -u --advisory` | ERROR OPF-014; INVALID | `property-scripted-svg-document-missing.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-svg-document-missing.epub -u` | ERROR OPF-014; INVALID | `property-scripted-svg-document-missing.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The same `picture.svg` as `svg-document-script`, without `properties="scripted"`.

## History

- 2026-11-13: First version.
