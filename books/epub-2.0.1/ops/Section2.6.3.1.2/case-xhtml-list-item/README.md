# An `li` inside an `ops:case`, outside any list

- Book: `case-xhtml-list-item.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.2/case-xhtml-list-item/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#640](https://github.com/veripublica/epub-test-books/issues/640)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an ops:switch whose case holds an XHTML li with no list around it. The default holds a p. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Validity is decided with each switch replaced by the content of its default. The case is removed with the switch, so the li in it does not count.

## Question

In `content.xhtml`, an `ops:case` holds an XHTML `li` that has no list around it. The `ops:default` holds a `p`. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.2):

> The case element is used to contain non-Preferred Vocabulary or Extended Module markup.

OPS 2.0.1, [`Section2.6.3.1.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.3):

> The default element must contain only XML nodes that would be allowed at the point of the document where its parent switch element was used. More precisely, a document is considered valid if and only if replacing all switch elements with the content of their child default elements yields a valid document.

## Expected result

Valid. Validity is decided with each switch replaced by the content of its default. The case is removed with the switch, so the `li` in it does not count.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.50.0 | `epubveri -i case-xhtml-list-item.epub -u --advisory` | no findings; VALID | `case-xhtml-list-item.epubveri-0.50.0.txt` |
| epubcheck 5.4.0 | `epubcheck case-xhtml-list-item.epub -u` | no findings; VALID | `case-xhtml-list-item.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1999/xhtml"><li xmlns="http://www.w3.org/1999/xhtml">a</li></ops:case><ops:default><p>a</p></ops:default></ops:switch>
```

## History

- 2026-11-18: First version.
