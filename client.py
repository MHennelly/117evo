import socket

s = socket.socket()

port = 12345

s.connect(('172.30.7.241', port))

print(s.recv(1024))
s.close()
