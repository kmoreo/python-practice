# LEARN PYTHON THE HARD WAY

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
