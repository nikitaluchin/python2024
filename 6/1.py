# https://docs.python.org/3/library/sqlite3.html

import sqlite3
import os

if os.path.exists("hospital.db"):
    os.remove("hospital.db")
con = sqlite3.connect("hospital.db")
cur = con.cursor()
script_file = open("script.sql")
cur.executescript(script_file.read())

# con.commit()
# con.close()