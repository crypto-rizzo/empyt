import http.server
import socketserver
from empyt import EmpytEngine

PORT = 8002
template = EmpytEngine(template_dir='examples/templates', engine='none')

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            context = {
                'some_var': True,
                'another_var': False
            }
            content = template.render("standalone.html", context).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
