from http.server import HTTPServer, BaseHTTPRequestHandler

import json, os





class H(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":

            body = json.dumps({"status": "ok"})

        elif self.path == "/version":

            body = json.dumps({"version": os.environ.get("APP_VERSION")})

        else:

            body = "Hello from container!"

        self.send_response(200)

        self.end_headers()

        self.wfile.write(body.encode())



    def log_message(self, format, *args):

        print(f"{self.address_string()} {format % args}")  # ensure logs go to stdout



print("Server listening on port 9090")  # startup log (you'll see this in docker logs)

HTTPServer(("", 9090), H).serve_forever()