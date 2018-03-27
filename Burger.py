print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There's something going on here.
With the three double- quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split \n on a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print
print
print
print
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
"""
Time to Travel
"""
# New Program
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "So, you're %r years old, %r inch tall and %r heavy." % (
age, height, weight)

# New Program
print(3%100)
print(25*3%4)
print 100-25*3%4
print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > - 2
print "Is it greater or equal?", 5 >= - 2
print "Is it less or equal?", 5 <= - 2

### New Program Cars

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print ("There are only ", drivers, " drivers available.")
print ("There will be ", cars_not_driven, " empty cards today. ")
print ("We can transport ", carpool_capacity, " people Today. ")
print ( "We have ", passengers, " to carpool today. ")
print (" We need to put about ", average_passengers_per_car, " in each car. ")
