import os
import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from gi.repository import Gio

app = FastAPI()
app.mount("/svg", StaticFiles(directory="svg"), name="svg")


def launch_app(desktop_file_uri, *uris):
    launcher = Gio.DesktopAppInfo.new_from_filename(desktop_file_uri)
    launcher.launch_uris(uris, None)

@app.get('/', response_class=HTMLResponse)
async def root():
    HTML = Path("index.html").read_text()
    return HTML

@app.get('/app/{appname}')
async def launch_by_name(appname):
    for d in os.environ['XDG_DATA_DIRS'].split(':'):
        p = Path(d)
        for desktop_file in p.rglob(f'*/{appname}.desktop'):
            print(desktop_file)
            print(f"launch {desktop_file.resolve()}")
            launch_app(str(desktop_file.resolve()).encode())
            return
