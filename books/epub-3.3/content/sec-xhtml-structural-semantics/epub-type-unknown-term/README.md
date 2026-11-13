# An epub:type term that no vocabulary defines (valid)

- Book: `epub-type-unknown-term.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-unknown-term/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: [#559](https://github.com/veripublica/epub-test-books/issues/559)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p element with epub:type="no-such-term", an unprefixed term that the Structural Semantics Vocabulary does not define. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. Unprefixed terms outside the default vocabulary are allowed, though prefixed ones are preferred.

## Question

`content.xhtml` has `epub:type="no-such-term"`. Does a validator accept the book?

## Clause

EPUB 3.3, [`sec-epub-type-attribute`](https://www.w3.org/TR/epub-33/#sec-epub-type-attribute):

> EPUB creators MAY include unprefixed terms that are not part of this vocabulary, but the preferred method for adding custom semantics is to use prefixes for them.

## Expected result

Valid. Unprefixed terms outside the default vocabulary are allowed, though prefixed ones are preferred.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-type-unknown-term.epub -u --advisory` | USAGE OPF-088; VALID | `epub-type-unknown-term.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-unknown-term.epub -u` | USAGE OPF-088; VALID | `epub-type-unknown-term.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

USAGE OPF-088 does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets `<p epub:type="no-such-term">Content.</p>`.

## History

- 2026-11-13: First version.
