"""
AI, Data Science & Statistics Workforce & Education Intelligence Dashboard
Local Python Server Runner (Zero external pip dependencies required)
Compatible with Python 3.8+ and Python 3.14+
"""

import http.server
import socketserver
import os
import sys
import json
import webbrowser

PORT = int(os.environ.get("PORT", 8000))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AIDSSTDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        # API endpoint to fetch current career_data.json
        if self.path == "/api/data":
            data_file = os.path.join(BASE_DIR, "data", "career_data.json")
            if os.path.exists(data_file):
                try:
                    with open(data_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                    self.wfile.write(json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8"))
                    return
                except Exception as e:
                    self.send_error(500, f"Error loading data: {str(e)}")
                    return
            else:
                self.send_error(404, "career_data.json not found")
                return

        # Healthcheck endpoint
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "healthy", "service": "AIDSST-Dashboard"}')
            return

        # Default route serves index.html
        if self.path == "/" or self.path == "":
            self.path = "/index.html"

        return super().do_GET()

    def do_POST(self):
        # API endpoint to save updated dataset back to disk if requested
        if self.path == "/api/data":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                post_body = self.rfile.read(content_length)
                parsed_json = json.loads(post_body.decode("utf-8"))

                data_file = os.path.join(BASE_DIR, "data", "career_data.json")
                with open(data_file, "w", encoding="utf-8") as f:
                    json.dump(parsed_json, f, ensure_ascii=False, indent=2)

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(b'{"success": true, "message": "Dataset saved successfully to data/career_data.json"}')
                return
            except Exception as e:
                self.send_error(500, f"Error saving data: {str(e)}")
                return

        return super().do_POST()

    def log_message(self, format, *args):
        # Clean terminal logging
        sys.stdout.write(f"[{self.log_date_time_string()}] {args[0]} -> {args[1]}\n")

def run_server(port=PORT, auto_open=False):
    handler = AIDSSTDashboardHandler
    # Allow socket address reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    server_started = False
    current_port = port
    max_tries = 10

    for i in range(max_tries):
        try:
            with socketserver.TCPServer(("", current_port), handler) as httpd:
                print("=" * 70)
                print(f"  AI, Data Science & Statistics Career Intelligence Dashboard")
                print("=" * 70)
                print(f"  * Local URL:     http://localhost:{current_port}")
                print(f"  * API Endpoint:  http://localhost:{current_port}/api/data")
                print(f"  * Directory:     {BASE_DIR}")
                print(f"  * Press Ctrl+C to stop the server")
                print("=" * 70)

                if auto_open:
                    webbrowser.open(f"http://localhost:{current_port}")

                server_started = True
                httpd.serve_forever()
        except OSError as e:
            if "Address already in use" in str(e) or e.errno == 10048:
                current_port += 1
                continue
            else:
                raise e

    if not server_started:
        print(f"Could not bind to any port between {port} and {port + max_tries}")

if __name__ == "__main__":
    auto_launch = "--open" in sys.argv
    run_server(PORT, auto_open=auto_launch)
