from socket import *

HOST = '121.42.212.72'
PORT = 54321
BUFSIZE = 1024
ADDR = HOST, PORT

cs = socket(AF_INET, SOCK_STREAM)
cs.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    cs.send(data)
    data = cs.recv(BUFSIZE)
    if not data:
        break
    print data

cs.close()
