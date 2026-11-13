# A foreign `source` without `type`

- Book: `picture-source-foreign-untyped.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-fallbacks-img/picture-source-foreign-untyped/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#128](https://github.com/veripublica/epub-test-books/issues/128)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A source inside picture references a BMP and has no type attribute. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A `source` for a foreign resource must say its type.

## Question

A `source` inside `picture` references a BMP and has no `type` attribute. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fallbacks-img`](https://www.w3.org/TR/epub-33/#sec-fallbacks-img):

> If it is the child of a picture element: it MUST reference core media type resources from its src and srcset attributes, when EPUB creators specify those attributes; and each sibling source element MUST reference a core media type resource from its src and srcset attributes unless it specifies the MIME media type [rfc2046] of a foreign resource in its type attribute.

## Expected result

Invalid. A `source` for a foreign resource must say its type.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i picture-source-foreign-untyped.epub -u --advisory` | ERROR MED_007; INVALID | `picture-source-foreign-untyped.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck picture-source-foreign-untyped.epub -u` | ERROR MED_007; INVALID | `picture-source-foreign-untyped.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and JPEG are added, and `content.xhtml` has a `picture` with an untyped `source` for the BMP and an `img` for the JPEG.

## History

- 2026-11-09: First version.
