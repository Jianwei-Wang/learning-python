from socket import *
from time import ctime

HOST = '121.42.212.72'
PORT = 54321
BUFSIZE = 1024
ADDR = HOST, PORT

ss = socket(AF_INET, SOCK_DGRAM)
ss.bind(ADDR)

while True:
	print 'Waiting for message...'
	data, addr = ss.recvfrom(BUFSIZE)
	ss.sendto('[%s] %s' % (ctime(), data), addr)
	print '...received from and returned to:', addr

ss.close()
