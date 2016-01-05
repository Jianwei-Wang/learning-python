from socket import *
from time import ctime

HOST = ''
PORT = 54321
BUFSIZE = 1024
ADDR = (HOST, PORT)

ss = socket(AF_INET, SOCK_STREAM)
ss.bind(ADDR)
ss.listen(5)

while True:
	print 'Waiting for connection...'
	cs, addr = ss.accept()
	print '...connected from:', addr

	while True:
		data = cs.recv(BUFSIZE)
		if not data:
			break
		cs.send('[%s] %s' % (ctime(), data))

	cs.close()

ss.close()
