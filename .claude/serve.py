import http.server, socketserver, os, sys
os.chdir('/Users/louisportal/Desktop/Website/consulaires2026')
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 8080), handler) as httpd:
    print(f"Serving on port 8080", flush=True)
    httpd.serve_forever()
