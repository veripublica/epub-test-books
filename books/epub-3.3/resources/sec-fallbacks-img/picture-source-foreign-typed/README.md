# A foreign `source` with `type` (valid)

- Book: `picture-source-foreign-typed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-fallbacks-img/picture-source-foreign-typed/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#127](https://github.com/veripublica/epub-test-books/issues/127)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A source inside picture references a BMP and says its type, and the img is a JPEG. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The `source` names the foreign type, and the `img` is a core media type.

## Question

A `source` inside `picture` references a BMP and says its type, and the `img` is a JPEG. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-fallbacks-img`](https://www.w3.org/TR/epub-33/#sec-fallbacks-img):

> If it is the child of a picture element: it MUST reference core media type resources from its src and srcset attributes, when EPUB creators specify those attributes; and each sibling source element MUST reference a core media type resource from its src and srcset attributes unless it specifies the MIME media type [rfc2046] of a foreign resource in its type attribute.

## Expected result

Valid. The `source` names the foreign type, and the `img` is a core media type.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.40.1 | `epubveri -i picture-source-foreign-typed.epub -u --advisory` | no findings; VALID | `picture-source-foreign-typed.epubveri-0.40.1.txt` |
| epubcheck 5.4.0 | `epubcheck picture-source-foreign-typed.epub -u` | no findings; VALID | `picture-source-foreign-typed.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and JPEG are added, and `content.xhtml` has a `picture` with a typed `source` for the BMP and an `img` for the JPEG.

## History

- 2026-11-09: First version.
