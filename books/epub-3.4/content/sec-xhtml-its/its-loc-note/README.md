# ITS attributes its-loc-note and its-loc-note-type on a p (valid)

- Book: `its-loc-note.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.4/content/sec-xhtml-its/its-loc-note/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, from the EPUB 3.4 ITS support (w3c/epub-specs#2732)
- Issue: [#705](https://github.com/veripublica/epub-test-books/issues/705)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p in content.xhtml has its-loc-note="Keep the word Content in English." and its-loc-note-type="description", the HTML form of the ITS 2.0 localization note. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. EPUB 3.4 allows ITS attributes in XHTML content documents, in their HTML form, as ITS 2.0 defines them.

## Question

A `p` in `content.xhtml` has `its-loc-note` and `its-loc-note-type="description"`. Does a validator accept the book?

## Clause

EPUB 3.4, [`sec-xhtml-its`](https://www.w3.org/TR/epub-34/#sec-xhtml-its) (7.1.3.3 Internationalization tag set (ITS); Candidate Recommendation Draft, 25 November 2026):

> The [its20] specification defines a set of attributes that MAY be used in XHTML content documents to add support for internationalization, translation, and localization. ITS attributes MUST only be used as defined in Using ITS markup in HTML [its20] (i.e., EPUB 3 does not support the namespaced attributes). The use of these attributes MUST conform to the requirements defined in [its20].

## Expected result

Valid. `its-loc-note` and `its-loc-note-type` are the HTML form of the ITS 2.0 localization note, and `description` is one of the two values `its-loc-note-type` takes.

In EPUB 3.3 these attributes are neither HTML nor custom attributes, so the same book is invalid there. The namespaced form, `its:translate`, is invalid in both versions; the 3.3 set `content/sec-xhtml-custom-attributes/custom-attribute-its-namespace` shows it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i its-loc-note.epub -u --advisory` | no findings; VALID | `its-loc-note.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck its-loc-note.epub -u` | no findings; VALID | `its-loc-note.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

The EPUB 3 template, with `<p its-loc-note="Keep the word Content in English." its-loc-note-type="description">Content.</p>` in `content.xhtml`.

## History

- 2026-11-28: First version.
