# SPDX-License-Identifier: AGPL-3.0-only
# Copyright (c) 2026 Barış Kayadelen (veripublica) and contributors
"""The release step: index, checks and the download bundle.

    python3 scripts/release.py index  vX.Y.Z          write books/INDEX.md and books/index.json
    python3 scripts/release.py check  vX.Y.Z [--full] fail if anything is stale for that release
    python3 scripts/release.py bundle vX.Y.Z OUTDIR   write the release assets into OUTDIR
    python3 scripts/release.py lint                   the checks that need no release name (CI, every PR)

The index names the release it was made for. `check` fails when the
committed index was made for another release or differs from what `index`
would write now, so a release can never ship with a stale index (CONTRIBUTING
§7). `check` without `--full` needs only Python, and CI runs it; `--full`
also rebuilds every book and reruns both verifiers, which needs epubveri
and epubcheck installed.

Release assets: one .epub per book, named `<spec>--<anchor>--<set>.epub`
(templates: `templates--<name>.epub`) so that no two collide, and
`epub-test-books-vX.Y.Z.zip` with all of them in one flat folder, the index
and the licence files. The bundle is reproducible like the books.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "books"
REPO = "https://github.com/veripublica/epub-test-books"
CREDIT = ("EPUB test books © veripublica contributors, CC BY 4.0, " + REPO)
ZIP_TIME = (1980, 1, 1, 0, 0, 0)
LEVELS = ("FATAL", "ERROR", "WARNING", "INFO", "USAGE")


# --- reading the library ---------------------------------------------------

def vkey(v: str) -> tuple:
    return tuple(int(x) if x.isdigit() else x for x in re.split(r"[.+-]", v))


def field(text: str, name: str) -> str | None:
    m = re.search(rf"^- {re.escape(name)}: (.+)$", text, re.M)
    return m.group(1).strip() if m else None


def section_first_paragraph(text: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*$\n+(.*?)(?:\n\s*\n|\Z)", text,
                  re.M | re.S)
    return " ".join(m.group(1).split()) if m else ""


def verifier(folder: Path, stem: str, tool: str) -> dict | None:
    files = sorted(folder.glob(f"{stem}.{tool}-*.txt"),
                   key=lambda p: vkey(p.name[len(stem) + len(tool) + 2:-4]))
    if not files:
        return None
    f = files[-1]
    text = f.read_text(encoding="utf-8")
    if tool == "epubveri":
        codes = re.findall(rf"^({'|'.join(LEVELS)}) ([A-Z]+-\d+)", text, re.M)
    else:
        codes = re.findall(rf"^({'|'.join(LEVELS)})\(([A-Z]+-\d+)\)", text, re.M)
    valid = not any(level in ("FATAL", "ERROR") for level, _ in codes)
    return {
        "version": f.name[len(stem) + len(tool) + 2:-4],
        "verdict": "valid" if valid else "invalid",
        "messages": [f"{level} {code}" for level, code in codes],
        "output": f.relative_to(ROOT).as_posix(),
    }


def asset_name(book: Path) -> str:
    parts = book.parent.relative_to(BOOKS).parts
    if parts[0] == "templates":
        base = ["templates", parts[-1]]
    else:
        base = [parts[0], parts[-2], parts[-1]]      # spec, anchor, set
    if book.stem != parts[-1]:
        base.append(book.stem)
    return "--".join(base) + ".epub"


def library() -> list[dict]:
    entries = []
    readmes = sorted(BOOKS.rglob("README.md"),
                     key=lambda r: (r.parent.parts[len(BOOKS.parts)] != "templates", r))
    for readme in readmes:
        folder = readme.parent
        if folder == BOOKS:
            continue
        text = readme.read_text(encoding="utf-8")
        for book in sorted(folder.glob("*.epub")):
            title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
            issue = field(text, "Issue")
            m = re.search(r"\((https://[^)]+)\)", issue or "")
            entries.append({
                "path": folder.relative_to(ROOT).as_posix(),
                "book": book.relative_to(ROOT).as_posix(),
                "asset": asset_name(book),
                "sha256": hashlib.sha256(book.read_bytes()).hexdigest(),
                "title": title,
                "question": section_first_paragraph(text, "Question")
                            or section_first_paragraph(text, "Expected result"),
                "expected": field(text, "Expected"),
                "marks": field(text, "Marks"),
                "asked_by": field(text, "Asked for by"),
                "issue": m.group(1) if m else None,
                "epubveri": verifier(folder, book.stem, "epubveri"),
                "epubcheck": verifier(folder, book.stem, "epubcheck"),
            })
    return entries


# --- index -------------------------------------------------------------------

def render(version: str, entries: list[dict]) -> tuple[str, str]:
    data = {"release": version, "repository": REPO, "credit": CREDIT,
            "books": entries}
    js = json.dumps(data, indent=2, ensure_ascii=False) + "\n"

    def tool(t: dict | None) -> str:
        if not t:
            return "not run"
        msgs = ", ".join(t["messages"]) or "no finding"
        return f"{t['verdict']} ({msgs})"

    dl = f"{REPO}/releases/download/{version}"
    rows = []
    for e in entries:
        link = f"[{e['title']}]({REPO}/blob/{version}/{e['path']}/README.md)"
        issue = f"[#{e['issue'].rsplit('/', 1)[-1]}]({e['issue']})" if e["issue"] else ""
        rows.append(
            f"| {link} | {e['expected']} | {tool(e['epubveri'])} | "
            f"{tool(e['epubcheck'])} | {e['marks']} | {issue} | "
            f"[.epub]({dl}/{e['asset']}) |")
    md = f"""# Index of books

Release {version}. This page is generated by `scripts/release.py`; do not
edit it by hand. The same list, for programs, is in `index.json`.

Every book shows one thing. The expected result comes from the
specification; the verifier columns are what each tool says, with the
version in its README. A mark says where a tool differs from the expected
result.

All books in one download: [epub-test-books-{version}.zip]({dl}/epub-test-books-{version}.zip)

| Book | Expected | epubveri | epubcheck | Marks | Issue | Download |
|------|----------|----------|-----------|-------|-------|----------|
""" + "\n".join(rows) + f"""

{CREDIT}
"""
    return md, js


def problems(entries: list[dict]) -> list[str]:
    out = []
    names = [e["asset"] for e in entries]
    for n in sorted({n for n in names if names.count(n) > 1}):
        out.append(f"asset name used twice: {n}")
    for e in entries:
        for key in ("expected", "marks"):
            if not e[key]:
                out.append(f"{e['path']}: README has no '- {key.capitalize()}:' line")
        for t in ("epubveri", "epubcheck"):
            if not e[t]:
                out.append(f"{e['book']}: no {t} output")
        if e["path"].split("/")[1] != "templates" and not e["issue"]:
            out.append(f"{e['path']}: README has no issue link")
    return out


def cmd_index(version: str) -> None:
    entries = library()
    bad = problems(entries)
    if bad:
        raise SystemExit("\n".join(bad))
    md, js = render(version, entries)
    (BOOKS / "INDEX.md").write_text(md, encoding="utf-8")
    (BOOKS / "index.json").write_text(js, encoding="utf-8")
    print(f"books/INDEX.md, books/index.json: {len(entries)} books, {version}")


# --- check -------------------------------------------------------------------

def cmd_check(version: str, full: bool) -> None:
    bad: list[str] = []
    if not re.fullmatch(r"v\d+\.\d+\.\d+", version):
        bad.append(f"{version}: not a vMAJOR.MINOR.PATCH tag")
    entries = library()
    bad += problems(entries)
    md, js = render(version, entries)
    for name, want in (("INDEX.md", md), ("index.json", js)):
        f = BOOKS / name
        if not f.exists():
            bad.append(f"books/{name} is missing: run `release.py index {version}`")
            continue
        have = f.read_text(encoding="utf-8")
        if have != want:
            made_for = re.search(r'"release": "([^"]+)"|^Release (\S+)\.', have, re.M)
            for_ = next((g for g in (made_for.groups() if made_for else ()) if g), "?")
            bad.append(f"books/{name} is stale (made for {for_}, release is "
                       f"{version}, or a book changed): run `release.py index {version}`")
    if full:
        before = {e["book"]: e["sha256"] for e in entries}
        for script in sorted((ROOT / "scripts").rglob("build.py")):
            subprocess.run([sys.executable, str(script)], check=True,
                           stdout=subprocess.DEVNULL)
        for e in library():
            if before.get(e["book"]) != e["sha256"]:
                bad.append(f"{e['book']}: a rebuild changed its bytes")
        for folder in sorted({Path(e["path"]) for e in entries}):
            r = subprocess.run([sys.executable, str(ROOT / "scripts/check.py"),
                                str(ROOT / folder)], capture_output=True, text=True)
            if r.returncode or "written" in r.stdout:
                bad.append(f"{folder}: verifier outputs are not current "
                           f"({(r.stdout + r.stderr).strip().splitlines()[-1]})")
    if bad:
        raise SystemExit("release check failed:\n- " + "\n- ".join(bad))
    print(f"release check passed for {version}: {len(entries)} books"
          + (" (full)" if full else ""))


# --- bundle ------------------------------------------------------------------

def zinfo(name: str) -> zipfile.ZipInfo:
    zi = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    zi.create_system, zi.external_attr = 3, 0o100644 << 16
    zi.compress_type = zipfile.ZIP_DEFLATED
    return zi


def cmd_bundle(version: str, outdir: str) -> None:
    cmd_check(version, full=False)
    out = Path(outdir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    entries = library()
    top = f"epub-test-books-{version}"
    zpath = out / f"{top}.zip"
    with zipfile.ZipFile(zpath, "w") as z:
        for name in ("INDEX.md", "index.json"):
            z.writestr(zinfo(f"{top}/{name}"), (BOOKS / name).read_bytes(),
                       compresslevel=9)
        for name in ("LICENSE", "NOTICE"):
            z.writestr(zinfo(f"{top}/{name}"), (ROOT / name).read_bytes(),
                       compresslevel=9)
        z.writestr(zinfo(f"{top}/CREDIT.txt"), (CREDIT + "\n").encode(),
                   compresslevel=9)
        for e in entries:
            data = (ROOT / e["book"]).read_bytes()
            z.writestr(zinfo(f"{top}/{e['asset']}"), data, compresslevel=9)
            (out / e["asset"]).write_bytes(data)
    print(f"{zpath.name} and {len(entries)} .epub files in {out}")


def cmd_lint() -> None:
    entries = library()
    bad = problems(entries)
    if bad:
        raise SystemExit("lint failed:\n- " + "\n- ".join(bad))
    print(f"lint passed: {len(entries)} books")


def main() -> None:
    a = sys.argv[1:]
    if a == ["lint"]:
        cmd_lint()
    elif len(a) >= 2 and a[0] == "index":
        cmd_index(a[1])
    elif len(a) >= 2 and a[0] == "check":
        cmd_check(a[1], full="--full" in a)
    elif len(a) == 3 and a[0] == "bundle":
        cmd_bundle(a[1], a[2])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
