# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months
print
"""
There's something going on here.
With the three double- quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print "I am 6'feet & 2\" tall."
print 'I am 6\'2" tall.'
# escape double- quote inside string
# escape single- quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print()
pass

while True:
    for i in ["/","- ","|","\\","|"]:
        print "%s\r" % i,
