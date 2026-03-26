#!/usr/bin/env python3
import http.server, socketserver, os, sys

port = int(os.environ.get('PORT', 8080))
os.chdir('/Users/louisportal/Desktop/Websites/consulaires2026')
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}", flush=True)
    httpd.serve_forever()
