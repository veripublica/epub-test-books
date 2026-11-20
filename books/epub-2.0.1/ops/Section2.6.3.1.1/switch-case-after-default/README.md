# An `ops:case` after the `ops:default`

- Book: `switch-case-after-default.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.1/switch-case-after-default/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#630](https://github.com/veripublica/epub-test-books/issues/630)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an ops:switch whose default comes first and whose case comes after it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The schema puts the case elements before the default, and here the case comes after it.

## Question

In `content.xhtml`, an `ops:switch` holds its `ops:default` first and its `ops:case` after it. Does a validator reject it?

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

## Expected result

Invalid. The schema puts the case elements before the default, and here the case comes after it.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.45.0 | `epubveri -i switch-case-after-default.epub -u --advisory` | ERROR RSC-005, ERROR RSC-005; INVALID | `switch-case-after-default.epubveri-0.45.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-case-after-default.epub -u` | ERROR RSC-005, ERROR RSC-005; INVALID | `switch-case-after-default.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:default><p>x</p></ops:default><ops:case required-namespace="http://www.w3.org/1998/Math/MathML"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>x</mi></math></ops:case></ops:switch>
```

## History

- 2026-11-18: First version.
