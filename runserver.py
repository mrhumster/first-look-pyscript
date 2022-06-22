import http.server, ssl

server_address = ('192.168.1.159', 443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile='https/localhost.key',
                               server_side=True,
                               certfile='https/localhost.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()