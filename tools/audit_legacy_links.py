#!/usr/bin/env python3
"""Check original 2023 links with explicit evidence; no automatic deletion."""
import argparse
import collections
import concurrent.futures
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError

REV="4c1f034829f112b4b57240623e101a0d594b0ecc"
FILES=["README.md","Watch TV apps/README.md","Cursor for Windows/README.md","Youtube Playlist Films.md","Google_group.txt"]
REGEX=re.compile(r"https?://[^\s<>\"')\]]+",re.I)
MDCAP=re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
DRIVE={"drive.google.com","docs.google.com"}
DEAD=("the file you have requested does not exist","this file does not exist","the file has been deleted","this item has been deleted")
AUTH=("you need access","request access","you don't have access","you do not have access","sign in to continue","you need permission")
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"

def original_links():
    found=[]
    for filename in FILES:
        run=subprocess.run(["git","show",REV+":"+filename],capture_output=True)
        if run.returncode:
            print("MISSING",filename,file=sys.stderr)
            continue
        for index,line in enumerate(run.stdout.decode("utf-8","replace").splitlines(),1):
            labels={m.group(2):m.group(1) for m in MDCAP.finditer(line)}
            for m in REGEX.finditer(line):
                url=m.group().rstrip(".,;:!?}]")
                if "[" in url: continue
                found.append({"source":filename,"line":index,"name":labels.get(url,line.strip()[:76]),"url":url})
    return found

def probe(url,timeout):
    host=(urlsplit(url).hostname or "").lower()
    gd=host in DRIVE
    response=None
    error=""
    for method in (["GET"] if gd else ["HEAD","GET"]):
        try:
            req=Request(url,method=method,headers={"User-Agent":UA,"Accept-Language":"en-US,en;q=0.8"})
            with urlopen(req,timeout=timeout) as r:
                response={"http":r.status,"final_url":r.geturl(),"body":(r.read(240000).decode("utf-8","replace") if method=="GET" else "")}
            break
        except HTTPError as e:
            response={"http":e.code,"final_url":e.geturl(),"body":e.read(70000).decode("utf-8","replace") if method=="GET" else ""}
            if not gd and method=="HEAD": continue
            break
        except Exception as e:
            error=type(e).__name__+": "+str(e)[:150]
    if response is None: return {"status":"NETWORK_ERROR","http_code":None,"evidence":error,"final_url":url,"title":""}
    code=response["http"]
    content=html.unescape(response["body"]).lower()
    mt=re.search(r"<title[^>]*>(.*?)</title>",response["body"],re.I|re.S)
    title=html.unescape(mt.group(1)).strip()[:100] if mt else ""
    if code in (404,410): status,why="DEAD_CONFIRMED","HTTP "+str(code)
    elif gd and any(x in content for x in DEAD): status,why="DEAD_CONFIRMED","Google explicit file-missing/deleted message"
    elif gd and (any(x in content for x in AUTH) or "accounts.google.com" in response["final_url"]):
        status,why="ACCESS_RESTRICTED","Sign-in or permission needed"
    elif code in (401,403,429): status,why="ACCESS_RESTRICTED","HTTP "+str(code)
    elif gd and code in range(200,300): status,why="NEEDS_BROWSER","Google page responds, folder contents NOT proven accessible"
    elif code in range(200,300): status,why="HTTP_OK","Only HTTP endpoint checked, not working service"
    else: status,why="UNCERTAIN","HTTP "+str(code)
    return {"status":status,"http_code":code,"evidence":why,"final_url":response["final_url"],"title":title}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scope",choices=["drive","all"],default="drive")
    p.add_argument("--output",default="legacy-drive-audit.json")
    p.add_argument("--timeout",type=float,default=10.0)
    p.add_argument("--workers",type=int,default=12)
    a=p.parse_args()
    refs=original_links()
    if a.scope=="drive": refs=[r for r in refs if (urlsplit(r["url"]).hostname or "").lower() in DRIVE]
    unique=list(dict.fromkeys(r["url"] for r in refs))
    if not unique: return print("ERROR: original URLs missing") or 2
    checked={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,min(a.workers,16))) as pool:
        jobs={pool.submit(probe,u,a.timeout):u for u in unique}
        for job in concurrent.futures.as_completed(jobs):
            checked[jobs[job]]=job.result()
    stats=dict(collections.Counter(v["status"] for v in checked.values()))
    report={"timestamp":datetime.now(timezone.utc).isoformat(),"source_revision":REV,"scope":a.scope,"unique_urls":len(unique),"references":len(refs),"statuses":stats,"items":[dict(row,**checked[row["url"]]) for row in refs]}
    Path(a.output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# Original 2023 URLs — actual audit","",
        "Date: "+report["timestamp"],"Links: "+str(len(unique)),"",
        "Do not treat Google HTTP 200 as publicly readable. 403 means restricted, not necessarily deleted.","",
        "| Verdict | Label | Original file:line | Link | HTTP | Evidence |","|---|---|---|---|---|---|"]
    for r in report["items"]:
        label=re.sub(r"[\n\r|]"," ",r["name"])
        md.append("| "+r["status"]+" | "+label[:65]+" | "+r["source"]+":"+str(r["line"])+" | "+r["url"].replace("|","%7C")+" | "+str(r["http_code"] or "-")+" | "+r["evidence"]+" |")
    output_md=str(Path(a.output).with_suffix(".md"))
    Path(output_md).write_text("\n".join(md)+"\n",encoding="utf-8")
    print("AUDIT",len(unique),"URLs:",json.dumps(stats,ensure_ascii=False))
    for r in report["items"]:
        if a.scope=="drive": print("DRIVE",r["status"],r["http_code"] or "-",r["source"]+":"+str(r["line"]),r["name"][:65])
    print("REPORTS",a.output,output_md)
    return 0

if __name__=="__main__":
    sys.exit(main())
