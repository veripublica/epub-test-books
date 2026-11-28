# rendition:layout roll (valid)

- Book: `roll.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/layout/sec-roll/roll/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 roll layouts (w3c/epub-specs#2791)
- Issue: [#708](https://github.com/veripublica/epub-test-books/issues/708)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The package sets rendition:layout to roll, EPUB 3.4's continuous scrolling layout. Both spine documents, about.xhtml and content.xhtml, have the viewport meta tag width=1200, height=600. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.4 adds roll as a value of rendition:layout. Each spine item is a fixed-layout document, and each gives its dimensions in a viewport meta tag.

## Question

The package sets `rendition:layout` to `roll`, and both spine documents have a viewport meta tag. Does a validator accept the book?

## Clause

EPUB 3.4, [`sec-roll`](https://www.w3.org/TR/epub-34/#sec-roll) (6.3.2 Roll; Candidate Recommendation Draft, 25 November 2026):

> When the rendition:layout property is declared in a meta element with the value roll, it indicates that the content is a roll (i.e., reading systems fit the width of each spine itemref to the viewport and display them in a continuous roll with no visible gap).

> The roll layout style applies globally (i.e., for all spine items) and cannot be overridden.

> When a roll layout is declared, each spine item MUST reference a fixed-layout document. The dimensions of each document MUST be set as defined in 7.3.2 Fixed-layout document dimensions.

EPUB 3.4, [`sec-fxl-icb-html`](https://www.w3.org/TR/epub-34/#sec-fxl-icb-html) (in 7.3.2 Fixed-layout document dimensions; Candidate Recommendation Draft, 25 November 2026):

> For XHTML fixed-layout documents, the initial containing block [css2] is obtained from the REQUIRED height and width definitions in a viewport meta tag

## Expected result

Valid. `roll` is a value of `rendition:layout` in EPUB 3.4. Both spine documents are XHTML fixed-layout documents, and each gives its height and width in a viewport meta tag, `width=1200, height=600`.

In EPUB 3.3 `roll` is not one of the values of `rendition:layout`, so the same book is invalid there.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i roll.epub -u --advisory` | no findings; VALID | `roll.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck roll.epub -u` | no findings; VALID | `roll.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The fixed-layout form of the EPUB 3 template (`scripts/lib/layoutvariants.py`), with `<meta property="rendition:layout">roll</meta>` in place of `pre-paginated`. `about.xhtml` and `content.xhtml` both have `<meta name="viewport" content="width=1200, height=600"/>`.

## History

- 2026-11-28: First version.
