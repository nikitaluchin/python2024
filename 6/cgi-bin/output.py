from warnings import filterwarnings
import cgi
import sqlite3

# ignore msg that cgi is deprecated
filterwarnings("ignore")

def prepare_row(row):
    row = list(map(lambda value: f"<td>{value}</td>", row))
    row = "\n".join(row)
    return "<tr>\n" + row + "\n</tr>"

con = sqlite3.connect("hospital.db")
cur = con.cursor()

def get_rows(query):
    cur.execute(query)
    rows = cur.fetchall()
    rows = list(map(prepare_row, rows))
    return "\n".join(rows)

rows_address = get_rows("SELECT * FROM address")
rows_person = get_rows("SELECT * FROM person")

print("Content-type: text/html\n")

print(f"""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hospital tables</title>
        </head>
        <body>
            <h3>Addresses</h3>
            <table>
            <thead>
                <tr>
                <td>ID</td>
                <td>Country</td>
                <td>City</td>
                <td>Street</td>
                <td>House number</td>
                </tr>
            </thead>
            <tbody>
                {rows_address}
            </tbody>
            </table>
            <h3>Person</h3>
            <table>
            <thead>
                <tr>
                <td>ID</td>
                <td>First name</td>
                <td>Middle name</td>
                <td>Surname</td>
                <td>Contact number</td>
                <td>Date of birth</td>
                <td>Sex</td>
                <td>Address ID</td>
                </tr>
            </thead>
            <tbody>
                {rows_person}
            </tbody>
            </table><br>
        """)

print("""<form action="/redirect.html">
        <input type="submit" value="Main page">
        </form><br>""")

print("""</body>
        </html>""")

con.close()
