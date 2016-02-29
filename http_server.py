import http.server
import socketserver
import control

mapping = {inp: lambda: control.set_input(inp) for inp in control.mappings}
mapping['off'] = control.off

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


def generate_index():
    global mapping
    with open('web/index.html') as f:
        template = f.read()
    links = []
    for action in mapping:
        links.append('<a href="#" onclick="send_command(\'{inp}\');"><h2>{inp}</h2></a>'.format(inp=action))
    return template.replace('#BODY', '\n'.join(links))

def main(port=8081):
    global index_cache
    index_cache = bytes(generate_index().encode('UTF-8'))
    httpd = socketserver.TCPServer(('', port), HTTPHandler)
    httpd.serve_forever()
    

if __name__ == '__main__':
    main()
