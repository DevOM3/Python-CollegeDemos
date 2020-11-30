import sqlite3

con = sqlite3.connect("Database")
cur = con.cursor()

c = cur.execute("SELECT * FROM DB")
for i in c:
    print(i)

con.commit()
con.close()
