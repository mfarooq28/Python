import sqlite3
conn =sqlite3.connect('employees.db')
curs = conn.cursor()
#curs.execute("""CREATE TABLE employees (
#                first text,
#                last text,
#                pay integer)""")
#curs.execute("INSERT INTO employees VALUES ('Corey','Schafer', 5000)")
curs.execute(" SELECT * FROM employees WHERE last = 'Schafer' ")
print(curs.fetchall())
conn.commit()
conn.close()
