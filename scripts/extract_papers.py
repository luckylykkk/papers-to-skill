#!/usr/bin/env python3
"""Extract text from one or more research paper PDFs.

The script prefers installed command-line or Python extractors and keeps going
when individual PDFs fail. It writes a manifest plus one text file per paper.
"""

from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def install_packages(packages: list[str]) -> bool:
    if not packages:
        return True
    result = subprocess.run([sys.executable, "-m", "pip", "install", *packages])
    importlib.invalidate_caches()
    return result.returncode == 0


def slugify(value: str, fallback: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-{2,}", "-", value)
    return value[:80] or fallback


def resolve_inputs(patterns: list[str]) -> list[Path]:
    pdfs: list[Path] = []
    for pattern in patterns:
        path = Path(pattern)
        if path.is_dir():
            pdfs.extend(path.rglob("*.pdf"))
            pdfs.extend(path.rglob("*.PDF"))
        elif any(ch in pattern for ch in "*?[]"):
            pdfs.extend(Path(p) for p in glob.glob(pattern, recursive=True))
        elif path.is_file():
            pdfs.append(path)

    seen: set[Path] = set()
    unique: list[Path] = []
    for pdf in pdfs:
        resolved = pdf.resolve()
        if resolved.suffix.lower() == ".pdf" and resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return sorted(unique)


def extract_with_pdftotext(pdf: Path) -> str | None:
    exe = shutil.which("pdftotext")
    if not exe:
        return None
    result = subprocess.run(
        [exe, "-layout", "-enc", "UTF-8", str(pdf), "-"],
        text=True,
        capture_output=True,
        timeout=180,
        errors="replace",
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout
    return None


def extract_with_pypdf2(pdf: Path) -> str | None:
    if not module_available("PyPDF2"):
        return None
    from PyPDF2 import PdfReader  # type: ignore

    reader = PdfReader(str(pdf))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            pages.append(f"\n\n--- Page {i} ---\n{page.extract_text() or ''}")
        except Exception as exc:
            pages.append(f"\n\n--- Page {i} extraction failed: {exc} ---\n")
    text = "\n".join(pages)
    return text if text.strip() else None


def extract_with_pdfminer(pdf: Path) -> str | None:
    if not module_available("pdfminer.high_level"):
        return None
    from pdfminer.high_level import extract_text  # type: ignore

    text = extract_text(str(pdf))
    return text if text.strip() else None


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        cleaned = re.sub(r"\s+", " ", line).strip()
        if 8 <= len(cleaned) <= 220:
            return cleaned
    return ""


def find_year(text: str, filename: str) -> str:
    match = re.search(r"\b(19|20)\d{2}\b", filename)
    if match:
        return match.group(0)
    match = re.search(r"\b(19|20)\d{2}\b", text[:5000])
    return match.group(0) if match else ""


def find_doi(text: str) -> str:
    match = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", text[:12000], re.I)
    return match.group(0).rstrip(".") if match else ""


def estimate_tokens(text: str) -> int:
    return int(len(text.split()) / 0.75)


def extract_one(pdf: Path, install_missing: str) -> tuple[str, str]:
    text = extract_with_pdftotext(pdf)
    if text:
        return text, "pdftotext"

    missing: list[str] = []
    if not module_available("PyPDF2"):
        missing.append("PyPDF2")
    if not module_available("pdfminer.high_level"):
        missing.append("pdfminer.six")
    if missing and install_missing == "yes":
        install_packages(missing)

    text = extract_with_pypdf2(pdf)
    if text:
        return text, "PyPDF2"

    text = extract_with_pdfminer(pdf)
    if text:
        return text, "pdfminer.six"

    raise RuntimeError("no extractor produced text; install poppler pdftotext, PyPDF2, or pdfminer.six")


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from multiple paper PDFs.")
    parser.add_argument("inputs", nargs="+", help="PDF files, folders, or glob patterns")
    parser.add_argument("--out", default="paper_skill_work", help="Output work directory")
    parser.add_argument(
        "--install-missing",
        choices=["yes", "no"],
        default=os.environ.get("PAPERS_TO_SKILL_INSTALL_MISSING", "no"),
        help="Install missing Python PDF packages with pip",
    )
    args = parser.parse_args()

    out_dir = Path(args.out).resolve()
    text_dir = out_dir / "texts"
    text_dir.mkdir(parents=True, exist_ok=True)

    pdfs = resolve_inputs(args.inputs)
    manifest: dict[str, object] = {
        "inputs": args.inputs,
        "output_dir": str(out_dir),
        "paper_count": len(pdfs),
        "papers": [],
    }

    papers: list[dict[str, object]] = []
    for index, pdf in enumerate(pdfs, start=1):
        record: dict[str, object] = {
            "source_file": str(pdf),
            "status": "pending",
        }
        try:
            text, extractor = extract_one(pdf, args.install_missing)
            title = first_nonempty_line(text) or pdf.stem
            year = find_year(text, pdf.name)
            doi = find_doi(text)
            paper_id = slugify(f"{year}-{title}" if year else title, f"paper-{index:03d}")
            output_text = text_dir / f"{paper_id}.txt"
            output_text.write_text(text, encoding="utf-8")

            record.update(
                {
                    "status": "ok",
                    "id": paper_id,
                    "title_guess": title,
                    "year_guess": year,
                    "doi_guess": doi,
                    "extractor": extractor,
                    "text_file": str(output_text),
                    "word_count": len(text.split()),
                    "estimated_tokens": estimate_tokens(text),
                }
            )
        except Exception as exc:
            record.update({"status": "failed", "error": str(exc)})
        papers.append(record)

    manifest["papers"] = papers
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    ok = sum(1 for paper in papers if paper.get("status") == "ok")
    failed = len(papers) - ok
    print(f"PDFs found: {len(pdfs)}")
    print(f"Extracted: {ok}")
    print(f"Failed: {failed}")
    print(f"Manifest: {manifest_path}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
