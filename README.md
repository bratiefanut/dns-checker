Requirements:

Python 3.10+

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
