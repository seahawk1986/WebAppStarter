# WebAppStarter
Proof of concept for starting apps by clicking SVG objects

# Installation
Make sure, that you can create virtual python environments - this requires the package `python3-venv` to be installed on Ubuntu.

```
git clone https://github.com/seahawk1986/WebAppStarter.git
cd WebAppStarter
python3 -m venv .venv
. .venv/bin/activate
pip install -U uvicorn fastapi
```

# Run the backend
In the WebAppStarter director run the following command:
```
.venv/bin/uvicorn app:app --reload
```
Now you can open the URL http://localhost:8000 in your browser to see the result.
