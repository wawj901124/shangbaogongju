import os
from pathlib import Path
from pyppeteer import __chromium_revision__, __pyppeteer_home__
DOWNLOADS_FOLDER = Path(__pyppeteer_home__) / 'local-chromium'
REVISION = os.environ.get('PYPPETEER_CHROMIUM_REVISION', __chromium_revision__)
chromiumExecutable = {
'linux': DOWNLOADS_FOLDER / REVISION / 'chrome-linux' / 'chrome',
'mac': (DOWNLOADS_FOLDER / REVISION / 'chrome-mac' / 'Chromium.app' /
'Contents' / 'MacOS' / 'Chromium'),
'win32': DOWNLOADS_FOLDER / REVISION / 'chrome-win32' / 'chrome.exe',
'win64': DOWNLOADS_FOLDER / REVISION / 'chrome-win32' / 'chrome.exe',
}
print(chromiumExecutable['win64'])