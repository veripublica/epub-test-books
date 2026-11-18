# An `ops:switch` in a table row, with a `td` in its default

- Book: `default-table-cell.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.3/default-table-cell/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a table whose only row holds a td and an ops:switch. The switch's default holds a second td. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. With the switch replaced by the content of its default, the tr holds two td elements.

## Question

In `content.xhtml`, a `tr` holds a `td` and an `ops:switch` whose `ops:default` holds a second `td`. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.3):

> The default element must contain only XML nodes that would be allowed at the point of the document where its parent switch element was used. More precisely, a document is considered valid if and only if replacing all switch elements with the content of their child default elements yields a valid document.

## Expected result

Valid. With the switch replaced by the content of its default, the `tr` holds two `td` elements.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.45.0 | `epubveri -i default-table-cell.epub -u --advisory` | no findings; VALID | `default-table-cell.epubveri-0.45.0.txt` |
| epubcheck 5.4.0 | `epubcheck default-table-cell.epub -u` | no findings; VALID | `default-table-cell.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<table><tr><td>a</td><ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><td>b</td></ops:default></ops:switch></tr></table>
```

## History

- 2026-11-18: First version.
