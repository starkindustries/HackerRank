# https://realpython.com/python-sockets/
# https://pastebin.com/uy0dhBjD

#!/usr/bin/env python3

import socket

# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

HOST = '3.93.128.89'  # Standard loopback interface address (localhost)
FAKE_PORT = 12022        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, FAKE_PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
print(f"Received: {data}")
