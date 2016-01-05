from socket import *

HOST = '121.42.212.72'
PORT = 54321
BUFSIZE = 1024
ADDR = (HOST, PORT)

cs = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    cs.sendto(data, ADDR)
    data, ADDR = cs.recvfrom(BUFSIZE)
    if not data:
        break
    print data

cs.close()
