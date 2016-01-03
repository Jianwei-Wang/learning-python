import pdb
import socket, asyncore
from asyncore import dispatcher
from asynchat import async_chat

PORT = 5005
#pdb.set_trace()

class ChatSession(async_chat):

    def __init__(self, sock, server):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\n')
        self.data = []
        self.push('Welcome to %s\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    
    def __init__(self, port, name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', PORT))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\n')

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn, self))

if __name__ == '__main__':
    s = ChatServer(PORT, 'Wechat')
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

