from sys import argv
from os.path import exists

script, file_from, file_to = argv

print "Copying from %s to %s" % (file_from, file_to)

input = open(file_from); indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(file_to)
print "Ready, hit RETURN to containue, Ctrl-C to abort."
raw_input()

output = open(file_to, 'w')
output.write(indata)

print "Alright, all done."
output.close()
input.close()
