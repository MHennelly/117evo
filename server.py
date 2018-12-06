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
sim = Simulation(0,0)
sim.firstGen()
while repeat is True:
    DataRecv = c.recv(1024).decode()
    print("Received target from client: ",DataRecv)
    Tx = int(DataRecv[DataRecv.find("(")+1:DataRecv.find(",")])
    Ty = int(DataRecv[DataRecv.find(",")+1:DataRecv.find(")")])
    sim.changeTarget(Tx,Ty)
    for _ in range(100):
        sim.naturalSelection()
        x, y, vel, ang, height, gen = sim.getValues()
        DataSend = "Target: " + "(" + str(x) + "," + str(y) + ")\nVelocity: " + str(vel) + "\nAngle: " + str(ang) + "\nCalculated Final Height: " + str(height) + "\nGeneration: " + str(gen) + "\n\n\n"
        c.send(DataSend.encode())
        c.recv(1024).decode()
    x = c.recv(1024).decode()
    print("Received message from client: ",x)
    if x is "Y":
        repeat = True
        print("Changing target...")
    if x is "N":
        repeat = False
        print("Terminating server...\n")
c.close()
