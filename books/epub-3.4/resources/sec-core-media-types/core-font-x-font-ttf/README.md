# A TrueType font declared as application/x-font-ttf (valid)

- Book: `core-font-x-font-ttf.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/resources/sec-core-media-types/core-font-x-font-ttf/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 core media types (w3c/epub-specs#667)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml links style.css, whose @font-face rule uses fonts/box.ttf, a two-glyph TrueType font. Its manifest item is application/x-font-ttf. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.4 lists application/x-font-ttf with font/ttf and application/font-sfnt as media types for TrueType fonts.

## Question

`style.css` uses a TrueType font, declared in the manifest as `application/x-font-ttf`. Does a validator accept the book?

## Clause

EPUB 3.4, [`sec-core-media-types`](https://www.w3.org/TR/epub-34/#sec-core-media-types) (3.2 Core media types; Candidate Recommendation Draft, 25 November 2026):

> Publication resources that conform to the MIME media type [rfc2046] specifications defined in the following table MAY be included in EPUB publications without fallbacks when they are used in EPUB content documents and foreign content documents.

> | font/ttf, application/font-sfnt, application/x-font-ttf | [truetype] | TrueType fonts | 3.0 |

## Expected result

Valid. EPUB 3.4 lists `application/x-font-ttf` with `font/ttf` and `application/font-sfnt` as media types for TrueType fonts.

EPUB 3.3 lists only `font/ttf` and `application/font-sfnt`. Fonts need no fallback in either version, so the verdict is valid in both; only the media type's standing changes.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i core-font-x-font-ttf.epub -u --advisory` | USAGE OPF-090, USAGE CSS-028; VALID | `core-font-x-font-ttf.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck core-font-x-font-ttf.epub -u` | USAGE OPF-090, USAGE CSS-028, USAGE CSS-028; VALID | `core-font-x-font-ttf.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

USAGE CSS-028, USAGE OPF-090 do not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<link rel="stylesheet" type="text/css" href="style.css"/>` in the head of `content.xhtml`, `OEBPS/style.css` (`text/css`) with an `@font-face` rule for `fonts/box.ttf`, and `OEBPS/fonts/box.ttf` (`application/x-font-ttf`), the two-glyph font from `scripts/lib/minifont.py`.

## History

- 2026-11-28: First version.
