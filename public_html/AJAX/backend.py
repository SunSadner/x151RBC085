from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import SimpleHTTPServer

PORT = 10085

class AjaxHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        # Send the thml message
        self.wfile.write("Nikita Afanasjevs, 151RBC085")
        return

try:
    server = HTTPServer(('', PORT), AjaxHandler)
    print 'Started AJAX handler on port' , PORT
    server.serve_forever()

except KeyboardInterrupt:
    print '^C recieved, shutting down the web srever'
    server.socket.close()

