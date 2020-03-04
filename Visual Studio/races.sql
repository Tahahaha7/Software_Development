.mode column
PRAGMA foreign_keys = ON;

-- CREATING TABLES

CREATE TABLE Runners (
    RUNNERID INTEGER PRIMARY KEY,
    FIRSTNAME VARCHAR(20),
    SURNAME VARCHAR(20),
    GENDER VARCHAR(1),
    EMAIL VARCHAR(20),
    RATING NUMERIC(11, 2)
);

CREATE TABLE Races (
    RACEID INTEGER PRIMARY KEY,
    NAME VARCHAR(20)
);

CREATE TABLE Challenges (
    CHALLENGEID INTEGER PRIMARY KEY,
    NAME VARCHAR(20)
);

CREATE TABLE Events (
    CHALLENGE_KEY INTEGER,
    RACE_KEY INTEGER,
    FOREIGN KEY (CHALLENGE_KEY) REFERENCES Challenges(CHALLENGEID),
    FOREIGN KEY (RACE_KEY) REFERENCES Races(RACEID),
    PRIMARY KEY (CHALLENGE_KEY, RACE_KEY)
);

CREATE TABLE Participation (
    RUNNER_KEY INTEGER,
    RACE_KEY INTEGER,
    RUNTIME INTEGER, -- Minutes
    FOREIGN KEY (RACE_KEY) REFERENCES Races(RACEID),
    FOREIGN KEY (RUNNER_KEY) REFERENCES Runners(RUNNERID),
    PRIMARY KEY (RUNNER_KEY, RACE_KEY)
);

-- INNSERT DATA IN THE DATABASE

INSERT INTO Challenges VALUES (1, 'The marathon challenge');
INSERT INTO Challenges VALUES (2, 'The terrain challenge');

INSERT INTO Races VALUES (1, 'The ruby marathon');
INSERT INTO Races VALUES (2, 'The bridge challenge');
INSERT INTO Races VALUES (3, 'The sea to mountain sprint');
INSERT INTO Races VALUES (4, 'Flat and fast marathon');
INSERT INTO Races VALUES (5, 'The wine route stroll');

INSERT INTO Runners VALUES (1, 'Tom', 'Will', 'M', 'tom@gmail.com', 7.1);
INSERT INTO Runners VALUES (2, 'Steven', 'Hill', 'M', 'steven@gmail.com', 6.4);
INSERT INTO Runners VALUES (3, 'Sara', 'Queens', 'F', 'sara@gmail.com', 5.9);
INSERT INTO Runners VALUES (4, 'Sam', 'Claire', 'F', 'sam@gmail.com', 6.6);
INSERT INTO Runners VALUES (4, 'Ali', 'Kamara', 'M', 'ali@gmail.com', 6.2);
INSERT INTO Runners VALUES (4, 'Sam', 'Claire', 'F', 'sam@gmail.com', 6.6);

-- RELATIONAL INFORMATION

INSERT INTO Events VALUES (1, 1);
INSERT INTO Events VALUES (1, 4);
INSERT INTO Events VALUES (2, 1);
INSERT INTO Events VALUES (2, 2);
INSERT INTO Events VALUES (2, 3);

INSERT INTO Participation VALUES (1, 1, 10);
INSERT INTO Participation VALUES (1, 5, 14);
INSERT INTO Participation VALUES (2, 2, 15);
INSERT INTO Participation VALUES (2, 3, 11);
INSERT INTO Participation VALUES (3, 4, 20);
INSERT INTO Participation VALUES (3, 5, 16);
INSERT INTO Participation VALUES (3, 1, 19);
INSERT INTO Participation VALUES (4, 2, 21);

-- QUERIES
