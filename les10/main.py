import sqlite3

con = sqlite3.connect("itstep_DB.db",5)

cur = con.cursor()

cur.execute("CREATE TABLE first_table (name TEXT);")
con.commit()

con.close()