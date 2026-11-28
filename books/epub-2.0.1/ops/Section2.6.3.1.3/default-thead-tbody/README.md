# An `ops:switch` whose default holds a `thead` and a `tbody`

- Book: `default-thead-tbody.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.3/default-thead-tbody/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#650](https://github.com/veripublica/epub-test-books/issues/650)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a table whose only child is an ops:switch. The switch's default holds a thead and then a tbody. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. With the switch replaced by the content of its default, the table holds a thead and then a tbody.

## Question

In `content.xhtml`, a `table` holds only an `ops:switch`, whose `ops:default` holds a `thead` and then a `tbody`. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.3):

> The default element must contain only XML nodes that would be allowed at the point of the document where its parent switch element was used. More precisely, a document is considered valid if and only if replacing all switch elements with the content of their child default elements yields a valid document.

## Expected result

Valid. With the switch replaced by the content of its default, the `table` holds a `thead` and then a `tbody`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i default-thead-tbody.epub -u --advisory` | no findings; VALID | `default-thead-tbody.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck default-thead-tbody.epub -u` | no findings; VALID | `default-thead-tbody.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<table><ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><thead><tr><th>h</th></tr></thead><tbody><tr><td>a</td></tr></tbody></ops:default></ops:switch></table>
```

## History

- 2026-11-18: First version.
