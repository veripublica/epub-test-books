# An empty `ops:case`

- Book: `case-empty.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.2/case-empty/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: pending

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an ops:switch whose case is empty. The default holds a p. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. The schema allows an empty case, and a Reading System must not invalidate a document for one.

## Question

In `content.xhtml`, the `ops:case` of an `ops:switch` is empty. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.2):

> An OPS Reading System must not invalidate a document and must display nothing if a case element contains no content.

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

## Expected result

Valid. The schema allows an empty case, and a Reading System must not invalidate a document for one.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.45.0 | `epubveri -i case-empty.epub -u --advisory` | no findings; VALID | `case-empty.epubveri-0.45.0.txt` |
| epubcheck 5.4.0 | `epubcheck case-empty.epub -u` | no findings; VALID | `case-empty.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"/><ops:default><p>x</p></ops:default></ops:switch>
```

## History

- 2026-11-18: First version.
