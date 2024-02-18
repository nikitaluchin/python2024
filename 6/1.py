# https://docs.python.org/3/library/sqlite3.html

import sqlite3

con = sqlite3.connect("medicine.db")
cur = con.cursor()
