# An SVG `script` inside a content document

- Book: `svg-inline-script.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.5.1/svg-inline-script/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, for the OPS 2.0.1 content document sets; parked on 2026-11-11 while both verifiers missed it, shipped after epubveri reports it
- Issue: [#617](https://github.com/veripublica/epub-test-books/issues/617)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an svg element, in the SVG namespace, that holds a script element and a gray square. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. SVG scripting must not be used in OPS content, and here the svg holds a script element.

## Question

In `content.xhtml`, an inline `svg` holds a `script` element. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.5.1`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.5.1):

> The only exception is that since OPS is not targeting interactive content. SVG animation and scripting features are not supported and must not be used by publication authors; a Reading System should not render such content.

## Expected result

Invalid. SVG scripting must not be used in OPS content, and here the `svg` holds a `script` element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.48.0 | `epubveri -i svg-inline-script.epub -u --advisory` | ERROR RSC-005; INVALID | `svg-inline-script.epubveri-0.48.0.txt` |
| epubcheck 5.4.0 | `epubcheck svg-inline-script.epub -u` | no findings; VALID | `svg-inline-script.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1780](https://github.com/w3c/epubcheck/issues/1780).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in a `div`, `<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 40 40"><script type="text/ecmascript">var a = 1;</script><rect width="40" height="40" fill="gray"/></svg>`.

## History

- 2026-11-11: First version, parked.
- 2026-11-15: Measured on epubveri 0.43.0 and added to the library.
