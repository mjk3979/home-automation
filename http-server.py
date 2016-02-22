import http.server
import socketserver
import control

def desktop():
    control.set_input('desktop')


def off():
    control.off()


mapping = {
    'desktop' : desktop,
    'off' : off
}

class HTTPHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global index_cache
        if self.path == '/index':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(index_cache)
            return
        return super(HTTPHandler, self).do_GET()

    def do_POST(self):
        global mapping
        path = self.path[1:]
        if path not in mapping:
            return self.send_response(404)
        mapping[path]()

        return self.send_response(200)


def main():
    global index_cache
    with open('web/index.html') as f:
        index_cache = bytes(f.read().encode('UTF-8'))

    PORT=8081
    httpd = socketserver.TCPServer(('', PORT), HTTPHandler)
    httpd.serve_forever()
    

if __name__ == '__main__':
    main()
