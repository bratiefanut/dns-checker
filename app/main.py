from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import subprocess

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
