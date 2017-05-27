import sys

## LEARN PYTHON THE HARD WAY, Exercises 11-20

# Exercise 11: Asking Questions
print "How old are you?",   # commas at the end of the line make it so that 
age = int(raw_input())      # input answers are inline with the question
print "How tall are you?",  # rather than appearing on the next line. Spiffy.
height = raw_input()
print "How much do you weigh?",
weight = int(raw_input())

print "You are %r years old, %r tall and %r pounds." % (age, height, weight)

print "This is only a test?",
input = sys.argv[1]   # this takes in text submitted on the command line at the
                      # same time that the program is run, versus user input.
print input

