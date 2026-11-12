from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)


class AppHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested = ROOT / self.path.split("?", 1)[0].lstrip("/")
        if not requested.exists() or requested.is_dir():
            self.path = "/index.html"
        return super().do_GET()


if __name__ == "__main__":
    print("Clarity AI running at http://localhost:8000")
    ThreadingHTTPServer(("127.0.0.1", 8000), AppHandler).serve_forever()