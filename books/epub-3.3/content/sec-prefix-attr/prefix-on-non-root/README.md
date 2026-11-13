# epub:prefix on an element other than the root

- Book: `prefix-on-non-root.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-on-non-root/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#567](https://github.com/veripublica/epub-test-books/issues/567)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares the prefix foo with epub:prefix on a div element, not on html, and uses epub:type="foo:bar" inside it. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The prefix attribute may only be on the root element.

## Question

`content.xhtml` has `epub:prefix` on a `div` instead of `html`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr):

> EPUB creators MUST only specify the prefix attribute on the root element [xml] of the respective format.

## Expected result

Invalid. The prefix attribute may only be on the root element.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i prefix-on-non-root.epub -u --advisory` | ERROR RSC-005, ERROR OPF-028; INVALID | `prefix-on-non-root.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-on-non-root.epub -u` | ERROR RSC-005, ERROR OPF-028; INVALID | `prefix-on-non-root.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<div epub:prefix="foo: https://example.org/epub-test-books/vocab#">` around `<p epub:type="foo:bar">Content.</p>`.

## History

- 2026-11-13: First version.
