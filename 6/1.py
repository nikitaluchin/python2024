# https://docs.python.org/3/library/sqlite3.html

import sqlite3
import os

if os.path.exists("hospital.db"):
    os.remove("hospital.db")
con = sqlite3.connect("hospital.db")
cur = con.cursor()
script_file = open("script.sql")
cur.executescript(script_file.read())
con.commit()

# Выбрать имена всех пациентов, их возраст и диагноз,
# а также имена врачей, которые надзират за ними
query = """SELECT 
    p.first_name || ' ' || p.surname,
    pat.age,
    pat.diagnosis,
    d.first_name || ' ' || d.surname
FROM 
    patient pat
JOIN 
    person p ON pat.person_id = p.id
JOIN 
    staff s ON pat.supervised_by = s.person_id
JOIN 
    person d ON s.person_id = d.id
WHERE 
    s.staff_type_id = 2; -- Выбираем только врачей
"""

cur.execute(query)
for res in cur.fetchall():
    print(res)
print()

# Подсчитать количество пациентов, находящихся под наблюдением
# каждого врача
query = """SELECT 
    p.first_name || ' ' || p.surname AS doctor_name,
    COUNT(pat.id)
FROM 
    staff s
JOIN 
    person p ON s.person_id = p.id
JOIN 
    patient pat ON s.person_id = pat.supervised_by
WHERE 
    s.staff_type_id = 2 -- Выбираем только врачей
GROUP BY
    doctor_name;
"""

cur.execute(query)
for res in cur.fetchall():
    print(res)
print()

# Выбрать всех членов персонала, отсортированных по типу персонала по убыванию
query = """SELECT 
    p.first_name || ' ' || p.surname,
    st.type_name
FROM
    staff s
JOIN 
    person p ON s.person_id = p.id
JOIN 
    staff_type st ON s.staff_type_id = st.id
ORDER BY 
    st.type_name DESC;
"""

cur.execute(query)
for res in cur.fetchall():
    print(res)

con.close()