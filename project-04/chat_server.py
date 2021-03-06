import pdb
import socket, asyncore
from asyncore import dispatcher
from asynchat import async_chat

PORT = 5005
NAME = 'TestChat'
class EndSession(Exception):
	pass

#pdb.set_trace()

class CommandHandler:

	def unknown(self, session, cmd):
		session.push('Unknown command: %s\n' % cmd)

	def handle(self, session, line):
		if not line.strip():
			return
		parts = line.split(' ', 1)
		cmd = parts[0]
		try:
			line = parts[1].strip()
		except IndexError:
			line = ''
		method = 'do_' + cmd
		method = getattr(self, method, None)
		try:
			method(session, line)
		except TypeError:
			self.unknown(session, cmd)

class Room(CommandHandler):

	def __init__(self, server):
		self.server = server
		self.sessions = []

	def add(self, session):
		self.sessions.append(session)

	def remove(self, session):
		self.sessions.remove(session)

	def broadcast(self, line):
		for session in self.sessions:
			session.push(line)

	def do_logout(self, session, line):
		raise EndSession

class LoginRoom(Room):
	
	def add(self, session):
		Room.add(self, session)
		self.broadcast('Welcome to %s\n' % self.server.name)
		
	def unknow(self, session, cmd):
		session.push('Please log in Use "login<nick>"\n')

	def do_login(self, session, line):
		name = line.strip()
		if not name:
			session.push('Please enter a name\n')
		elif name in self.server.users:
			session.push('The name "%s" is taken.\n' % name)
			session.push('Please try again.\n')
		else:
			session.name = name
			session.enter(self.server.main_room)

class ChatRoom(Room):

	def add(self, session):
		self.broadcast(session.name + ' has entered the room.\n')
		self.server.users[session.name] = session
		Room.add(self, session)

	def remove(self, session):
		Room.remove(self, session)
		self.broadcast(session.name + ' has left the room.\n')

	def do_say(self, session, line):
		self.broadcast(session.name + ': ' + line + '\n')

	def do_look(self, session, line):
		session.push('The following are in this room:\n')
		for other in self.sessions:
			session.push(other.name + '\n')

	def do_who(self, session, line):
		session.push('The following are logged in:\n')
		for name in self.server.users:
			session.push(name + '\n')

class LogoutRoom(Room):

	def add(self, session):
		try:
			del self.server.users[session.name]
		except KeyError:
			pass

class ChatSession(async_chat):

	def __init__(self, sock, server):
		async_chat.__init__(self, sock)
		self.server = server
		self.set_terminator('\n')
		self.data = []
		self.name = None
		self.enter(LoginRoom(server))

	def enter(self, room):
		try:
			cur = self.room
		except AttributeError:
			pass
		else:
			cur.remove(self)
		self.room = room
		room.add(self)

	def collect_incoming_data(self, data):
		self.data.append(data)

	def found_terminator(self):
		line = ''.join(self.data)
		self.data = []
		try:
			self.room.handle(self, line)
		except EndSession:
			self.handle_close()

	def handle_close(self):
		async_chat.handle_close(self)
		self.enter(LogoutRoom(self.server))

class ChatServer(dispatcher):

	def __init__(self, port, name):
		dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('', PORT))
		self.listen(5)
		self.name = name
		self.users = {}
		self.main_room = ChatRoom(self)

	def handle_accept(self):
		conn, addr = self.accept()
		ChatSession(conn, self)

if __name__ == '__main__':
	s = ChatServer(PORT, 'Wechat')
	try:
		asyncore.loop()
	except KeyboardInterrupt:
		pass

