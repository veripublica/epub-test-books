# The `scripted` property on a document whose only script is a data block (invalid)

- Book: `property-scripted-data-block.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-data-block/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3126
- Issue: [#702](https://github.com/veripublica/epub-test-books/issues/702)
- Other clauses: EPUB 3.3 `sec-scripted-support`, `sec-scripted` (appendix D.6.5)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml holds one script element, script type="application/json" with {"a": 1} inside: a data block, which HTML does not run. Its manifest item has the scripted property. The document has no other script, no event handler attribute and no form. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. EPUB 3.3 says a script element that contains a data block does not represent scripted content. So the document is not a scripted content document, and scripted says that it is.

## Question

`content.xhtml`'s only `script` is `<script type="application/json">{"a": 1}</script>`, and its manifest item has `properties="scripted"`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-scripted-support`](https://www.w3.org/TR/epub-33/#sec-scripted-support) (6.3.2.1 Script inclusion):

> When an [html] script element contains a data block [html], it does not represent scripted content.

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`sec-scripted`](https://www.w3.org/TR/epub-33/#sec-scripted) (D.6.5 scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or HTML form elements).

## Expected result

Invalid. A `script` element with `type="application/json"` holds a data block, and EPUB 3.3 says such an element does not represent scripted content. The document has no other scripting and no form, so it is not a scripted content document, and `scripted` says that it is.

A property may be set only where the resource matches its definition. The question went to [w3c/epub-specs#3126](https://github.com/w3c/epub-specs/issues/3126), where the [answer](https://github.com/w3c/epub-specs/issues/3126#issuecomment-7241168844) was: "if a property can be used when a resource doesn't match its definition then why have the properties at all?" The same comment points to the data-block sentence, which EPUB 3.4 keeps in 7.4.2.1.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i property-scripted-data-block.epub -u --advisory` | ERROR OPF-015; INVALID | `property-scripted-data-block.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-data-block.epub -u` | ERROR OPF-015; INVALID | `property-scripted-data-block.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

A `script` element with `type="application/json"` and `{"a": 1}` is added to `content.xhtml`, and `properties="scripted"` to its manifest item.

## History

- 2026-11-28: First version.
