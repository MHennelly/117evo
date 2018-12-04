import socket

s = socket.socket()

port = 12345

print ("Please enter the server's IP:")
IP = input()

s.connect((IP, port))

repeat = True
while repeat is True:
    print("Please enter the target:")
    T = input()
    s.send(T.encode())
    print(s.recv(1024).decode())
    print("Do you want to try again? Y/N")
    repeat = (input() is "Y")
    if repeat:
        s.send("yes".encode())
    else:
        s.send("no".encode())

s.close()
