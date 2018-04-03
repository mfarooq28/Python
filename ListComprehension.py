# I want n for each n in the num

nums = [1,2,3,4,5,6,7,8,9,10]

my_list = []

for n in nums:
    my_list.append(n)
print(my_list)

print(" mod % 2")
my_list = []
for n in nums:
    if n%2 ==0:
        my_list.append(n)
print(my_list)

print("Another method")

my_list=[n for n in nums if n%2 ==0]
print(my_list)

print("Sqauare of the ")

# 2nd method of the above code
print("Second method of list")

my_list =[n for n in nums]
print(my_list)

# square of each element
print("Sqauare of the ")
my_list =[n*n for n in nums]
print(my_list)
print("Sqauare of the map + lamda")
pass
my_list = map(lambda n: n*n, nums)
print(my_list)

print(" Filter method")

my_list = filter(lambda n: n%2 ==0, nums)
print(my_list)

print("New Program")

my_list=[]
for letter in 'abcd':
    for nums in range(4):
        my_list.append((letter,nums))
print(my_list)

print("Same Program with new method")

my_list =[(letter,nums) for letter in 'abcd' for nums in range(4)]
print(my_list)

print()
print("Now we will use Zip function")
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print zip(names,heros)

print("Now we will use Dictionary")
my_dict ={}
for names, heros in zip(names, heros):
    my_dict[names] = heros
print(my_dict)

print("Now we will use Dictionary with new method")

my_dict ={name: hero for name, hero in zip(names,heros) if name != 'Peter'}

print my_dict

print("Now we will use Dictionary with set method")

numbers =[1,1,1,2,3,3,4,4,5,5,5,6,7,8,8,9,9,9,10,10]

my_set = set()
for n in numbers:
    my_set.add(n)
print(my_set)

print()
my_set = {n for n in numbers}
print my_set

print("Use of Generator Expression")

def gen_func(numbers):
    for n in numbers:
        yield n*n
my_gen = gen_func(numbers)
for i in my_gen:
    print i
