# An `ops:case` with `required-modules="ruby"`

- Book: `case-required-modules.epub`, built from the EPUB 2 template
- Built by: `scripts/epub-2.0.1/ops/Section2.6.3.1.2.2/case-required-modules/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: epubveri, after a user report on MobileRead (thread 374286)
- Issue: [#638](https://github.com/veripublica/epub-test-books/issues/638)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

content.xhtml has a p with an ops:switch in it. The case holds a ruby element and names the ruby module. The default holds a span. Everything else is the EPUB 2 template, which raises no finding.

Expected result: Valid. Ruby is an XHTML Extended Module, so a case may hold it when required-modules names it. The default holds a span, which a p allows.

## Question

In `content.xhtml`, an `ops:case` with `required-namespace` set to XHTML and `required-modules="ruby"` holds a `ruby` element. Does a validator accept it?

## Clause

OPS 2.0.1, [`Section2.6.3.1.2.2`](https://idpf.org/epub/20/spec/OPS_2.0.1_draft.htm#Section2.6.3.1.2.2):

> The attribute value for required-modules must be a comma-separated list containing the name(s) of the Extended Modules used in the Inline XML Island.

> For XHTML, in the context of OPS, the Extended Modules include ruby, forms, server-side-image-map, and intrinsic-events.

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

Valid. Ruby is an XHTML Extended Module, so a case may hold it when `required-modules` names it. The default holds a `span`, which a `p` allows.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.51.0 | `epubveri -i case-required-modules.epub -u --advisory` | no findings; VALID | `case-required-modules.epubveri-0.51.0.txt` |
| epubcheck 5.4.0 | `epubcheck case-required-modules.epub -u` | no findings; VALID | `case-required-modules.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

Every epubveri finding here is in its default output. None is an `--advisory` finding.

## Build

`content.xhtml` holds, in the template's `div`:

```xml
<p>The word is <ops:switch xmlns:ops="http://www.idpf.org/2007/ops"><ops:case required-namespace="http://www.w3.org/1999/xhtml" required-modules="ruby"><ruby xmlns="http://www.w3.org/1999/xhtml"><rb>x</rb><rt>y</rt></ruby></ops:case><ops:default><span>x (y)</span></ops:default></ops:switch>.</p>
```

## History

- 2026-11-18: First version.
