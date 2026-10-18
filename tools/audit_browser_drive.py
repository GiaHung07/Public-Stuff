#!/usr/bin/env python3
"""Second-pass Chromium verification of inconclusive historical Drive links."""
import argparse
import asyncio
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path

DEAD = ("this file does not exist", "the file you have requested does not exist",
        "this item has been deleted", "can't find the file", "file doesn't exist")
DENIED = ("you need access", "request access", "you don't have access",
          "you need permission", "you do not have access", "sign in to continue")

async def verify_one(context, item, sem):
    async with sem:
        page = await context.new_page()
        url = item["url"]
        result = {"url": url, "original_status": item["status"],
                  "browser_status": "INCONCLUSIVE", "title": "", "final_url": url,
                  "visible_rows": 0, "evidence": ""}
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=18000)
            await page.wait_for_timeout(2200)
            result["final_url"] = page.url
            result["title"] = (await page.title())[:140]
            txt = (await page.locator("body").inner_text(timeout=6000)).lower()[:14000]
            result["visible_rows"] = await page.locator('[role="row"]').count()
            if any(x in txt for x in DEAD):
                result.update(browser_status="UNAVAILABLE_MESSAGE",
                              evidence="Browser rendered a file not found/deleted message")
            elif any(x in txt for x in DENIED) or "accounts.google.com" in page.url:
                result.update(browser_status="ACCESS_RESTRICTED",
                              evidence="Browser rendered request-access/sign-in message")
            elif result["visible_rows"] >= 2 and ("drive.google.com" in page.url):
                result.update(browser_status="CONTENT_VISIBLE",
                              evidence="Browser rendered file/folder rows; inspect content manually")
            elif "docs.google.com" in page.url and len(txt) > 400 and ("document" in result["title"].lower() or "google" not in result["title"].lower()):
                result.update(browser_status="CONTENT_POSSIBLE",
                              evidence="Document UI visible but readable content not conclusively verified")
            else:
                result.update(browser_status="INCONCLUSIVE",
                              evidence="No conclusive file listing or error; browser page title: " + result["title"])
        except Exception as exc:
            result.update(browser_status="BROWSER_ERROR",
                          evidence=type(exc).__name__ + ": " + str(exc)[:130])
        finally:
            await page.close()
        print("BROWSER", result["browser_status"], "rows", result["visible_rows"], url[:100], flush=True)
        return result

async def main_async(args):
    from playwright.async_api import async_playwright
    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
    candidates = list({r["url"]: r for r in raw["items"]
                       if r["status"] in ("NEEDS_BROWSER","PUBLIC_UNAVAILABLE")}.values())
    sem = asyncio.Semaphore(min(4, max(1, args.workers)))
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(locale="en-US", viewport={"width": 1280, "height": 850})
        results = await asyncio.gather(*(verify_one(context, x, sem) for x in candidates))
        await browser.close()
    stat = dict(Counter(r["browser_status"] for r in results))
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "source_report": args.input,
              "checked": len(results), "status_counts": stat, "results": results}
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("BROWSER SUMMARY:", len(results), "links", json.dumps(stat, ensure_ascii=False), flush=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="legacy-drive-audit.json")
    ap.add_argument("--output", default="legacy-drive-browser.json")
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()
    asyncio.run(main_async(args))

if __name__ == "__main__":
    main()
