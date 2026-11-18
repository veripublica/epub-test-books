# An empty `ops:default`, the only child of a `ul`

- Book: `default-empty-list.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.3/default-empty-list/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a ul whose only child is an ops:switch. The switch's default is empty. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. With the switch replaced by the content of its default, the ul is empty, and XHTML 1.1 requires at least one li.

## Question

In `content.xhtml`, a `ul` holds only an `ops:switch`, whose `ops:default` is empty. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.3):

> The default element must contain only XML nodes that would be allowed at the point of the document where its parent switch element was used. More precisely, a document is considered valid if and only if replacing all switch elements with the content of their child default elements yields a valid document.

## Expected result

Invalid. With the switch replaced by the content of its default, the `ul` is empty, and XHTML 1.1 requires at least one `li`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.45.0 | `epubveri -i default-empty-list.epub -u --advisory` | ERROR RSC-005; INVALID | `default-empty-list.epubveri-0.45.0.txt` |
| epubcheck 5.4.0 | `epubcheck default-empty-list.epub -u` | ERROR RSC-005; INVALID | `default-empty-list.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<ul><ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default></ops:default></ops:switch></ul>
```

## History

- 2026-11-18: First version.
