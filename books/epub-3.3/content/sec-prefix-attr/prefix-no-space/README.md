# An epub:prefix mapping with no space after the colon

- Book: `prefix-no-space.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-no-space/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#568](https://github.com/veripublica/epub-test-books/issues/568)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares epub:prefix="foo:https://..." on its html element, with no space between the colon and the URL. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The grammar asks for at least one space after the colon, so this is not a mapping.

## Question

`content.xhtml` declares `epub:prefix="foo:https://…"`, with no space after the colon. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-prefix-attr`](https://www.w3.org/TR/epub-33/#sec-prefix-attr), the grammar of the prefix attribute:

> mapping = prefix , ":" , space , { space } , ? xsd:anyURI ? ;

## Expected result

Invalid. The grammar asks for at least one space after the colon, so this is not a mapping.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i prefix-no-space.epub -u --advisory` | ERROR OPF-004d, ERROR OPF-028; INVALID | `prefix-no-space.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-no-space.epub -u` | ERROR OPF-004d, ERROR OPF-028; INVALID | `prefix-no-space.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:prefix="foo:https://example.org/epub-test-books/vocab#"` on `html` and `<p epub:type="foo:bar">Content.</p>`.

## History

- 2026-11-13: First version.
