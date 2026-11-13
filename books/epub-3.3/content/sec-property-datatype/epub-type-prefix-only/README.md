# An epub:type of a prefix and a colon only

- Book: `epub-type-prefix-only.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-property-datatype/epub-type-prefix-only/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#563](https://github.com/veripublica/epub-test-books/issues/563)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares the prefix foo on its html element and has a p element with epub:type="foo:". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. A property with an empty reference, only a prefix and a colon, is not a valid property value.

## Question

`content.xhtml` has `epub:type="foo:"`, with `foo` declared. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-property-datatype`](https://www.w3.org/TR/epub-33/#sec-property-datatype):

> an empty reference does not represent a valid property value even though it is valid to the definition above (i.e., a property value that only consists of a prefix and colon is invalid).

## Expected result

Invalid. A property with an empty reference, only a prefix and a colon, is not a valid property value.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i epub-type-prefix-only.epub -u --advisory` | ERROR OPF-026; INVALID | `epub-type-prefix-only.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-prefix-only.epub -u` | ERROR OPF-026; INVALID | `epub-type-prefix-only.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:prefix="foo: https://example.org/epub-test-books/vocab#"` on `html` and `<p epub:type="foo:">Content.</p>`.

## History

- 2026-11-13: First version.
