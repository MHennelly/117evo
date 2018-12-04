import socket                
  
s = socket.socket()          
print ("Socket successfully created")
   
port = 12345                
  
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
s.listen(5)      
print ("socket is listening")            
  
c, addr = s.accept()      
print ('Got connection from', addr)

DataRecv= ""

x = "yes"
while x != "no":
      DataRecv = c.recv(1024).decode()
      Tx = DataRecv[DataRecv.find("(")+1:DataRecv.find(",")]
      Ty = DataRecv[DataRecv.find(",")+1:DataRecv.find(")")]
      a[2] = {}
      DataSend = "Target was hit at" + DataRecv + " with velocity " + str(a[0] + "and angle " + str(a[1])
      c.send(DataSend.encode())
      x = c.recv(1024).decode()
      s.send("Recived Data.".encode())

c.close()
