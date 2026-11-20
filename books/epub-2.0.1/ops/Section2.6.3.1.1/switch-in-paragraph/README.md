# An `ops:switch` inside a `p`

- Book: `switch-in-paragraph.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.1/switch-in-paragraph/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#633](https://github.com/veripublica/epub-test-books/issues/633)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p that holds text, an ops:switch and more text. The switch's case holds MathML, and its default holds an em. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. With the switch replaced by the content of its default, the p holds text and an em, which XHTML 1.1 allows.

## Question

In `content.xhtml`, an `ops:switch` stands inside a `p`, between two runs of text. Its `ops:default` holds an `em`. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.3):

> The default element must contain only XML nodes that would be allowed at the point of the document where its parent switch element was used. More precisely, a document is considered valid if and only if replacing all switch elements with the content of their child default elements yields a valid document.

## Expected result

Valid. With the switch replaced by the content of its default, the `p` holds text and an `em`, which XHTML 1.1 allows.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i switch-in-paragraph.epub -u --advisory` | no findings; VALID | `switch-in-paragraph.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-in-paragraph.epub -u` | no findings; VALID | `switch-in-paragraph.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<p>The value is <ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><em>x</em></ops:default></ops:switch>.</p>
```

## History

- 2026-11-18: First version.
