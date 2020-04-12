import os
from pyppeteer import __chromium_revision__, __pyppeteer_home__
from pathlib import Path

DOWNLOADS_FOLDER = Path(__chromium_revision__) / 'local-chromium'

REVISION = os.environ.get('PYPPETEER_CHROMIUM_REVISION', __pyppeteer_home__)

print(DOWNLOADS_FOLDER)

print(REVISION)