DROP DATABASE IF EXISTS ELECTIONSCONGRESSMANS;
CREATE DATABASE ELECTIONSCONGRESSMANS;

-- créer l'utilisateur pour la BDD
DROP USER IF EXISTS 'ElectionsCongressmans'@'localhost'  ;
CREATE USER 'ElectionsCongressmans'@'localhost' IDENTIFIED BY 'ASimpleP@ssW0rd' ;

-- ajout de droits
GRANT DELETE ON ELECTIONSCONGRESSMANS.* TO 'ElectionsCongressmans'@'localhost' ;
GRANT INSERT ON ELECTIONSCONGRESSMANS.* TO 'ElectionsCongressmans'@'localhost' ;
GRANT UPDATE ON ELECTIONSCONGRESSMANS.* TO 'ElectionsCongressmans'@'localhost' ;
GRANT SELECT ON ELECTIONSCONGRESSMANS.* TO 'ElectionsCongressmans'@'localhost' ;

USE ELECTIONSCONGRESSMANS;

-- 1 Department
CREATE TABLE IF NOT EXISTS DEPARTMENT(
    DepartmentId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    DepartmentName VARCHAR(50),
    DepartmentNumber INT
);

-- 2 Party
CREATE TABLE IF NOT EXISTS PARTY(
    PartyId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    PartyName VARCHAR(50),
    ShortName VARCHAR(3)
);

-- 3 District
CREATE TABLE IF NOT EXISTS DISTRICT(
    DistrictId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Position INT,
    DistrictName VARCHAR(25),
    DepartmentId INT NOT NULL,
    Registered INT,
    Abstention INT,
    Voting INT,
    BlankVoting INT,
    NullVoting INT,
    FOREIGN KEY (DepartmentId) REFERENCES DEPARTMENT(DepartmentId)
);

-- 4 Candidate
CREATE TABLE IF NOT EXISTS CANDIDATE(
    CandidateId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    CandidateLastName VARCHAR(50),
    CandidateFirstName VARCHAR(50),
    CandidateSexe VARCHAR(1),
    CandidateBirthDate DATE,
    PartyId INT NOT NULL,
    Job VARCHAR(150),
    OldCandidate BIT,
    DistrictId INT NOT NULL,
    VoteFirstRound INT,
    RateVoteExpressedFirstRound FLOAT,
    RateVoteRegisteredFirstRound FLOAT,
    VoteSecondRound INT,
    RateVoteExpressedSecondRound FLOAT,
    RateVoteRegisteredSecondRound FLOAT,
    FOREIGN KEY (PartyId) REFERENCES PARTY(PartyId),
    FOREIGN KEY (DistrictId) REFERENCES DISTRICT(DistrictId)
);

-- 5 Deputy
CREATE TABLE IF NOT EXISTS DEPUTY(
    DeputyId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    DeputyLastName VARCHAR(50),
    DeputyFirstName VARCHAR(50),
    DeputySexe VARCHAR(1),
    DeputyBirthDate DATE,
    OldCandidate BIT,
    CandidateId INT NOT NULL,
    FOREIGN KEY (CandidateId) REFERENCES CANDIDATE(CandidateId)
);

-- 6 Result
CREATE TABLE IF NOT EXISTS RESULT(
    ResultId INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    RoundNumber INT,
    StateCompute VARCHAR(25),
    Registered INT,
    Abstaining INT,
    RateAbstaining FLOAT,
    Voting INT,
    RateVoting FLOAT,
    BlankBalot INT,
    RateBlankRegistered FLOAT,
    RateBlankVoting FLOAT,
    NullBallot INT,        
    RateNullRegistered FLOAT,
    RateNullVoting FLOAT,
    Expressed INT,
    RateExpressRegistered FLOAT,
    RateExpressVoting FLOAT,
    DistrictId INT NOT NULL,
    FOREIGN KEY (DistrictId) REFERENCES DISTRICT(DistrictId)
);

-- Add Datas 
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Divers extrême gauche','DXG');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Parti radical de gauche','RDG');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Nouvelle union populaire écologique et sociale','NUP');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Divers gauche','DVG');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Ecologistes','ECO');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Régionaliste','REG');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Ensemble ! (Majorité présidentielle)','ENS');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Divers Centre','DVC');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Divers','DIV');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Union des Démocrates et des Indépendants','UDI');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Les Républicains','LR');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Divers droite','DVD');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Droite souverainiste','DSV');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Reconquête !','REC');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Rassemblement National','RN');
INSERT INTO PARTY(PartyName, ShortName) VALUES ('Divers extrême droite','DXD');