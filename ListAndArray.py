guests = ['Christopher','Susan', 'Bill', 'Staya']
for currentGuest in guests:
    print(currentGuest)
#
pass
guests.sort()
for guest in guests:
    print(guest)

#
pass
y=[]
for x in range(0,9,2):
    y.append(x)
    print(y)
#
pass

c=['New York', 'Seoul', 'Beijing']
l=['USA','Korea', 'China']
cl={}
j =0
for x in c:
    cl[x]=l[j]
    j+=1
    print(cl)
#
pass

m = {1:[1,2,3],\
      2:[4,5,6], \
      3:[7,8,9]}
print(m[1], \
      m[2], \
      m[3])
print(m[2][1])
print(m[3][2])
print(m[3][1])

#
pass

data=['XBOX 360','150','NEW']
print(data)
product, price, condition = data.split('|')
assert isinstance (product,object )
product

