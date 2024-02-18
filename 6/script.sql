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
    sex TEXT,
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
    person_id INTEGER,
    FOREIGN KEY (staff_type_id) REFERENCES staff_type (id),
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

INSERT INTO address (country, city, street, house_number)
VALUES 
    ('Russia', 'Moscow', 'Lenina', 10),
    ('Russia', 'Saint Petersburg', 'Nevsky Prospect', 20),
    ('Russia', 'Yekaterinburg', 'Proletarskaya', 30),
    ('Russia', 'Novosibirsk', 'Kirova', 40),
    ('Russia', 'Kazan', 'Sovetskaya', 50),
    ('Russia', 'Vladivostok', 'Pushkina', 60),
    ('Russia', 'Rostov-on-Don', 'Lenina', 70),
    ('Russia', 'Ufa', 'Mira', 80),
    ('Russia', 'Krasnoyarsk', 'Sovetskaya', 90),
    ('Russia', 'Samara', 'Leninskaya', 100);

INSERT INTO person (first_name, middle_name, surname, contact_number, date_of_birth, sex, address_id)
VALUES 
    ('John', 'Doe', 'Doe', 1234567890, '1990-01-01', 'M', 1),
    ('Jane', 'Doe', 'Doe', 9876543210, '1985-05-15', 'F', 2),
    ('Alex', 'Smith', 'Smith', 5555555555, '1988-11-20', 'M', 3),
    ('Emma', 'Johnson', 'Johnson', 7777777777, '1975-08-10', 'F', 4),
    ('Michael', 'Williams', 'Williams', 9999999999, '1982-03-25', 'M', 5),
    ('Emily', 'Brown', 'Brown', 1111111111, '1987-09-05', 'F', 6),
    ('James', 'Jones', 'Jones', 2222222222, '1970-12-20', 'M', 7),
    ('Olivia', 'Miller', 'Miller', 3333333333, '1983-07-17', 'F', 8),
    ('William', 'Davis', 'Davis', 4444444444, '1965-04-30', 'M', 9),
    ('Sophia', 'Wilson', 'Wilson', 5555555555, '1995-11-12', 'F', 10);

INSERT INTO staff_type (type_name)
VALUES 
    ('Nurse'),
    ('Doctor'),
    ('Head Doctor');

INSERT INTO staff (staff_type_id, person_id)
VALUES 
    (2, 1),  -- Doctor
    (2, 2),  -- Doctor
    (2, 3),  -- Doctor
    (1, 4),  -- Nurse
    (3, 5);  -- Head Doctor

INSERT INTO patient (person_id, supervised_by, room, age, diagnosis)
VALUES 
    (6, 1, 101, 30, 'Flu'),      -- supervised_by: John Doe
    (7, 2, 102, 40, 'Pneumonia'), -- supervised_by: Jane Doe
    (8, 3, 103, 25, 'Angina'),    -- supervised_by: Alex Smith
    (9, 1, 104, 35, 'Gastritis'), -- supervised_by: John Doe
    (10, 2, 105, 50, 'Asthma');   -- supervised_by: Jane Doe
