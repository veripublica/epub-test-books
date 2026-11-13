# An SVG content document with a script, with the scripted property (valid)

- Book: `svg-document-script.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-scripted-content/svg-document-script/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#539](https://github.com/veripublica/epub-test-books/issues/539)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

OEBPS/picture.svg, an SVG content document in the spine, has a script element, and its manifest item has the scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. An SVG content document can be scripted too, and its manifest item says so.

## Question

The SVG content document `picture.svg`, in the spine, has a `script` element and the `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-scripted-content`](https://www.w3.org/TR/epub-33/#sec-scripted-content):

> EPUB content documents MAY contain scripting using the facilities defined for this in the respective underlying specifications ([html] and [svg]).
>
> When an EPUB content document contains scripting, this specification refers to it as a scripted content document. This label also applies to XHTML content documents that contain [html] form elements.

## Expected result

Valid. An SVG content document can be scripted too, and its manifest item says so.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i svg-document-script.epub -u --advisory` | no findings; VALID | `svg-document-script.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-document-script.epub -u` | no findings; VALID | `svg-document-script.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/picture.svg` is a 40 by 40 SVG with a gray `rect` and `<script>let a = 1;</script>`, in the manifest as `image/svg+xml` with `properties="scripted"`, and last in the spine.

## History

- 2026-11-13: First version.
