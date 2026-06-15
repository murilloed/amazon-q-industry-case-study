#!/usr/bin/env python3
"""Conservative scanner for accidental secrets and restricted artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "generic secret assignment": re.compile(
        r"(?i)\b(password|passwd|secret|token|api[_-]?key)\b\s*[:=]\s*[\"']?[^\"'\s]{8,}"
    ),
    "Brazilian CPF-like value": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
    "Brazilian CNPJ-like value": re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"),
}

FORBIDDEN_SUFFIXES = {".zip", ".gz", ".7z", ".p12", ".pfx", ".jks", ".keystore"}
SKIP_DIRS = {".git", "__pycache__"}


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts) or not path.is_file():
            continue
        relative = path.relative_to(root)
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"{relative}: forbidden binary/archive suffix")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{relative}:{line_number}: {label}")
    return findings


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings = scan(root)
    if findings:
        print("Potential release blockers:")
        print("\n".join(findings))
        return 1
    print(f"Public-release scan passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
