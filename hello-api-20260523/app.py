from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os, sys, logging

# Configure logging to ensure all output goes to stdout/stderr
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    stream=sys.stdout,  # Explicitly send logs to stdout so docker logs captures them
)
logger = logging.getLogger(__name__)


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"})
            logger.info(f"GET /health from {self.client_address[0]}")
            status, content_type = 200, "application/json"
        elif self.path == "/version":
            version = os.environ.get("APP_VERSION", "1.1")
            body = json.dumps({"version": version})
            logger.info(f"GET /version - {version}")
            status, content_type = 200, "application/json"
        elif self.path == "/":
            body = "Hello from container!"
            logger.info(f"GET / from {self.client_address[0]}")
            status, content_type = 200, "text/plain"
        else:
            body = json.dumps({"error": "not found"})
            logger.info(f"GET {self.path} from {self.client_address[0]} -> 404")
            status, content_type = 404, "application/json"

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, format, *args):
        # Override to ensure HTTP logs go to logger (stdout)
        logger.info(f"HTTP {self.address_string()}: {format % args}")


try:
    logger.info(f"APP_VERSION={os.environ.get('APP_VERSION', '1.1')}")
    logger.info("Server listening on port 9090")
    HTTPServer(("", 9090), H).serve_forever()
except Exception as e:
    logger.error(
        f"Server error: {e}", exc_info=True
    )  # exc_info=True includes traceback to stderr
    sys.exit(1)
