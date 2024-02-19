import sqlite3
from xml.dom import minidom
import cgi

form = cgi.FieldStorage()
table = form.getfirst("table")

doc = minidom.Document()
root = doc.createElement(f'{table}')
doc.appendChild(root)
structure = doc.createElement('structure')
items = doc.createElement('items')
root.appendChild(structure)
root.appendChild(items)

con = sqlite3.connect('hospital.db')
cur = con.cursor()

try:
    cur.execute(f'SELECT * FROM {table}')
except sqlite3.OperationalError as e:
    print('Content-type: text/html\n')
    print(e)
    exit(0)

for row in cur.fetchall():
    item = doc.createElement('item')
    items.appendChild(item)
    # cur.description - кортежи, где содержатся имена столбцов
    for i, column_name in enumerate(cur.description):
        column_value = row[i]
        column_element = doc.createElement(column_name[0])
        column_element.appendChild(doc.createTextNode(str(column_value)))
        item.appendChild(column_element)

cur.execute(f"PRAGMA foreign_key_list({table})")
fkeys = cur.fetchall()
cur.execute(f"PRAGMA table_info({table})")
for row in cur.fetchall():
    column = doc.createElement(row[1])
    structure.appendChild(column)
    column_info = row[2] + " " + str(row[-1])
    for fk in fkeys:
        if fk[3] == row[1]:
            column_info += " " + fk[2] + " " + fk[4]
            break
    column.appendChild(doc.createTextNode(column_info))

xml_str = doc.toprettyxml(indent='  ')
# print(xml_str)
print("Content-type: text/html\n")

print(f"""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Exported address table</title>
        </head>
        <body>
            <textarea rows=50 cols=60>
{xml_str}
            </textarea>
    """)

print("""</body>
        </html>""")

con.close()
