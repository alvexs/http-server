from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def check_anagrams(s1, s2):
    if sorted(s1.casefold()) == sorted(s2.casefold()):
        return True
    return False


class AnagramServer(HTTPServer):
    data = []


class Handler(BaseHTTPRequestHandler):
    data = []

    def do_GET(self):
        if self.path.startswith('/get'):
            return_list = []
            url = urlparse(self.path)
            parsed_query = parse_qs(url.query)
            param = parsed_query.get('word')[0]

            for i in server.data:
                if check_anagrams(param, i):
                    return_list.append(i)

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            if not return_list:
                self.wfile.write('null'.encode())
            else:
                self.wfile.write(json.dumps(return_list).encode())

        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode()
        self.send_response(200)
        self.end_headers()

        server.data = json.loads(post_data)
        self.wfile.write('Data was added: {}'.format(json.dumps(server.data)).encode())
        return


if __name__ == '__main__':
    server = AnagramServer(('localhost', 8080), Handler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()
