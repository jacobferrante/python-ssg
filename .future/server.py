import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("http://127.0.0.1:8080")
        httpd.serve_forever()

