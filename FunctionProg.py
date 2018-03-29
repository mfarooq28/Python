def main():
    printMessage()
    return


def printMessage():
    print('Have a nice day!')
    return


# Execute the main function
# In order to that function must be created.
main()

# New Program
print

pass


def main():
    printNames()
    return


def printNames():
    names = ['Farooq', 'Haroon', 'Mamoon', 'Hassan']
    for name in names:
        print 'Hello', name
    return


main()

print

pass


def printMsg(message):
    print(message)
    return

printMsg("Hello my Dear!")

#
pass
print()

def displayMessage(greetings, name):
    message = greetings +"<=> "+ name
    print(message)
    return
displayMessage('Hi', 'Christopher')
displayMessage('Hello', 'Christopher')
displayMessage('Good Morning', 'Christopher')

# New program taking user input

print
pass

def main():
    names =['Farooq', 'Zahid', 'Jamil', 'Waheed', 'Asma']
    name = raw_input("Enter the name of new Guest ")
    names.append(name)
    printTitle(names)
    return
def printTitle(list):
    for name in list:
        print(name)
    return
main()

# New Program about Function

pass
print

def getMessage(name):
    message = 'Hello ', name
    return message
def printMessage(name):
    print(message)
    return
outPut = getMessage('Javed')
printMsg(outPut)


# New program about function

def main():
    #names = getNames()
    printNames(getNames())
    return

def getNames():
    names =['Christopher', 'William', 'Jhonsan']
    newName = raw_input("Enter the Guest Name ")
    names.append(newName)
    return names

def printNames(names):
    for name in names:
        print(name)
#        print()
#        print(name)
    return
main()
