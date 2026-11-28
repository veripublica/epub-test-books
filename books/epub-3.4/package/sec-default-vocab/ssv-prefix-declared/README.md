# A prefix for the structural semantics vocabulary's own URL (invalid)

- Book: `ssv-prefix-declared.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/package/sec-default-vocab/ssv-prefix-declared/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, from the EPUB 3.4 prefix URL for structural semantics (w3c/epub-specs#2733)
- Issue: [#710](https://github.com/veripublica/epub-test-books/issues/710)
- Other clauses: EPUB 3.4 `type-attr-syntax`

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The html element of content.xhtml has epub:prefix="s: http://idpf.org/epub/vocab/structure/#", and a p in it has epub:type="s:chapter". Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. EPUB 3.4 gives http://idpf.org/epub/vocab/structure/# as the URL of the default vocabulary for epub:type, and a prefix must not be assigned to a default vocabulary's URL.

## Question

`content.xhtml` declares `epub:prefix="s: http://idpf.org/epub/vocab/structure/#"` and uses `s:chapter`. Does a validator reject the book?

## Clause

EPUB 3.4, [`sec-default-vocab`](https://www.w3.org/TR/epub-34/#sec-default-vocab) (5.3.3 Default vocabularies; Candidate Recommendation Draft, 25 November 2026):

> A default vocabulary is one whose terms and properties MUST NOT have a prefix when a compact URL is expected. A prefix MUST NOT be assigned to the URLs associated with these vocabularies using the prefix attribute.

EPUB 3.4, [`type-attr-syntax`](https://www.w3.org/TR/epub-34/#type-attr-syntax) (7.4.3.2 Syntax; Candidate Recommendation Draft, 25 November 2026):

> The default vocabulary for the epub:type attribute is the EPUB 3 Structural Semantics Vocabulary [epub-ssv-11]. The prefix URL for referencing its properties is http://idpf.org/epub/vocab/structure/#.

## Expected result

Invalid. `http://idpf.org/epub/vocab/structure/#` is the URL of the default vocabulary for `epub:type`, and `epub:prefix` assigns the prefix `s` to it.

EPUB 3.3 gives no URL for this vocabulary, so it does not say whether this prefix is assigned to a default vocabulary.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i ssv-prefix-declared.epub -u --advisory` | ERROR OPF-007b; INVALID | `ssv-prefix-declared.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck ssv-prefix-declared.epub -u` | no findings; VALID | `ssv-prefix-declared.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1789](https://github.com/w3c/epubcheck/issues/1789).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `epub:prefix="s: http://idpf.org/epub/vocab/structure/#"` on the `html` element of `content.xhtml` and `<p epub:type="s:chapter">Content.</p>` in it.

## History

- 2026-11-28: First version.
