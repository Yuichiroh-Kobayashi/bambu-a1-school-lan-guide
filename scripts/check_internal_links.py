#!/usr/bin/env python3
"""Check that relative Markdown links point to existing local files."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def target_exists(source: Path, href: str) -> bool:
    href = href.strip()
    if not href or href.startswith(('#', 'http://', 'https://', 'mailto:', 'tel:')):
        return True
    path_part = unquote(href.split('#', 1)[0].split('?', 1)[0])
    if not path_part:
        return True
    target = (source.parent / path_part).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return False
    if target.exists():
        return True
    if target.suffix == "":
        return target.with_suffix(".md").exists() or (target / "index.md").exists()
    return False


def main() -> int:
    findings = []
    warnings = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                href = match.group(1)
                if not target_exists(path, href):
                    findings.append(f"{path.relative_to(ROOT).as_posix()}:{lineno}: missing link target: {href}")
                    continue
                href_text = href.strip()
                if path.relative_to(ROOT).parts[0] == "docs" and not href_text.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                    path_part = unquote(href_text.split("#", 1)[0].split("?", 1)[0])
                    if path_part:
                        target = (path.parent / path_part).resolve()
                        try:
                            rel_target = target.relative_to(ROOT)
                        except ValueError:
                            warnings.append(f"{path.relative_to(ROOT).as_posix()}:{lineno}: docs外への相対リンク: {href}")
                        else:
                            if rel_target.parts and rel_target.parts[0] != "docs":
                                warnings.append(f"{path.relative_to(ROOT).as_posix()}:{lineno}: docs外への相対リンク: {href}")
    if warnings:
        print("警告: docs配下のMarkdownからdocs外への相対リンクがあります:")
        print("\n".join(warnings))
    if findings:
        print("存在しない内部リンクを検出しました:")
        print("\n".join(findings))
        return 1
    print("内部リンクの問題は検出されませんでした。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
