import sqlite3

# connection =  sqlite3.connect("employee.db")
connection =  sqlite3.connect(':memory:')

c = connection.cursor()
c.execute("""CREATE TABLE employees (
    first TEXT,
    last TEXT,
    pay integer
    )""")

# c.execute("INSERT INTO employees VALUES ('James', 'Alex', 4000)")
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format("Jamie","Alex",12))
c.execute("INSERT INTO employees VALUES (?, ?, ?)", ('James', 'Alex', 4000))
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': 'James', 'last': 'Alex', 'pay': 4000})

connection.commit()

c.execute("SELECT * FROM employees WHERE last = 'Alex'")

print(c.fetchall())
# c.fetchmany()
# c.fetchall()
connection.commit()
connection.close()