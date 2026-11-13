# A `style` attribute (valid)

- Book: `style-attribute.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section1.3.5/style-attribute/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to start the OPS 2.0.1 content document sets
- Issue: [#303](https://github.com/veripublica/epub-test-books/issues/303)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

A p element in content.xhtml has a style attribute, which OPS 2.0.1 supports but calls deprecated. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The attribute is supported, though deprecated.

## Question

A `p` element in `content.xhtml` has a `style` attribute. OPS 2.0.1 supports it but calls it deprecated. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section1.3.5`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section1.3.5):

> This specification supports the style attribute (though deprecated), the style element, and externally linked style sheets.

## Expected result

Valid. The attribute is supported, though deprecated.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i style-attribute.epub -u --advisory` | no findings; VALID | `style-attribute.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck style-attribute.epub -u` | no findings; VALID | `style-attribute.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

In `content.xhtml`, the paragraph is `<p style="margin: 0">x</p>`.

## History

- 2026-11-11: First version.
