import sys

## LEARN PYTHON THE HARD WAY, Exercises 11-20

# # Exercise 11: Asking Questions
# print "How old are you?",   # commas at the end of the line make it so that 
# age = int(raw_input())      # input answers are inline with the question
# print "How tall are you?",  # rather than appearing on the next line.
# height = raw_input()
# print "How much do you weigh?",
# weight = int(raw_input())

# print "You are %s years old, %s tall and %s pounds." % (age, height, weight)

# print "This is only a test?",
# input = sys.argv[1]   # this takes in text submitted on the command line at the
#                       # same time that the program is run, versus user input.
# print input

# # Exercise 12: Prompting People
# name = raw_input("What is your name? ")
# age = int(raw_input("What is your age? "))
# city = raw_input("Where do you live? ")

# print "Your name is %s, you are %d years old, and live in %s. Spiffy" % (name, age, city)

# Exercise 13: Parameters, Unpacking, Variables
from sys import argv        # this imports just 'argv' from the sys module
                            # no need to prefix with "sys."

# script, first, second, third = sys.argv   # this works in Ruby too, except as "ARGV"

# print "The script is called:", script
# print "The first variable is:", first
# print "The second variable is:", second
# print "The third variable is:", third


# Exercise 14: Prompting and Passing
# script, user_name = argv
# prompt = '> '

# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me, %s?" % user_name
# likes = raw_input(prompt)

# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)

# print "What kind of computer do you have?"
# computer = raw_input(prompt)

# print """
# Alright, so you said %r about liking me.
# You live in %r.  Not sure where that is.
# And you have a %r computer.  Nice.
# """ % (likes, lives, computer)

## Exercise 15: Reading Files
# script, filename = argv

# txt = open(filename)

# print "Here are the contents of your file, %r:" % filename
# print txt.read()
# # print open(filename).read()   # does the same thing as the line above

# print "Want to open another file? Type the name here:",
# file_again = raw_input("> ")

# txt_again = open(file_again)

# print txt_again.read()

# txt.close()
# txt_again.close()

# print "\n\nThat's all for now. Goodbye!"

# # Exercise 16: Reading and Writing Files

# script, filename = argv

# print "We're going to erase %r. *evil laugh*" % filename
# print "If you don't want that, hit CTRL-C (^C)."
# print "If you do want that, hit RETURN."

# raw_input("?")

# print "Opening the file..."
# target = open(filename, 'a')

# ## Unnecessary since file was opened with 'w' mode
# # print "Truncating the file.  Goodbye!"
# # target.truncate()

# print "Now I'm going to ask you for three lines."

# line1 = raw_input("line 1: ")
# line2 = raw_input("line 2: ")
# line3 = raw_input("line 3: ")

# print "I'm going to write these to the file."

# target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# # target.write("\n")
# # target.write(line2)
# # target.write("\n")
# # target.write(line3)
# # target.write("\n")

# print "And finally, we close it."
# target.close()

# Exercise 17: More Files
# from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# in_file = open(from_file)
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
# in_file.close()
