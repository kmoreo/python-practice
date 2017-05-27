## LEARN PYTHON THE HARD WAY

# Exercise 1: A Good First Program
print "Hello World!"
print "Python print statements are preceded by 'print', versus 'puts' in Ruby"
print "Hey %s there." % "you"

# Exercise 4: Variables And Names
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars,"cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Exercise 5: More Variables and Printing
name = 'Kristen Moore'
city = 'Chicago'
pets = 3
pet_1 = 'Mierin'
pet_2 = 'Rahvin'
pet_3 = 'Reiko'
cat = 'cat'
dog = 'dog'
string = "O'Malley's Pub"

print "Let's talk about %s." % name
print "She lives in %s." % city
print "She has %d pets." % len([pet_1, pet_2, pet_3])
print "The first of these %d pets is a %s named %s." % (pets, cat, pet_1)
print "The second is a %s named %s." % (cat, pet_2)
print "The third is a %s named %s." % (dog, pet_3)
print "This is a test sentence: %r vs. %s." % (string, string)

# Exercise 6: Strings and Text
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
is_funny = 'No'
joke_statement = "Isn't that joke so funny?!"
cheese = ["cheddar", "swiss", "brie", "pepperjack"]

print x
print y
print joke_evaluation % hilarious
print joke_statement, is_funny # using a comma inserts spaces around variable values
print joke_statement + is_funny # using a + smashes them together and looks dumb
print "Cheese is awesome. %d of my favorite cheeses are: %s, %s, %s, %s, and %s." % (len(cheese)+1, cheese[0], cheese[1], cheese[2], cheese[3], 'gouda')

# Exercise 7: More Printing
ltr1 = "C"
ltr2 = "h"
ltr3 = "e"
ltr4 = "e"
ltr5 = "s"
ltr6 = "e"
ltr7 = "S"
ltr8 = "t"
ltr9 = "i"
ltr10 = "c"
ltr11 = "k"
ltr12 = "s"

print ltr1 + ltr2 + ltr3 + ltr4 + ltr5 + ltr6, # without comma two lines print
print ltr7 + ltr8 + ltr9 + ltr10 + ltr11 + ltr12 # with comma one line prints

# Exercise 8: Printing, Printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.", #lines 1, 2, and 4 will print out in single quotes
    "That you could type up right.", 
    "But it didn't sing.", # line 3 prints out in double quotes because of "didn't"
    "So I said goodnight."
)

# Exercise 9: Printing, Printing, Printing
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
# print "Here are the days: %s" % days
# print "Here are the months: ", months
print "Here are the months: %s" % months

# this is like to a HEREDOC in Ruby
print """
There's something going on here.
    With the three double-quotes.
We'll be able to type as much as we like.
  Even 4 lines if we want, or 5, or 6.
"""


