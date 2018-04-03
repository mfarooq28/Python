from string import Template
class MyTemplate(Template):
        delimiter = '#'
def Main():
    cart = []
    cart.append(dict(item = 'Cocke', price=70, qty = 3, ))
    cart.append(dict(item = 'Cacke', price=700, qty =1 ))
    cart.append(dict(item= 'Chicken', price=240, qty =3.7))

    t = MyTemplate("#qty x #item = #price")
    total = 0
    print('Cart')
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("Total: " + str(total))

if __name__ == '__main__':
    Main()
