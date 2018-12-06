import socket

s = socket.socket()

port = 12345

IP = input("Server IP: ")

s.connect((IP, port))

repeat = True
while repeat is True:
    T = input("Enter target coordinates: ")
    s.send(T.encode())
    for _ in range(100):
        print(s.recv(1024).decode())
        s.send("buffer".encode())
    repeat = (input("Do you want to try again? Y/N: ") is "Y")
    if repeat is True:
        s.send("Y".encode())
    else:
        s.send("N".encode())

s.close()
