PRAGMA foreign_keys = OFF;
DROP TABLE IF EXISTS app_address;
DROP TABLE IF EXISTS app_person;
DROP TABLE IF EXISTS app_stafftype;
DROP TABLE IF EXISTS app_staff;
DROP TABLE IF EXISTS app_patient;
DELETE FROM sqlite_sequence
WHERE name IN ('app_address', 'app_person', 'app_stafftype', 'app_staff', 'app_patient');
PRAGMA foreign_keys = ON;