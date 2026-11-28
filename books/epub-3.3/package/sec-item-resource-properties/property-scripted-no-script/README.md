# The `scripted` property on a document with no scripting (invalid)

- Book: `property-scripted-no-script.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/package/sec-item-resource-properties/property-scripted-no-script/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, after w3c/epub-specs#3126
- Issue: [#703](https://github.com/veripublica/epub-test-books/issues/703)
- Other clauses: EPUB 3.3 `sec-scripted` (appendix D.6.5)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The manifest item of content.xhtml has the scripted property, but content.xhtml has no script element, no event handler attribute and no form. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. scripted says that the document is a scripted content document, and this one is not. A property may be set only where the resource matches its definition (w3c/epub-specs#3126).

## Question

The manifest item of `content.xhtml` has `properties="scripted"`, but the document has no scripting and no form. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-item-resource-properties`](https://www.w3.org/TR/epub-33/#sec-item-resource-properties):

> EPUB creators MUST set the following properties whenever a resource referenced by an item element matches their respective definitions:

EPUB 3.3, [`sec-scripted`](https://www.w3.org/TR/epub-33/#sec-scripted) (D.6.5 scripted):

> The scripted property indicates that the described publication resource is a scripted content document (i.e., contains scripting and/or HTML form elements).

## Expected result

Invalid. `content.xhtml` has no scripting and no form, so it is not a scripted content document, and `scripted` says that it is.

The requirement is worded in one direction only: it asks for `scripted` where the document has scripting, and does not say that the property must not be set elsewhere. The question went to [w3c/epub-specs#3126](https://github.com/w3c/epub-specs/issues/3126). The [first answer](https://github.com/w3c/epub-specs/issues/3126#issuecomment-7240601454) there: per the definition of a scripted content document, "an html resource without a `script` element is not one of those". The [second](https://github.com/w3c/epub-specs/issues/3126#issuecomment-7241168844): "if a property can be used when a resource doesn't match its definition then why have the properties at all?" It proposes "only when" for "whenever" in EPUB 3.4.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i property-scripted-no-script.epub -u --advisory` | ERROR OPF-015; INVALID | `property-scripted-no-script.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck property-scripted-no-script.epub -u` | ERROR OPF-015; INVALID | `property-scripted-no-script.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`properties="scripted"` is added to the manifest item of `content.xhtml`. The document is not changed.

## History

- 2026-11-28: First version.
