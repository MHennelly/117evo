import socket
from simulation import Simulation

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
      Tx = int(DataRecv[DataRecv.find("(")+1:DataRecv.find(",")])
      Ty = int(DataRecv[DataRecv.find(",")+1:DataRecv.find(")")])
      a = Simulation(Tx, Ty)
      a.run()
      vel, ang = a.getValues()
      a[2] = {vel, ang}
      DataSend = "Target was hit at" + DataRecv + " with velocity " + str(a[0] + "and angle " + str(a[1])
      c.send(DataSend.encode())
      x = c.recv(1024).decode()
      s.send("Recived Data.".encode())

c.close()