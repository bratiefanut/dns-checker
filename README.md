Requirements:

Python 3.10+

Folder structure - setup step and first commit

├── app/
│   ├── main.py                ← FastAPI app
│   ├── dns_utils.py           ← Helper functions (DNS, ping, etc.)
│   ├── templates/
│   │   └── index.html         ← Jinja2 HTML template
├── requirements.txt           ← Python dependencies
├── run.sh                     ← Start script (optional)
├── README.md


requirements.txt:
fastapi
uvicorn
jinja2
aiofiles
python-whois


python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

To run the app:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
