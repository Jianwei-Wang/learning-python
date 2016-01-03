from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)."
print "If you do want that hit RETRUN."

raw_input("?")

print "Opening the file..."
txt = open(filename, 'w')

print "Truncating the file. Goodbye!"
txt.truncate()

print "Now I'm going to ask you three lines."

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "Now I'm going to write these to the file!"

txt.write(line1 + '\n' + line2 + '\n' +
          line3 + '\n')
txt.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
txt.close()
