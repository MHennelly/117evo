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

repeat = True
while repeat is True:
      DataRecv = c.recv(1024).decode()
      Tx = int(DataRecv[DataRecv.find("(")+1:DataRecv.find(",")])
      Ty = int(DataRecv[DataRecv.find(",")+1:DataRecv.find(")")])
      sim = Simulation(Tx, Ty)
      sim.run()
      vel, ang = sim.getValues()
      print(vel, ang)
      a = []
      a.append(vel)
      a.append(ang)
      DataSend = "Target was hit at" + DataRecv + " with velocity " + str(a[0]) + "and angle " + str(a[1])
      c.send(DataSend.encode())
      print(c.recv(1024).decode())

c.close()
