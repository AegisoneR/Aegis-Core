import json
import os
import secrets
import hashlib
import base64
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from aegis_core import process_user_input
from reservation_store import ReservationStore


ROOT = os.path.dirname(__file__)
DB_PATH = os.path.join(ROOT, "reservations.sqlite")
STORE = ReservationStore(DB_PATH)

# Admin credentials (set via environment variable ADMIN_PASSWORD)
# Generate a secure hash on first run if not set
def get_admin_hash():
    password = os.environ.get("ADMIN_PASSWORD", "")
    if not password:
        return None
    return hashlib.sha256(password.encode()).hexdigest()

ADMIN_CREDENTIALS = {
    "username": "admin",
    "password_hash": get_admin_hash()
}


def check_admin_auth(self):
    """Check if request has valid admin credentials"""
    if ADMIN_CREDENTIALS["password_hash"] is None:
        return False
    
    auth_header = self.headers.get("Authorization", "")
    if not auth_header.startswith("Basic "):
        return False
    
    try:
        encoded = auth_header[6:]
        decoded = base64.b64decode(encoded).decode("utf-8")
        username, password = decoded.split(":", 1)
        
        username_hash = hashlib.sha256(username.encode()).hexdigest()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        return (username_hash == hashlib.sha256(ADMIN_CREDENTIALS["username"].encode()).hexdigest() and
                password_hash == ADMIN_CREDENTIALS["password_hash"])
    except Exception:
        return False


def send_auth_required(self):
    """Send 401 Unauthorized response with Basic Auth challenge"""
    self.send_response(401)
    self.send_header("WWW-Authenticate", 'Basic realm="Aegis Admin"')
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.send_header("Content-Length", "0")
    self.end_headers()


class AegisHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        resource = parsed_path.path

        if resource in ("/", ""):
            self._serve_file("index.html", "text/html; charset=utf-8")
            return

        if resource == "/admin":
            if not check_admin_auth(self):
                send_auth_required(self)
                return
            self._serve_file("admin.html", "text/html; charset=utf-8")
            return

        if resource == "/token":
            self._serve_file("token.html", "text/html; charset=utf-8")
            return

        if resource == "/manufacturer-inquiry.html":
            self._serve_file("manufacturer-inquiry.html", "text/html; charset=utf-8")
            return

        if resource == "/distributor-inquiry.html":
            self._serve_file("distributor-inquiry.html", "text/html; charset=utf-8")
            return

        if resource == "/investor-inquiry.html":
            self._serve_file("investor-inquiry.html", "text/html; charset=utf-8")
            return

        if resource == "/admin-data":
            if not check_admin_auth(self):
                send_auth_required(self)
                return
            reservations = STORE.list_reservations()
            summary = {
                "total": len(reservations),
                "by_vehicle": {},
                "by_country": {},
            }
            for reservation in reservations:
                vehicle = reservation.get("vehicle", "Unknown")
                country = reservation.get("country", "Unknown")
                summary["by_vehicle"][vehicle] = summary["by_vehicle"].get(vehicle, 0) + 1
                summary["by_country"][country] = summary["by_country"].get(country, 0) + 1
            self._send_json(200, {"reservations": reservations, "summary": summary})
            return

        safe_path = resource.lstrip("/")
        if safe_path in {"styles.css", "app.js", "admin.css"}:
            content_type = "text/css; charset=utf-8" if safe_path.endswith(".css") else "application/javascript; charset=utf-8"
            self._serve_file(safe_path, content_type)
            return

        self._send_json(404, {"error": "not found"})

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/validate":
            length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(length).decode("utf-8")

            try:
                payload = json.loads(raw_body) if raw_body else {}
            except json.JSONDecodeError:
                payload = {}

            result = process_user_input(payload)
            self._send_json(200, result)
            return

        if parsed_path.path == "/reserve":
            length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(length).decode("utf-8")

            try:
                payload = json.loads(raw_body) if raw_body else {}
            except json.JSONDecodeError:
                payload = {}

            result = process_user_input(payload)
            if result["success"]:
                reservation_id = STORE.save(result["validated_data"])
                result["reservation_id"] = reservation_id

            self._send_json(200, result)
            return

        if parsed_path.path == "/submit-inquiry":
            length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(length).decode("utf-8")

            try:
                payload = json.loads(raw_body) if raw_body else {}
            except json.JSONDecodeError:
                payload = {}

            # Validate inquiry type and process
            inquiry_type = payload.get("type", "unknown")
            if inquiry_type in ["manufacturer", "distributor", "investor"]:
                # Save inquiry to store
                inquiry_id = STORE.save_inquiry(payload)
                self._send_json(200, {
                    "success": True,
                    "message": f"✓ Thank you for your {inquiry_type} inquiry! We'll review it and contact you shortly.",
                    "inquiry_id": inquiry_id,
                })
            else:
                self._send_json(400, {
                    "success": False,
                    "error": "Invalid inquiry type",
                })
            return

        self._send_json(404, {"error": "not found"})

    def _serve_file(self, filename, content_type):
        file_path = os.path.join(ROOT, filename)
        if not os.path.exists(file_path):
            self._send_json(404, {"error": "not found"})
            return

        with open(file_path, "rb") as handle:
            content = handle.read()

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _send_json(self, status_code, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        return


def main():
    server = ThreadingHTTPServer(("0.0.0.0", 8000), AegisHandler)
    print("Aegis UI running at http://127.0.0.1:8000")
    server.serve_forever()


if __name__ == "__main__":
    main()
