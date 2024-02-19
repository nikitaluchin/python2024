import sqlite3
from xml.dom import minidom
import cgi

form = cgi.FieldStorage()
xml_string = form.getfirst("xml")

con = sqlite3.connect('hospital.db')
cur = con.cursor()

doc = minidom.parseString(xml_string)
root = doc.documentElement
table = root.tagName
columns = root.getElementsByTagName('structure')[0].childNodes
columns = list(filter(lambda node: node.nodeType == 1, columns))
table_body = ""
fkeys = ""
for column in columns:
    table_body += column.nodeName
    column_info = column.firstChild.data.split()
    table_body += " " + column_info[0]
    if column_info[1] == "1":
        table_body += " PRIMARY KEY"
    if column.nodeName == "id":
        table_body += " AUTOINCREMENT"
    table_body += ', '
    if len(column_info) == 4:
        fkeys += f"FOREIGN KEY ({column.nodeName}) REFERENCES {column_info[-2]} ({column_info[-1]}), "
table_body += fkeys
table_body = table_body[:-2]

cur.execute(f"CREATE TABLE {table} ( {table_body} );")
con.commit()

items = root.getElementsByTagName('items')[0].childNodes
items = list(filter(lambda node: node.nodeType == 1, items))
for item in items:
    item_columns = list(filter(lambda node: node.nodeType == 1, item.childNodes))
    column_names = ", ".join([item_column.nodeName for item_column in item_columns])
    column_values = list(map(lambda value: f"'{value}'", [item_column.firstChild.data for item_column in item_columns]))
    column_values = ", ".join(column_values)
    cur.execute(f"INSERT INTO {table} ({column_names}) VALUES ({column_values})")
con.commit()

con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')
