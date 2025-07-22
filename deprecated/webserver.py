import deprecated.database as database
import http.server
import json
import os
import deprecated.gw2api as gw2api

FILENAME = __file__.split(os.sep)[-1].split('.')[0]

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        content = None
        file_routes = {
        '/': '/index.html',
        '/index.css' : '/index.css',
        '/index.js' : '/index.js'
        }

        path = self.path.split('?')[0]
        if path in file_routes:
            file_type = file_routes[path].split('.')[-1]
            self_dir = os.path.dirname(os.path.abspath(__file__))
            if file_type in ['html', 'css', 'js']:
                with open(self_dir + file_routes[path], 'r') as file:
                    content = file.read()
                content = content.encode()

            if content is not None:
                self.send_response(200)
            else:
                self.send_response(500)

            if file_type == 'html':
                self.send_header('content-type', 'text/html')
            elif file_type == 'css':
                self.send_header('content-type', 'text/css')
            elif file_type == 'js':
                self.send_header('content-type', 'text/javascript')
            elif file_type == 'json':
                self.send_header('content-type', 'application/json')
            elif file_type == 'png':
                self.send_header('content-type', 'image/png')
            
            self.end_headers()

            self.wfile.write(content)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_length)
        post_body = post_body.decode()

        self.send_response(200)
        # post_body = post_body.replace('+', ' ')
        # keyValuePairs = post_body.split('&')
        # print(keyValuePairs)
        print(post_body)
        
        APIResults = {}
        # for pair in keyValuePairs:
        #     key, value = pair.split('=')
        #     APIResults[key] = value
        APIResults['name'] = "testName"
        # if "API_access_token" in APIResults:
        APIResults['API_access_token'] = post_body
        #     print(APIResults['API_access_token'])
        
        
        # db = database.DB('access_tokens.sqlite3')
        # db.log_DB(APIResults)

        self.send_response(201)
        self.end_headers()
        return

def main():
    with open('network.json') as networkfile:
        network = json.load(networkfile)
    #configure server
    PORT = network['http_server']['port']
    IP = network['http_server']['ip']    

    # PORT = 8000
    # IP = 'localhost'
    server = http.server.HTTPServer((IP, PORT), handler)
    print(f'[{FILENAME}] Running on ' + str(IP) + ' port ' + str(PORT))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
    finally:
        server.shutdown()

if __name__ == '__main__':
    main()