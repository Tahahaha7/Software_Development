.mode column
PRAGMA foreign_keys = ON;

CREATE TABLE Drivers (
    DRIVERID INTEGER PRIMARY KEY,
    CARMODEL VARCHAR(20),
    NFIRSTNAME VARCHAR(20),
    SURNAME VARCHAR(20),
    EMAIL VARCHAR(100),
    PHONE VARCHAR(20),
    RATING NUMERIC(11, 2)
);

CREATE TABLE Clients (
    CLIENTID INTEGER PRIMARY KEY,
    NFIRSTNAME VARCHAR(20),
    SURNAME VARCHAR(20),
    EMAIL VARCHAR(100),
    PHONE VARCHAR(20),
    RATING NUMERIC(11, 2)
);

CREATE TABLE Rides (
    RIDENUMBER INTEGER,
    STARTTIME DATETIME,
    ENDTIME DATETIME,
    DRIVERID INTEGER,
    CLIENTID INTEGER,
    COST NUMERIC(11, 2),
    FOREIGN KEY (DRIVERID) REFERENCES Drivers(DRIVERID),
    FOREIGN KEY (CLIENTID) REFERENCES Clients(CLIENTID)
);

INSERT INTO Drivers VALUES (1, 'Toyota', 'Carlos', 'Leva', '@gmail.com', '415 265 11453', 4.8);
INSERT INTO Drivers VALUES (2, 'Honda', 'Steven', 'Seine', '@gmail.com', '415 265 11453', 4.2);
INSERT INTO Drivers VALUES (3, 'Renault', 'Walter', 'White', '@gmail.com', '415 265 11453', 4.5);

INSERT INTO Clients VALUES (1, 'Claire', 'Leva', '@gmail.com', '415 265 11453', 4.2);
INSERT INTO Clients VALUES (2, 'Sara', 'Stevens', '@gmail.com', '415 265 11453', 4.7);
INSERT INTO Clients VALUES (3, 'Catalina', 'Lema', '@gmail.com', '415 265 11453', 4.9);
INSERT INTO Clients VALUES (4, 'Oscar', 'Keppa', '@gmail.com', '415 265 11453', 4.8);

INSERT INTO Rides VALUES (1, '2017-11-01 10:00:00', '2017-11-01 10:20:00', 1, 2, 20);
INSERT INTO Rides VALUES (2, '2017-11-01 10:30:00', '2017-11-01 10:50:00', 1, 3, 10);
INSERT INTO Rides VALUES (3, '2017-11-01 10:00:00', '2017-11-01 10:10:00', 2, 4, 13);
INSERT INTO Rides VALUES (4, '2017-11-01 10:20:00', '2017-11-01 10:50:00', 2, 3, 24);
INSERT INTO Rides VALUES (5, '2017-11-01 10:00:00', '2017-11-01 10:10:00', 3, 2, 17);
INSERT INTO Rides VALUES (6, '2017-11-01 10:20:00', '2017-11-01 10:50:00', 3, 4, 7);


SELECT '1. how many trips have been made by each driver this month, and how much they will be paid?';
SELECT '----------------------------------------------------';
SELECT Drivers.DRIVERIDR, COUNT(*) AS NUMBER_RIDES, SUM(Rides.COST) AS PAYMENT FROM Rides
    JOIN Drivers ON Drivers.DRIVERIDR = Rides.DRIVERID
    GROUP BY Drivers.DRIVERID;
SELECT '';

SELECT '2. find all the riders who have not taken any trips this month and their phone number';
SELECT '----------------------------------------------------';
SELECT * FROM Clients
    ON Clients.CLIENTID = Rides.RIDENUMBER
    GROUP BY Rides.RIDENUMBER HAVING SUM(Rides.RIDENUMBER) IS NULL;