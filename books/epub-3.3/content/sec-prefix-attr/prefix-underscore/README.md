# The prefix _ declared

- Book: `prefix-underscore.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-underscore/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares the prefix _ with epub:prefix on its html element and uses epub:type="_:bar". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The prefix _ is reserved and must not be declared.

## Question

`content.xhtml` declares the prefix `_`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr):

> EPUB creators MUST NOT declare the prefix '_' as this specification reserves this prefix for future compatibility with RDFa [rdfa-core] processing.

## Expected result

Invalid. The prefix _ is reserved and must not be declared.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i prefix-underscore.epub -u --advisory` | ERROR OPF-007a; INVALID | `prefix-underscore.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-underscore.epub -u` | ERROR OPF-007a, ERROR OPF-028; INVALID | `prefix-underscore.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report different messages but reach the same verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:prefix="_: https://example.org/epub-test-books/vocab#"` on `html` and `<p epub:type="_:bar">Content.</p>`.

## History

- 2026-11-13: First version.
