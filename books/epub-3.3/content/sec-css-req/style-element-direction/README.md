# `direction: rtl` in a `style` element

- Book: `style-element-direction.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-css-req/style-element-direction/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: styloria, its proposal 4 (vertical and right-to-left books, 2026-10-28)
- Issue: [#428](https://github.com/veripublica/epub-test-books/issues/428)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The head of content.xhtml holds <style>p { direction: rtl; }</style>. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The style element holds a CSS style sheet, and that style sheet includes the direction property.

## Question

The head of `content.xhtml` holds `<style>p { direction: rtl; }</style>`. Does a validator reject the book?

## Clause

HTML Living Standard, [`the-style-element`](https://html.spec.whatwg.org/multipage/semantics.html#the-style-element) (4.2.6 The style element; checked 2026-11-12):

> The style element allows authors to embed CSS style sheets in their documents.

EPUB 3.3, [`sec-css-req`](https://www.w3.org/TR/epub-33/#sec-css-req):

> It MUST NOT include the direction property [css-writing-modes-3].

## Expected result

Invalid. The `style` element holds a CSS style sheet, and that style sheet includes the `direction` property.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i style-element-direction.epub -u --advisory` | ERROR CSS-001; INVALID | `style-element-direction.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck style-element-direction.epub -u` | ERROR CSS-001; INVALID | `style-element-direction.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the head gets `<style>p { direction: rtl; }</style>`.

## History

- 2026-11-12: First version.
