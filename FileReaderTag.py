import csv

input_file = csv.DictReader(open("Cities.csv"))
for row in input_file:
    print row
#rows = [ line.strip().split(' ') for line in data.split('\n') ]
