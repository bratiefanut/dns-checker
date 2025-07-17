from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import subprocess
import socket
import dns.resolver  # from `dnspython`
import dns.reversename  # for PTR lookups

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/ping")
async def ping_host(host: str):
    try:
        output = subprocess.check_output(["ping", "-c", "3", host], text=True)
        return {"output": output}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}


@app.get("/whois")
async def whois_query(domain: str):
    try:
        output = subprocess.check_output(["whois", domain], text=True)
        return {"output": output}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}


@app.get("/dns")
async def dns_lookup(
    domain: str = Query(..., description="Domain to query"),
    record_type: str = Query(..., description="Record type: A, CNAME, MX, TXT, NS, PTR")
):
    try:
        if record_type.upper() == "PTR":
            # Reverse IP lookup
            rev_name = dns.reversename.from_address(domain)
            result = dns.resolver.resolve(rev_name, "PTR")
            return {"type": "PTR", "results": [r.to_text() for r in result]}
        else:
            result = dns.resolver.resolve(domain, record_type.upper())
            return {"type": record_type.upper(), "results": [r.to_text() for r in result]}
    except Exception as e:
        return {"error": str(e)}

