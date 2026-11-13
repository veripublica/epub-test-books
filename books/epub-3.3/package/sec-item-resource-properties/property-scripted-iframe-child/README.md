# A scripted document in an iframe: scripted on that document only (valid)

- Book: `property-scripted-iframe-child.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-iframe-child/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 scripting
- Issue: [#544](https://github.com/veripublica/epub-test-books/issues/544)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an iframe of OEBPS/framed.xhtml, which has a script element. framed.xhtml has the scripted property, and content.xhtml does not. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The properties do not apply to content included with an iframe, so only the framed document needs scripted.

## Question

`content.xhtml` frames `framed.xhtml`, which has a script. Only `framed.xhtml` has the `scripted` property. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> These properties do not apply recursively to content included into a resource (e.g., via the [html] iframe element). For example, if a non-scripted XHTML content document embeds a scripted content document, only the embedded document's manifest item properties attribute will have the scripted value.

## Expected result

Valid. The properties do not apply to content included with an iframe, so only the framed document needs scripted.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i property-scripted-iframe-child.epub -u --advisory` | no findings; VALID | `property-scripted-iframe-child.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-iframe-child.epub -u` | no findings; VALID | `property-scripted-iframe-child.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p><iframe src="framed.xhtml" title="A framed document"></iframe></p>`. `OEBPS/framed.xhtml` has `<script>let a = 1;</script>` and is in the manifest with `properties="scripted"`, not in the spine.

## History

- 2026-11-13: First version.
