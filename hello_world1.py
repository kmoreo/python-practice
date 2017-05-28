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
script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
