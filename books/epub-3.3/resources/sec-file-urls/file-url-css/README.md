# A file URL in a stylesheet

- Book: `file-url-css.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/resources/sec-file-urls/file-url-css/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to start the publication resources section
- Issue: [#145](https://github.com/veripublica/epub-test-books/issues/145)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A stylesheet uses a file URL in url(). Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. File URLs are not allowed.

## Question

A stylesheet uses a file URL in `url()`. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-file-urls`](https://www.w3.org/TR/epub-33/#sec-file-urls):

> EPUB creators MUST NOT use file URLs in EPUB publications.

## Expected result

Invalid. File URLs are not allowed.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i file-url-css.epub -u --advisory` | ERROR RSC-006, ERROR OPF-014, ERROR RSC-030; INVALID | `file-url-css.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck file-url-css.epub -u` | ERROR RSC-030, ERROR OPF-014, ERROR RSC-006; INVALID | `file-url-css.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

The other errors come from the same URL: the tools also treat it as a remote resource.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` is added to the manifest with a `file:` URL in `url()`, and `content.xhtml` links to it.

## History

- 2026-11-09: First version.
