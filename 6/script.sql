CREATE TABLE address (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    city TEXT,
    street TEXT,
    house_number INTEGER
);

CREATE TABLE person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    middle_name TEXT,
    surname TEXT,
    contact_number INTEGER,
    date_of_birth TEXT,
    gender TEXT,
    address_id INTEGER,
    FOREIGN KEY (address_id) REFERENCES address (id)
);

CREATE TABLE staff_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT
);

CREATE TABLE staff (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_type_id INTEGER,
    staff_type_name TEXT,
    person_id INTEGER,
    FOREIGN KEY (staff_type_id) REFERENCES staff_type (id),
    FOREIGN KEY (staff_type_name) REFERENCES staff_type (type_name),
    FOREIGN KEY (person_id) REFERENCES person (id)
);

CREATE TABLE patient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_id INTEGER,
    supervised_by INTEGER,
    room INTEGER,
    age INTEGER,
    diagnosis TEXT,
    FOREIGN KEY (person_id) REFERENCES person (id),
    FOREIGN KEY (supervised_by) REFERENCES staff (id)
);