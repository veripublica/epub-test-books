# `media:active-class` and `media:playback-active-class` with no style sheet (valid)

- Book: `active-class-no-css.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/media-overlays/sec-docs-assoc-style/active-class-no-css/build.py`
- Origin: built here
- Expected: valid
- Marks: epubcheck: wrong error
- Asked for by: the maintainer, to cover the media overlays section
- Issue: [#701](https://github.com/veripublica/epub-test-books/issues/701)
- Other clauses: EPUB 3.3 `conformance`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book is the EPUB 3 template with one media overlay: content.smil pairs the paragraph p1 of content.xhtml with audio.mp3, three seconds of silent MP3, from 0:00:00 to 0:00:03. content.xhtml's manifest item has media-overlay="mo", and the package gives the overlay's duration and the total, both 0:00:03. In this set: The package also declares media:active-class active and media:playback-active-class playing, but content.xhtml links no style sheet.

Expected result: Valid. EPUB 3.3 says that EPUB creators "must ensure" that a content document with a media overlay includes a CSS style sheet. That "must" is in lowercase, and EPUB 3.3 makes its key words requirements only when they are in all capitals.

## Question

The package declares `media:active-class` and `media:playback-active-class`, and `content.xhtml`, which has a media overlay, links no style sheet. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-docs-assoc-style`](https://www.w3.org/TR/epub-33/#sec-docs-assoc-style):

> When used, EPUB creators MUST declare the class names in the package document using the active-class and playback-active-class properties.

> EPUB creators MAY define any CSS properties for the specified CSS classes but must ensure that each EPUB content document with an associated media overlay document includes a CSS stylesheet (either embedded or linked) containing the class definitions.

EPUB 3.3, [`conformance`](https://www.w3.org/TR/epub-33/#conformance):

> The key words MAY, MUST, MUST NOT, OPTIONAL, RECOMMENDED, REQUIRED, SHOULD, and SHOULD NOT in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

## Expected result

Valid. The class names are declared in the package document, one in each property, as the MUST asks. The sentence about the style sheet says "must ensure" in lowercase. It is the only lowercase "must" in the section, and EPUB 3.3 reads its key words as requirements "when, and only when, they appear in all capitals". So a content document with a media overlay and no style sheet breaks no requirement. A reading system then styles the active element its own way, or not at all, as the section says: "In the absence of such definitions reading systems might provide their own styling, or no styling at all."

Whether the lowercase "must" is meant is asked in [w3c/epub-specs#3125](https://github.com/w3c/epub-specs/issues/3125). Until it is answered, the book follows the text as written.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i active-class-no-css.epub -u --advisory` | USAGE ADV-026; VALID | `active-class-no-css.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck active-class-no-css.epub -u` | ERROR CSS-030; INVALID | `active-class-no-css.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result: it reports the content document with no CSS at usage level (USAGE ADV-026), which does not change the verdict. epubcheck does not: it reports the content document with no CSS as an error (CSS-030).

- **epubcheck: wrong error.** [w3c/epubcheck#1788](https://github.com/w3c/epubcheck/issues/1788).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The book is the EPUB 3 template with one media overlay: `content.smil` pairs the paragraph `p1` of `content.xhtml` with `audio.mp3`, three seconds of silent MP3, from 0:00:00 to 0:00:03. `content.xhtml`'s manifest item has `media-overlay="mo"`, and the package gives the overlay's duration and the total, both `0:00:03`. `audio.mp3` comes from `silent_mp3()` in `scripts/lib/minimedia.py`. Then: The package also declares `media:active-class` `active` and `media:playback-active-class` `playing`, but `content.xhtml` links no style sheet and has no `style` element.

## History

- 2026-11-28: First version.
