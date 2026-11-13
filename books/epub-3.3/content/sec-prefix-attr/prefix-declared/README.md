# An epub:type prefix declared on the root element (valid)

- Book: `prefix-declared.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-declared/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#564](https://github.com/veripublica/epub-test-books/issues/564)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares the prefix foo with epub:prefix on its html element and uses epub:type="foo:bar". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The prefix is declared, on the root element, in the right form.

## Question

`content.xhtml` declares `foo` on `html` and uses `epub:type="foo:bar"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr):

> With the exception of reserved prefixes, EPUB creators MUST declare all prefixes used in a document.
>
> EPUB creators MUST only specify the prefix attribute on the root element [xml] of the respective format.

## Expected result

Valid. The prefix is declared, on the root element, in the right form.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i prefix-declared.epub -u --advisory` | no findings; VALID | `prefix-declared.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-declared.epub -u` | no findings; VALID | `prefix-declared.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:prefix="foo: https://example.org/epub-test-books/vocab#"` on `html` and `<p epub:type="foo:bar">Content.</p>`.

## History

- 2026-11-13: First version.
