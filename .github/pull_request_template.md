Closes #

- [ ] Built from a template in `books/templates/` by a script under `scripts/` at the set's path.
- [ ] Book and README under `books/`; nothing executable there.
- [ ] README has About this book, Question, Clause (quoted), Expected result, Verifier results, Build and History.
- [ ] Origin is `built here`, or `reduced from a real book` and every item of CONTRIBUTING §3 is done.
- [ ] No title, publisher or file of a source book appears anywhere.
- [ ] Two builds give the same bytes.
- [ ] `scripts/check.py` outputs added (`epubveri -u --advisory`, `epubcheck -u`), named with exact versions.
- [ ] Every difference from the expected result is marked (intended / spec unclear, followed epubcheck / missed / wrong error).
- [ ] Default vs `--advisory` recorded for each epubveri finding.
- [ ] Reviewed by whoever asked for the set.

I confirm this contribution is licensed under CC BY 4.0 (`books/`, READMEs, docs) and AGPL-3.0-only (`scripts/`, with their output under CC BY 4.0), and that I have the right to give it.
