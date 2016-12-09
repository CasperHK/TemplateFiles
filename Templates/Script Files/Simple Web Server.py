# Import the required packages.
import http.server  
import socketserver

# Setting up the port for the web server.
PORT = 4422

# Creating a HTTP request handler for handling HTTP request.
Handler = http.server.SimpleHTTPRequestHandler

# Making the TCP web server.
httpd = socketserver.TCPServer(("", PORT), Handler)

# Print success message.
print("serving at port", PORT)

# Serve multiple request.
httpd.serve_forever()
