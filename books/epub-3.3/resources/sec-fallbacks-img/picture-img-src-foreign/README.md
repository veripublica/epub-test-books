# A foreign `img` inside `picture`

- Book: `picture-img-src-foreign.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-fallbacks-img/picture-img-src-foreign/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#126](https://github.com/veripublica/epub-test-books/issues/126)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

An img inside picture references a BMP that has a manifest fallback. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. Inside `picture`, the `img` must reference a core media type resource. A manifest fallback does not change that.

## Question

An `img` inside `picture` references a BMP that has a manifest fallback. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-fallbacks-img`](https://www.w3.org/TR/epub-33/#sec-fallbacks-img):

> If it is the child of a picture element: it MUST reference core media type resources from its src and srcset attributes, when EPUB creators specify those attributes; and each sibling source element MUST reference a core media type resource from its src and srcset attributes unless it specifies the MIME media type [rfc2046] of a foreign resource in its type attribute.

## Expected result

Invalid. Inside `picture`, the `img` must reference a core media type resource. A manifest fallback does not change that.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i picture-img-src-foreign.epub -u --advisory` | ERROR MED-003, USAGE OBS-001, USAGE OPF-097; INVALID | `picture-img-src-foreign.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck picture-img-src-foreign.epub -u` | ERROR MED-003, USAGE OPF-097, USAGE OBS-001; INVALID | `picture-img-src-foreign.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-097 says no content document references an item that the book lists. That follows from the change and is not a second defect. USAGE OBS-001 says a manifest content fallback is outdated. That is the feature this book uses, not a defect.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A generated BMP and JPEG are added, the BMP's `fallback` names the JPEG, and `content.xhtml` has a `picture` whose `img` shows the BMP.

## History

- 2026-11-09: First version.
