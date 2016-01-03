from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died.  You kinda suck at this.",
            "Your mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n--------"
            room = getattr(self, next)
            next = room()

    def death(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)

    def central_corridor(self):
        print 'In central_corridor function.'
        action = raw_input('> ')

        if action == '1':
            return 'death'
        elif action == '2':
            return 'death'
        elif action == '8':
            return 'laser_weapon_armory'
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print 'In laser_weapon_armory function.'
        action = raw_input('> ')

        if action == '8':
            return 'the_bridge'
        else:
            return 'death'

    def the_bridge(self):
        print 'In the bridge function.'
        action = raw_input('> ')

        if action == '1':
            return 'death'
        elif action == '8':
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

    def escape_pod(self):
        print 'In the escape_pod function'
        action = raw_input('> ')

        if action == '8':
            print "time.  You won!"
            exit(0)
        else:
            return 'death'

a_game = Game("central_corridor")
a_game.play()
