#!/usr/bin/env python3
"""Check documentation URLs conservatively; generate JSON, never delete links."""
import argparse
import concurrent.futures
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

URL_PATTERN = re.compile(r"https?://[^\s<>\"'\)\]]+", re.I)
MANUAL_DOMAINS = {"drive.google.com", "docs.google.com", "groups.google.com"}
SUFFIXES = {".md", ".txt"}

def extract(path):
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return []
    rows = []
    for n, line in enumerate(lines, 1):
        for match in URL_PATTERN.finditer(line):
            url = match.group(0).rstrip(".,;:!?}]")
            if url:
                rows.append({"source": str(path), "line": n, "url": url})
    return rows

def is_manual(url):
    parts = urlsplit(url)
    host = (parts.hostname or "").lower()
    if host in MANUAL_DOMAINS:
        return True
    if host in {"www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be"} and ("playlist" in parts.path or "list=" in parts.query):
        return True
    return False

def check(url, timeout=10, include_drive=False):
    if is_manual(url) and not include_drive:
        return {"status": "MANUAL_CHECK_REQUIRED", "http_code": None, "final_url": None, "error": "Requires signed-out content-level verification"}
    last_error = ""
    for method in ("HEAD", "GET"):
        try:
            headers = {"User-Agent": "Public-Stuff-Link-Checker/2026", "Accept": "*/*"}
            req = Request(url, method=method, headers=headers)
            with urlopen(req, timeout=timeout) as r:
                code = r.status
                dest = r.geturl()
                status = "REDIRECT" if dest != url else "OK"
                if code in (404, 410):
                    status = "BROKEN_404_410"
                if code in (401, 403, 429):
                    status = "AUTH_OR_RATE_LIMIT"
                if is_manual(url):
                    status = "MANUAL_CHECK_REQUIRED"
                return {"status": status, "http_code": code, "final_url": dest, "error": ""}
        except HTTPError as err:
            if method == "HEAD":
                continue
            code = err.code
            status = ("BROKEN_404_410" if code in (404, 410) else
                      "AUTH_OR_RATE_LIMIT" if code in (401, 403, 429) else "HTTP_ERROR")
            if is_manual(url) and code not in (404, 410):
                status = "MANUAL_CHECK_REQUIRED"
            return {"status": status, "http_code": code, "final_url": err.geturl(), "error": str(err)}
        except (URLError, OSError, ValueError) as err:
            last_error = str(err)
    return {"status": "NETWORK_ERROR", "http_code": None, "final_url": None, "error": last_error}

def paths_to_check(inputs):
    seen = set()
    for item in inputs:
        p = Path(item)
        children = [p] if p.is_file() else (p.rglob("*") if p.is_dir() else [])
        for child in children:
            if child.is_file() and child.suffix.lower() in SUFFIXES:
                if any(part in {".git", ".github", ".venv", "node_modules", "legacy"} for part in child.parts):
                    continue
                if str(child) not in seen:
                    seen.add(str(child))
                    yield child

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", default=["."])
    ap.add_argument("--output", default="link-report.json")
    ap.add_argument("--timeout", type=float, default=10.0)
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--include-drive", action="store_true")
    ap.add_argument("--fail-on-broken", action="store_true")
    args = ap.parse_args()
    rows = [row for file in paths_to_check(args.paths) for row in extract(file)]
    urls = sorted({row["url"] for row in rows})
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, min(16, args.workers))) as pool:
        jobs = {pool.submit(check, u, args.timeout, args.include_drive): u for u in urls}
        for job in concurrent.futures.as_completed(jobs):
            u = jobs[job]
            try:
                results[u] = job.result()
            except Exception as err:
                results[u] = {"status": "NETWORK_ERROR", "http_code": None, "final_url": None, "error": str(err)}
    now = datetime.now(timezone.utc).isoformat()
    counts = {}
    for result in results.values():
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    report = {
        "checked_at": now,
        "unique_urls": len(urls),
        "references": len(rows),
        "summary": counts,
        "results": [{**row, **results[row["url"]], "checked_at": now} for row in rows],
    }
    Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(urls)} URLs / {len(rows)} references; {counts}; report: {args.output}")
    return 1 if args.fail_on_broken and counts.get("BROKEN_404_410", 0) else 0

if __name__ == "__main__":
    sys.exit(main())
