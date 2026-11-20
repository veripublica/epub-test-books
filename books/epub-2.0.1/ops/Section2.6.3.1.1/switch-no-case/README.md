# An `ops:switch` with no `ops:case`

- Book: `switch-no-case.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.1/switch-no-case/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#635](https://github.com/veripublica/epub-test-books/issues/635)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has an ops:switch that holds only a default, with a p in it. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Invalid. The schema, which the specification names as the normative definition, requires one or more case elements before the default.

## Question

In `content.xhtml`, an `ops:switch` holds an `ops:default` and no `ops:case`. Does a validator reject it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.1`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.1):

> It contains zero or more case elements, and must contain one default element.

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

Invalid. The schema, which the specification names as the normative definition, requires one or more case elements before the default.

The prose of `Section2.6.3.1.1` and `Section2.6.3.1.2` says "zero or more case elements". `Section2.6.3.1` settles this in favour of the schema, and the later definition of the same element in the same namespace agrees: EPUB Content Documents 3.0.1, [`elemdef-switch`](http://www.idpf.org/epub/301/spec/epub-contentdocs-20140626.html#elemdef-switch), gives its content model as "In this order: case [1 or more], default [exactly 1]."

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.45.0 | `epubveri -i switch-no-case.epub -u --advisory` | ERROR RSC-005; INVALID | `switch-no-case.epubveri-0.45.0.txt` |
| epubcheck 5.4.0 | `epubcheck switch-no-case.epub -u` | ERROR RSC-005; INVALID | `switch-no-case.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:default><p>x</p></ops:default></ops:switch>
```

## History

- 2026-11-18: First version. Held the same day while the prose and the schema were compared, then added (Baris, 2026-11-18).
