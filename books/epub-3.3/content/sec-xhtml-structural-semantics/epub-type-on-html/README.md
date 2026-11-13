# epub:type on the html element (valid)

- Book: `epub-type-on-html.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-on-html/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has epub:type="bodymatter" on its root html element. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. html is not the head and not metadata content, so epub:type may go on it.

## Question

`content.xhtml` has `epub:type="bodymatter"` on `html`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-xhtml-structural-semantics`](https://www.w3.org/TR/epub-33/#sec-xhtml-structural-semantics):

> EPUB creators MAY use the epub:type attribute in XHTML content documents to express structural semantics. The attribute MUST NOT be used on the head element or metadata content [html].

## Expected result

Valid. html is not the head and not metadata content, so epub:type may go on it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-type-on-html.epub -u --advisory` | no findings; VALID | `epub-type-on-html.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-on-html.epub -u` | no findings; VALID | `epub-type-on-html.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:type="bodymatter"` on its `html` element.

## History

- 2026-11-13: First version.
