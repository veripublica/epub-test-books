# A stylesheet with the deprecated `text/x-oeb1-css` type (valid)

- Book: `css-mime-oeb1.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.3.5/css-mime-oeb1/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#302](https://github.com/veripublica/epub-test-books/issues/302)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A linked stylesheet has the media type text/x-oeb1-css, in the manifest and on the link element. The type is deprecated. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The type is deprecated, not removed. A warning would fit.

## Question

A linked stylesheet has the media type `text/x-oeb1-css` in the manifest and on the `link`. The type is deprecated. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section1.3.5`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.3.5):

> The style sheet MIME type text/x-oeb1-css has been deprecated in favor of text/css.

## Expected result

Valid. The type is deprecated, not removed. A warning would fit.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.39.0 | `epubveri -i css-mime-oeb1.epub -u --advisory` | WARNING OPF-037; VALID | `css-mime-oeb1.epubveri-0.39.0.txt` |
| epubcheck 5.4.0 | `epubcheck css-mime-oeb1.epub -u` | WARNING OPF-037; VALID | `css-mime-oeb1.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

WARNING OPF-037 is the warning for the deprecated media type. It does not change the verdict.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`OEBPS/style.css` is listed as `text/x-oeb1-css`, and the `link` in `content.xhtml` has `type="text/x-oeb1-css"`.

## History

- 2026-11-11: First version.
