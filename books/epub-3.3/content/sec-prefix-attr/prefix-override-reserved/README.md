# A reserved prefix declared with another URL (valid)

- Book: `prefix-override-reserved.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-prefix-attr/prefix-override-reserved/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#570](https://github.com/veripublica/epub-test-books/issues/570)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml declares msv, a reserved prefix, with epub:prefix on its html element, mapped to a URL of its own. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Overriding a reserved prefix is a SHOULD NOT, not a MUST NOT. A warning would fit.

## Question

`content.xhtml` declares the reserved prefix `msv` with another URL. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-reserved-prefixes`](https://www.w3.org/TR/epub-33/#sec-reserved-prefixes):

> EPUB creators SHOULD NOT override reserved prefixes in the prefix attribute.

## Expected result

Valid. Overriding a reserved prefix is a SHOULD NOT, not a MUST NOT. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i prefix-override-reserved.epub -u --advisory` | WARNING OPF-007, WARNING OPF-086c; VALID | `prefix-override-reserved.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck prefix-override-reserved.epub -u` | WARNING OPF-007, WARNING OPF-086c; VALID | `prefix-override-reserved.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-007, WARNING OPF-086c do not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `epub:prefix="msv: https://example.org/epub-test-books/vocab#"` on `html` and `<p epub:type="msv:article">Content.</p>`.

## History

- 2026-11-13: First version.
