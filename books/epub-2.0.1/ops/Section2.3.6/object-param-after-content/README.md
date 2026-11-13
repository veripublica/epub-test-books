# A `param` after the content of an `object`

- Book: `object-param-after-content.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.3.6/object-param-after-content/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets
- Issue: [#347](https://github.com/veripublica/epub-test-books/issues/347)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an object element of a JPEG image whose text, A small gray square., comes before its param element. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. param must come before the renderable content of the object, and here the text comes first.

## Question

In `content.xhtml`, an `object` holds its descriptive text first and a `param` element after it. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.3.6`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.3.6):

> The param element must only appear before the renderable content of an object.

## Expected result

Invalid. `param` must come before the renderable content of the `object`, and here the text comes first.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i object-param-after-content.epub -u --advisory` | ERROR RSC-005; INVALID | `object-param-after-content.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck object-param-after-content.epub -u` | ERROR RSC-005; INVALID | `object-param-after-content.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/image.jpg` is added to the manifest, and `content.xhtml` holds `<object data="image.jpg" type="image/jpeg">A small gray square.<param name="a" value="b"/></object>`.

## History

- 2026-11-12: First version.
