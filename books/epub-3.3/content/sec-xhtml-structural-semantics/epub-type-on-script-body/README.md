# epub:type on a script element in the body

- Book: `epub-type-on-script-body.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/content/sec-xhtml-structural-semantics/epub-type-on-script-body/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to cover EPUB 3.3 content document extensions
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has epub:type="chapter" on a script element in the body. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. script is metadata content, and epub:type must not be used on metadata content.

## Question

`content.xhtml` has `epub:type` on a `script` element in the body. Does a validator reject it?

## Clause

EPUB 3.3, [`sec-xhtml-structural-semantics`](https://www.w3.org/TR/epub-33/#sec-xhtml-structural-semantics):

> EPUB creators MAY use the epub:type attribute in XHTML content documents to express structural semantics. The attribute MUST NOT be used on the head element or metadata content [html].

HTML Living Standard, [`metadata-content`](https://html.spec.whatwg.org/multipage/dom.html#metadata-content) (3.2.5.2.1 Metadata content):

> Metadata content is content that sets up the presentation or behavior of the rest of the content, or that sets up the relationship of the document with other documents, or that conveys other "out of band" information.
>
> base, link, meta, noscript, script, style, template, title

## Expected result

Invalid. script is metadata content, and epub:type must not be used on metadata content.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i epub-type-on-script-body.epub -u --advisory` | ERROR RSC-005; INVALID | `epub-type-on-script-body.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck epub-type-on-script-body.epub -u` | ERROR RSC-005; INVALID | `epub-type-on-script-body.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` gets a `script` element in the body with `epub:type="chapter"`. The manifest item has `properties="scripted"`.

## History

- 2026-11-13: First version.
