'''
import turtle

# First Program with While loop
counter = 0
while counter < 4 :
	turtle.forward(100)
	turtle.right(90)
	counter += counter
# New Program with for loop
pass

for steps in range(4):
    turtle.forward(200)
    turtle.right(120)
'''
# New Program printing a list with while loop

colors =['red','green','blue', 'purple']
i = 0
while i < len(colors):
    print(colors[i])
    i += 1

# New Program printing a list with for loop

colors =['red','green','blue', 'purple']

for i in range(len(colors)):
    print(colors[i])

# list
guests =['Susan','Christopeher', 'Billi', 'Satya','Sonali']

nbrValueInList = len(guests)

for i in range(nbrValueInList):
    print(guests[i])

# for in
colors =['red','green','blue', 'purple']
for i in colors:
    print(i)
#
presidents = ["Washington", "Adams", "Jefferson", "Madison"]
for i in range(len(presidents)):
    print("President {}: {}".format(i+1,presidents[i]))
#
guests=[]

name=' '

while name != "DONE" :
    name = input("Enter the name of guests or enter DONE when finished : ")
    guests.append(name)

guests.sort()
for guest in guests:
    print(guest)
