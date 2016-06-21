import socket
import threading
import os

#Global Values
#----------------------------------------------------------------------------
host = '127.0.0.1'
port = 5000
#----------------------------------------------------------------------------


#Functions
#----------------------------------------------------------------------------
def RetrFile(name, sock):
    filename = sock.recv(1024)
    
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()
#----------------------------------------------------------------------------



#Socket transfer
#----------------------------------------------------------------------------
s = socket.socket()
s.bind((host,port))
s.listen(5)

print "Server Started."

c, addr = s.accept()
print "client connedted ip:<" + str(addr) + ">"
t = threading.Thread(target=RetrFile, args=("RetrThread", c))
t.start()         
s.close()
#----------------------------------------------------------------------------

