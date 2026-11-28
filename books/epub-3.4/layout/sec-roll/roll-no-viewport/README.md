# rendition:layout roll, with no viewport in content.xhtml (invalid)

- Book: `roll-no-viewport.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/layout/sec-roll/roll-no-viewport/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 roll layouts (w3c/epub-specs#2791)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:layout to roll. about.xhtml has a viewport meta tag, but content.xhtml has none. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. In a roll, each spine item must be a fixed-layout document with its dimensions set, and an XHTML fixed-layout document gives them in a viewport meta tag.

## Question

The package sets `rendition:layout` to `roll`, but `content.xhtml` has no viewport meta tag. Does a validator reject the book?

## Clause

EPUB 3.4, [`sec-roll`](https://www.w3.org/TR/epub-34/#sec-roll) (6.3.2 Roll; Candidate Recommendation Draft, 25 November 2026):

> When the rendition:layout property is declared in a meta element with the value roll, it indicates that the content is a roll (i.e., reading systems fit the width of each spine itemref to the viewport and display them in a continuous roll with no visible gap).

> The roll layout style applies globally (i.e., for all spine items) and cannot be overridden.

> When a roll layout is declared, each spine item MUST reference a fixed-layout document. The dimensions of each document MUST be set as defined in 7.3.2 Fixed-layout document dimensions.

EPUB 3.4, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-34/#sec-fxl-icb-html) (in 7.3.2 Fixed-layout document dimensions; Candidate Recommendation Draft, 25 November 2026):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag

## Expected result

Invalid. In a roll each spine item must be a fixed-layout document whose dimensions are set as 7.3.2 says, and for XHTML that is a viewport meta tag with a height and a width. `content.xhtml` has none.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i roll-no-viewport.epub -u --advisory` | ERROR HTM-046; INVALID | `roll-no-viewport.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck roll-no-viewport.epub -u` | ERROR HTM-046; INVALID | `roll-no-viewport.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the EPUB 3 template, with `rendition:layout` `roll`. `about.xhtml` has the viewport meta tag; `content.xhtml` has none.

## History

- 2026-11-28: First version.
