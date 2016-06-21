import socket
import sys
import hashlib

#Global Values
#--------------------------------------------------------------------------------
host = '127.0.0.1'
port = 5000
lst = sys.argv[1:]
file = open ("input","rb+")
#--------------------------------------------------------------------------------

#Functions
#--------------------------------------------------------------------------------
def socket_send():
    s = socket.socket()
    s.connect((host, port))
    filename = "input"
    s.send(filename)
    data = s.recv(1024)
    s.send("OK")
    f = open('new_'+filename, 'wb')
    data = s.recv(1024)
    totalRecv = len(data)
    f.write(data)
    f.close()
    s.close()
#--------------------------------------------------------------------------------

#check and calculate the md5 and call to socket_send
#--------------------------------------------------------------------------------
if lst[0] == 'submitjob':
    file.write("%s\n" % lst)
    file_name=lst[3]
    file.write(hashlib.md5(open(file_name,"rb").read()).hexdigest())
    file.write("\n")
    file.write(hashlib.md5(open("input","rb").read()).hexdigest())
    socket_send()
    file.close()
else:
    file.write("%s\n" % lst)
    file.write(hashlib.md5(open("input","rb").read()).hexdigest())
    socket_send()
    file.close()
#--------------------------------------------------------------------------------
