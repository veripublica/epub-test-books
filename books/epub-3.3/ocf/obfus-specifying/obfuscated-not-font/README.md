# A stylesheet obfuscated as if it were a font

- Book: `obfuscated-not-font.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/obfus-specifying/obfuscated-not-font/build.py`
- Origin: built here
- Expected: invalid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#29](https://github.com/veripublica/epub-test-books/issues/29)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book's stylesheet, OEBPS/style.css, is obfuscated with the EPUB font obfuscation algorithm and listed in META-INF/encryption.xml. The font it points to is stored as it is. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Invalid. The algorithm is only for fonts, and a stylesheet is not a font core media type resource.

## Question

`META-INF/encryption.xml` lists a stylesheet as obfuscated with the font algorithm. Does a validator reject it?

## Clause

EPUB 3.3, [`obfus-specifying`](https://www.w3.org/TR/epub-33/#obfus-specifying):

> As the obfuscation algorithm is restricted to fonts, the URI attribute of the CipherReference element MUST reference a Font core media type resource.

## Expected result

Invalid. The algorithm is only for fonts, and a stylesheet is not a font core media type resource.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.42.0 | `epubveri -i obfuscated-not-font.epub -u --advisory` | ERROR PKG-026, INFO RSC-004, USAGE OPF-097, USAGE OBS-001; INVALID | `obfuscated-not-font.epubveri-0.42.0.txt` |
| epubcheck 5.4.0 | `epubcheck obfuscated-not-font.epub -u` | USAGE OBS-001, INFO RSC-004, USAGE OPF-097, ERROR PKG-026; INVALID | `obfuscated-not-font.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark. They report the same messages.

The other findings follow from the defect. INFO RSC-004 says the tools cannot read the obfuscated stylesheet. Because of that, they do not see its reference to the font, so USAGE OPF-097 says nothing references the font. USAGE OBS-001 says font obfuscation is outdated.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

The same book as `font-obfuscated`, but the stylesheet is obfuscated instead of the font. `META-INF/encryption.xml` has one `EncryptedData` entry, with `CipherReference URI="OEBPS/style.css"`.

## History

- 2026-11-08: First version.
