
class Dispatcher:

    def unknown(self, cmd):
        print 'Unknown command: "%s"' % cmd

    def dispatch(self, line):
        if not line.strip():
            return
        parts = line.split(' ', 1)
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        cmd = 'do_' + parts[0]
        method = getattr(self, cmd, None)
        print method

class Room(Dispatcher):

    def do_aaa(self):
        pass
    def do_bbb(self):
        pass

d = Room()

d.dispatch('aaa')
d.dispatch('aaa ')
d.dispatch('bbb')
d.dispatch('bbb ')
