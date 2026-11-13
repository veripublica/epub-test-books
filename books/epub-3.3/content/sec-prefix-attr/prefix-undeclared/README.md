# An epub:type prefix that is never declared

- Book: `prefix-undeclared.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-undeclared/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#565](https://github.com/veripublica/epub-test-books/issues/565)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml uses epub:type="foo:bar", and foo is declared nowhere. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. foo is not a reserved prefix, so it must be declared.

## Question

`content.xhtml` uses `epub:type="foo:bar"` and declares no prefix. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr):

> With the exception of reserved prefixes, EPUB creators MUST declare all prefixes used in a document.

## Expected result

Invalid. foo is not a reserved prefix, so it must be declared.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i prefix-undeclared.epub -u --advisory` | ERROR OPF-028; INVALID | `prefix-undeclared.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-undeclared.epub -u` | ERROR OPF-028; INVALID | `prefix-undeclared.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p epub:type="foo:bar">Content.</p>`. No `epub:prefix` is added.

## History

- 2026-11-13: First version.
