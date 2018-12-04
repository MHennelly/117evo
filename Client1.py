import socket                
  
s = socket.socket()          
  
port = 12345

print ("Please enter the server's IP:")
IP = input()
  
s.connect((IP, port)) 

x = "no"
while x is "no":
    print("Please enter the target:")
    T = input()
    s.send(T.encode())
    print(s.recv(1024).decode())
    print("Do you want to try again?")
    x = input()
    s.send(x.encode())
    print(s.recv(1024).decode())

s.close()  
