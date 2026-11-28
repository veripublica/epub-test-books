# A Flate-compressed `mimetype` file

- Book: `mimetype-compressed.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-zip-container-mime/mimetype-compressed/build.py`
- Origin: built here
- Expected: invalid
- Marks: epubcheck: missed
- Asked for by: the maintainer, to complete the OCF section; parked on 2026-11-08 while both verifiers missed it, shipped once epubveri reports it
- Issue: [#623](https://github.com/veripublica/epub-test-books/issues/623)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The mimetype entry is Flate-compressed (method 8). Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The mimetype file must not be compressed.

## Question

The `mimetype` entry is Flate-compressed (method 8). Does a validator reject the book?

## Clause

EPUB 3.3, [`sec-zip-container-mime`](https://www.w3.org/TR/epub-33/#sec-zip-container-mime):

> EPUB creators MUST NOT compress or encrypt the mimetype file.

## Expected result

Invalid. The `mimetype` file must not be compressed. EPUB 2.0.1 has the same case: `books/epub-2.0.1/ocf/Section4/mimetype-compressed`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i mimetype-compressed.epub -u --advisory` | ERROR PKG-007; INVALID | `mimetype-compressed.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck mimetype-compressed.epub -u` | no findings; VALID | `mimetype-compressed.epubcheck-5.4.0.txt` |

epubveri agrees with the expected result. epubcheck does not: it reports nothing.

- **epubcheck: missed.** [w3c/epubcheck#1779](https://github.com/w3c/epubcheck/issues/1779).

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The template's files, written as a container by `scripts/lib/ocfvariants.py` `mimetype_compressed()`. The `mimetype` entry uses compression method 8; its content is still `application/epub+zip`.

## History

- 2026-11-15: First version. The case was parked on 2026-11-08 while both verifiers missed it.
