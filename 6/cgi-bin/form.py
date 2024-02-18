from warnings import filterwarnings
import cgi
import sqlite3

# ignore msg that cgi is deprecated
filterwarnings("ignore")

form = cgi.FieldStorage()
country = form.getfirst("country")
city = form.getfirst("city")
street = form.getfirst("street")
house_number = form.getfirst("house_number")
if house_number:
    house_number = int(house_number)

first_name = form.getfirst("first_name")
middle_name = form.getfirst("middle_name")
surname = form.getfirst("surname")
contact_number = form.getfirst("contact_number")
date_of_birth = form.getfirst("date_of_birth")
sex = form.getfirst("sex")
address_id = form.getfirst("address_id")

if contact_number:
    contact_number = int(contact_number)
if address_id:
    address_id = int(address_id)

con = sqlite3.connect("hospital.db")
cur = con.cursor()

if all((country, city, street, house_number)):
    query = f"INSERT INTO address (country, city, street, house_number) VALUES ('{country}', '{city}', '{street}', '{house_number}')"
    cur.execute(query)
    con.commit()

if all((first_name, middle_name, surname, contact_number, date_of_birth, sex, address_id)):
    query = f"INSERT INTO person (first_name, middle_name, surname, contact_number, date_of_birth, sex, address_id) VALUES ('{first_name}', '{middle_name}', '{surname}', '{contact_number}', '{date_of_birth}', '{sex}', '{address_id}')"
    cur.execute(query)
    con.commit()
    
con.close()

print('Content-type: text/html\n')
print('<meta http-equiv="refresh" content="0; url=/">')