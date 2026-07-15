#!/usr/bin/env python3
"""Detect likely non-public information in repository text files."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".jekyll-cache", "_site", "node_modules", ".venv", "venv"}
TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".txt", ".py", ""}

CHECKS = [
    ("IPv4アドレスらしい文字列", re.compile(r"(?<![\w.])(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|1?\d?\d)){3}(?![\w.])")),
    ("MACアドレスらしい文字列", re.compile(r"(?<![0-9A-Fa-f])(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}(?![0-9A-Fa-f])")),
    (".internal を含む文字列", re.compile(r"\.internal\b", re.IGNORECASE)),
    ("学校固有ドメインらしい文字列", re.compile(r"\b[a-z0-9.-]*(?:school|gakko|k12|edu|ed|ac)\.[a-z]{2,}\b", re.IGNORECASE)),
    ("Windowsユーザープロファイルの絶対パス", re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE)),
    ("アクセスコードやパスワードを直接記載した疑い", re.compile(r"(?i)\b(?:password|passphrase|access\s*code|token|secret)\s*[:=]\s*[^\s`'\"]{4,}")),
    ("メールアドレス", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)),
    ("日本語のパスワード・アクセスコード具体値", re.compile(r"(?:パスワード|アクセスコード)\s*[：:]\s*\S+")),
]

ALLOW = {
    ("scripts/check_public_content.py", "IPv4アドレスらしい文字列"),
    ("scripts/check_public_content.py", "MACアドレスらしい文字列"),
    ("scripts/check_public_content.py", ".internal を含む文字列"),
    ("scripts/check_public_content.py", "学校固有ドメインらしい文字列"),
    ("scripts/check_public_content.py", "Windowsユーザープロファイルの絶対パス"),
    ("scripts/check_public_content.py", "アクセスコードやパスワードを直接記載した疑い"),
    ("scripts/check_public_content.py", "メールアドレス"),
    ("scripts/check_public_content.py", "日本語のパスワード・アクセスコード具体値"),
}


def iter_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            files.append(path)
    return files


def main() -> int:
    findings = []
    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(lines, 1):
            for label, pattern in CHECKS:
                if (rel, label) in ALLOW:
                    continue
                if pattern.search(line):
                    findings.append(f"{rel}:{lineno}: {label}: {line.strip()}")
    if findings:
        print("公開禁止情報の疑いを検出しました:")
        print("\n".join(findings))
        return 1
    print("公開禁止情報の疑いは検出されませんでした。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
