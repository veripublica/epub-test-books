# An `ops:switch` nested in an `ops:default`

- Book: `switch-nested.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.1/switch-nested/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#634](https://github.com/veripublica/epub-test-books/issues/634)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an ops:switch whose default holds a second ops:switch. The inner default holds a p. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The schema lets a default hold switches. With both switches replaced by the content of their defaults, the div holds a p.

## Question

In `content.xhtml`, the `ops:default` of an `ops:switch` holds a second `ops:switch`, whose own `ops:default` holds a `p`. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1):

> The normative definition of the switch element and its contained elements can be found in the OPS Schema.

OPS 2.0.1, [Appendix B: The OPS Schema](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#AppendixB), the definition of `switch` (whitespace added):

```xml
<element name="switch">
  <optional><attribute name="id"><data type="ID"/></attribute></optional>
  <oneOrMore>
    <element name="case">
      <optional><attribute name="id"><data type="ID"/></attribute></optional>
      <attribute name="required-namespace"><text/></attribute>
      <optional><attribute name="required-modules"><text/></attribute></optional>
      <zeroOrMore><ref name="OPS.switch"/></zeroOrMore>
    </element>
  </oneOrMore>
  <element name="default">
      <optional><attribute name="id"><data type="ID"/></attribute></optional>
      <zeroOrMore><ref name="OPS.switch"/></zeroOrMore>
  </element>
</element>
```

OPS 2.0.1, [`Section2.6.3.1.3`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.3):

> The default element must contain only XML nodes that would be allowed at the point of the document where its parent switch element was used. More precisely, a document is considered valid if and only if replacing all switch elements with the content of their child default elements yields a valid document.

## Expected result

Valid. The schema lets a default hold switches. With both switches replaced by the content of their defaults, the `div` holds a `p`.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.47.0 | `epubveri -i switch-nested.epub -u --advisory` | no findings; VALID | `switch-nested.epubveri-0.47.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-nested.epub -u` | no findings; VALID | `switch-nested.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case><ops:default><p>x</p></ops:default></ops:switch></ops:default></ops:switch>
```

## History

- 2026-11-18: First version.
