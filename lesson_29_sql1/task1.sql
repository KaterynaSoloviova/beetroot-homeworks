CREATE TABLE users (
    UserID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    Phone varchar(255),
    Birthday date
);

ALTER TABLE users
RENAME COLUMN Phone to MobilePhone;

ALTER TABLE users
RENAME  to clients;

ALTER TABLE clients
RENAME COLUMN UserID to ID;

ALTER TABLE clients ADD Email varchar(255);

INSERT INTO clients (ID, LastName, FirstName, Address, City, MobilePhone, Birthday, Email)
VALUES (1, 'Kirshok', 'Stefan', 'Berliner str. 13', 'Berlin', '01764553289', '1976-10-21', 'stefan.kirshok@gmail.com');

INSERT INTO clients (ID, LastName, FirstName, Address, City, MobilePhone, Birthday, Email)
VALUES (2, 'King', 'Kong', 'Jungle str. 1', 'New York', '01664353289', '1970-06-14', 'king.kong@gmail.com');

INSERT INTO clients (ID, LastName, FirstName, Address, City, MobilePhone, Birthday, Email)
VALUES (3, 'Masliuk', 'Yurko', 'Waldow str. 3', 'Erfurt', '01765438732', '1991-02-03', 'yurko.thebest@gmail.com');

UPDATE clients SET City = 'Oslo'
WHERE ID = 1;

DELETE FROM clients WHERE ID = 2;
