# A JSON data block, without the scripted property (valid)

- Book: `data-block.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-scripted-content/data-block/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#535](https://github.com/veripublica/epub-test-books/issues/535)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a script element with type="application/json", and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. A script element with a type that is not JavaScript and not module is a data block, and a data block does not represent scripted content. So no scripted property is needed.

## Question

`content.xhtml` has `<script type="application/json">` and no `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-scripted-content`](https://www.w3.org/TR/epub-33/#sec-scripted-content):

> When an [html] script element contains a data block [html], it does not represent scripted content.

HTML Living Standard, [`attr-script-type`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) (4.12.1 The script element):

> Setting the attribute to any other value means that the script is a data block, which is not processed by the user agent, but instead by author script or other tools.

## Expected result

Valid. A script element with a type that is not JavaScript and not module is a data block, and a data block does not represent scripted content. So no scripted property is needed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i data-block.epub -u --advisory` | no findings; VALID | `data-block.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck data-block.epub -u` | no findings; VALID | `data-block.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script type="application/json">{"a": 1}</script>`. The manifest is not changed.

## History

- 2026-11-13: First version.
