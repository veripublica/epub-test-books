# An obfuscated font, done right

- Book: `font-obfuscated.epub`, built from the EPUB 3 template
- Built by: `scripts/epub-3.3/ocf/sec-font-obfuscation/font-obfuscated/build.py`
- Origin: built here
- Expected: valid
- Marks: none
- Asked for by: the maintainer, to complete the OCF section
- Issue: [#28](https://github.com/veripublica/epub-test-books/issues/28)

## About this book

This book is a set of epub-test-books, a library of small EPUB files that each show one rule or one defect.

The book has a stylesheet with an @font-face rule for a small TrueType font, OEBPS/fonts/box.ttf. The font is obfuscated with the EPUB font obfuscation algorithm: its bytes are XORed with the SHA-1 of the book's unique identifier. META-INF/encryption.xml lists it with the algorithm http://www.idpf.org/2008/embedding. Everything else is the EPUB 3 template, which raises no finding.

Expected result: Valid. This is the obfuscation the specification defines, done as it says: the key comes from the unique identifier, and encryption.xml has an entry for the font.

## Question

The book embeds a font obfuscated with the EPUB algorithm and lists it in `META-INF/encryption.xml`. Does a validator accept it?

## Clause

EPUB 3.3, [`sec-font-obfuscation`](https://www.w3.org/TR/epub-33/#sec-font-obfuscation):

> EPUB creators MUST derive the key used in the obfuscation algorithm from the unique identifier.
>
> Although not technically encrypted data, all obfuscated fonts MUST have an entry in the encryption.xml file accompanying the EPUB publication (see 4.2.6.3.2 Encryption file (encryption.xml)).
>
> Each EncryptedData element MUST contain a child EncryptionMethod element whose Algorithm attribute has the value http://www.idpf.org/2008/embedding.

The three sentences are from §4.4.3 and §4.4.5, under [`sec-font-obfuscation`](https://www.w3.org/TR/epub-33/#sec-font-obfuscation).

## Expected result

Valid. This is the obfuscation the specification defines, done as it says: the key comes from the unique identifier, and encryption.xml has an entry for the font.

## Verifier results

| Verifier | Command | Result | Output |
|----------|---------|--------|--------|
| epubveri 0.41.0 | `epubveri -i font-obfuscated.epub -u --advisory` | INFO RSC-004, USAGE CSS-028, USAGE OBS-001; VALID | `font-obfuscated.epubveri-0.41.0.txt` |
| epubcheck 5.4.0 | `epubcheck font-obfuscated.epub -u` | USAGE OBS-001, USAGE CSS-028, USAGE CSS-028, INFO RSC-004; VALID | `font-obfuscated.epubcheck-5.4.0.txt` |

Both agree with the expected result, so there is nothing to mark.

The other findings come with the font, not from a defect. INFO RSC-004 says the tools cannot read an encrypted resource, so they do not check it. USAGE OBS-001 says font obfuscation is outdated. USAGE CSS-028 notes the @font-face rule. epubcheck gives it once for each declaration in the rule, and epubveri once for the rule.

Every epubveri finding here is in its default output, except the USAGE messages, which need `-u`. None is an `--advisory` finding.

## Build

`OEBPS/style.css` (an @font-face rule) and `OEBPS/fonts/box.ttf` (`font/ttf`) are added to the manifest, and `OEBPS/content.xhtml` links the stylesheet. The font is written by `scripts/lib/minifont.py`. It is 928 bytes, so obfuscation changes the whole file, as §4.4.4 says it does for a font shorter than 1040 bytes. It is obfuscated, then deflated. `META-INF/encryption.xml` has one `EncryptedData` entry for it.

## History

- 2026-11-08: First version.
