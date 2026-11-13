# A data block of an unregistered type, without the scripted property (valid)

- Book: `data-block-unknown-type.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-scripted-content/data-block-unknown-type/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#536](https://github.com/veripublica/epub-test-books/issues/536)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a script element with type="text/x-template", and its manifest item has no scripted property. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Any type other than a JavaScript type, module or importmap makes the script element a data block, so the document is not scripted.

## Question

`content.xhtml` has `<script type="text/x-template">` and no `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-scripted-content`](https://www.w3.org/TR/epub-33/#sec-scripted-content):

> When an [html] script element contains a data block [html], it does not represent scripted content.

HTML Living Standard, [`attr-script-type`](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) (4.12.1 The script element):

> Setting the attribute to any other value means that the script is a data block, which is not processed by the user agent, but instead by author script or other tools.

## Expected result

Valid. Any type other than a JavaScript type, module or importmap makes the script element a data block, so the document is not scripted.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i data-block-unknown-type.epub -u --advisory` | no findings; VALID | `data-block-unknown-type.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck data-block-unknown-type.epub -u` | no findings; VALID | `data-block-unknown-type.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<script type="text/x-template">&lt;p&gt;A template.&lt;/p&gt;</script>`. The manifest is not changed.

## History

- 2026-11-13: First version.
