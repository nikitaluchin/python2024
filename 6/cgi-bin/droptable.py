import sqlite3
import cgi

form = cgi.FieldStorage()
table = form.getfirst("table_to_drop")

query = f"""PRAGMA foreign_keys = OFF;
        DROP TABLE {table};
        PRAGMA foreign_keys = ON;"""
con = sqlite3.connect("hospital.db")
cur = con.cursor()
try:
    cur.executescript(query)
except sqlite3.OperationalError as e:
    print('Content-type: text/html\n')
    print(e)
    exit(0)


print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')
