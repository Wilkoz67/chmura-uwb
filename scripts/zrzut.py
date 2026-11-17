"""Otwiera adres w osobnym oknie Chrome (czysty profil) i zapisuje zrzut tego okna z paskiem adresu.

Użycie: python scripts/zrzut.py <url> <plik.png>
"""
import ctypes
import subprocess
import sys
import tempfile
import time

from PIL import ImageGrab

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
X, Y, W, H = 0, 0, 1280, 860

url, out = sys.argv[1], sys.argv[2]
ctypes.windll.user32.SetProcessDPIAware()
profil = tempfile.mkdtemp(prefix="chrome-lab2-")
p = subprocess.Popen([
    CHROME, f"--user-data-dir={profil}", "--no-first-run", "--no-default-browser-check",
    "--disable-features=Translate,OptimizationHints", "--new-window", "--lang=pl", "--force-device-scale-factor=1",
    f"--window-position={X},{Y}", f"--window-size={W},{H}", url,
])
time.sleep(6)
# okno Chrome na wierzch
hwnd = ctypes.windll.user32.GetForegroundWindow()
buf = ctypes.create_unicode_buffer(512)
ctypes.windll.user32.GetWindowTextW(hwnd, buf, 512)
print("okno:", buf.value)
ImageGrab.grab(bbox=(X, Y, X + W, Y + H)).save(out)
p.terminate()
subprocess.run(["taskkill", "/F", "/T", "/PID", str(p.pid)], capture_output=True)
