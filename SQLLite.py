import sqlite3
from Employees import employees

conn =sqlite3.connect('employees.db')
curs = conn.cursor()
#curs.execute("""CREATE TABLE employees (
#                first text,
#                last text,
#                pay integer)""")

#curs.execute("INSERT INTO employees VALUES ('Jhon','Wax', 7500)")
#curs.commit()
Emp1 = employees('James','Doe', 6500)
Emp2 = employees('Jhon','Doe', 7500)

print(Emp1.first, Emp1.last, Emp1.pay)
print()
print(Emp2.first, Emp2.last, Emp2.pay)
print(Emp1.email)
print()
print(Emp2.email)
print(Emp1.fullname)
print()
print(Emp2.fullname)
curs.execute("INSERT INTO employees VALUES ('{}','{}','{}')".format(Emp1.first, Emp1.last, Emp1.pay))
conn.commit()
curs.execute(" SELECT * FROM employees ")
print(curs.fetchall())
conn.commit()
conn.close()
