# Two prefixes in one epub:prefix (valid)

- Book: `prefix-two.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-two/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#566](https://github.com/veripublica/epub-test-books/issues/566)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares two prefixes, foo and baz, in one epub:prefix attribute on its html element, and uses a term from each. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. The attribute holds a whitespace-separated list of mappings, each a prefix, a colon, a space and a URL.

## Question

`content.xhtml` declares `foo` and `baz` in one `epub:prefix` and uses `epub:type="foo:bar baz:qux"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr):

> With the exception of reserved prefixes, EPUB creators MUST declare all prefixes used in a document.

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr), the grammar of the prefix attribute:

> mapping = prefix , ":" , space , { space } , ? xsd:anyURI ? ;

## Expected result

Valid. The attribute holds a whitespace-separated list of mappings, each a prefix, a colon, a space and a URL.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i prefix-two.epub -u --advisory` | no findings; VALID | `prefix-two.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-two.epub -u` | no findings; VALID | `prefix-two.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:prefix="foo: https://example.org/epub-test-books/vocab# baz: https://example.org/epub-test-books/other#"` on `html` and `<p epub:type="foo:bar baz:qux">Content.</p>`.

## History

- 2026-11-13: First version.
