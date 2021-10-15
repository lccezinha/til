from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import start_http_server, Summary
import time

host_name = "localhost"
server_port = 8080
metrics_port = 8081
request_response_summary = Summary("app_response_latency_seconds", "Response latency")

class MyServer(BaseHTTPRequestHandler):

    @request_response_summary.time()
    def do_GET(self):
        # start_time = time.time()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8")
        )
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        # time_taken = time.time() - start_time
        # request_response_summary.observe(time_taken)


if __name__ == "__main__":
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        start_http_server(metrics_port)
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
