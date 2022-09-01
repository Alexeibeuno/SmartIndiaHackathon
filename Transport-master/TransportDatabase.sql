-- Database: 'Transport'
-- Database for the logistics department covering the transportation of products
-- Author: Natalia Skiba

CREATE DATABASE Transport CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE Transport;
SELECT DATABASE();


-- --------------------------------------------------------
-- --------------------------------------------------------

-- USERS AND LOGIN INFORMATION

-- --------------------------------------------------------
-- --------------------------------------------------------

-- USER CREATION: admin - all privileges 

-- CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';
-- GRANT ALL ON transport.* TO 'admin'@'localhost';

-- --------------------------------------------------------

-- USER CREATION: user - select privilege only

-- CREATE USER 'user'@'localhost' IDENTIFIED BY 'abc';
-- GRANT SELECT ON transport.* TO 'user'@'localhost';
-- ALTER USER 'user'@'localhost' WITH MAX_QUERIES_PER_HOUR 20;

-- --------------------------------------------------------

-- USER CREATION: manager - select & INSERT privileges

-- CREATE USER 'manager'@'localhost' IDENTIFIED BY 'def';
-- GRANT SELECT ON transport.* TO 'manager'@'localhost';
-- GRANT INSERT ON transport.* TO 'manager'@'localhost';
-- ALTER USER 'manager'@'localhost' WITH MAX_QUERIES_PER_HOUR 90;

-- --------------------------------------------------------

-- Table structure for table 'loginToDatabase' 

CREATE TABLE IF NOT EXISTS LoginToDatabase(
	login VARCHAR(30),
	passwd VARCHAR(30)
);

-- Inserting data for table 'LoginToDatabase'

INSERT INTO LoginToDatabase VALUES ('admin','admin');
INSERT INTO LoginToDatabase VALUES ('user','abc');
INSERT INTO LoginToDatabase VALUES ('manager','def');

-- --------------------------------------------------------
-- --------------------------------------------------------

-- TABLES

-- --------------------------------------------------------
-- --------------------------------------------------------

-- Table structure for table 'Countries'

CREATE TABLE IF NOT EXISTS Countries (
    CountryID VARCHAR(11) NOT NULL PRIMARY KEY,
    CountryNameEN VARCHAR(20) NOT NULL,
    CountryNamePL VARCHAR(20) NOT NULL,
    CountryNameLocal VARCHAR(20) NOT NULL
);

-- Inserting data for table 'Countries'

INSERT INTO Countries
	(CountryID, CountryNameEN, CountryNamePL, CountryNameLocal)
VALUES
	('PL', 'Poland', 'Polska', 'Polska'),
    ('CZ', 'Czech Republic', 'Republika Czeska', 'Česká republika'),
    ('DE', 'Germany', 'Niemcy', 'Deutschland'),
    ('FR', 'France', 'Francja', 'France'),
    ('RU', 'Russia', 'Rosja', 'Росси́я')
;

-- --------------------------------------------------------

-- Table structure for table 'Regions'

CREATE TABLE IF NOT EXISTS Regions (
    RegionID VARCHAR(11) NOT NULL PRIMARY KEY,
    RegionNameEN VARCHAR(50) NOT NULL,
    RegionNameLocal VARCHAR(50) NOT NULL,
    RegionTypeEN VARCHAR(20) DEFAULT NULL,
	RegionTypeLocal VARCHAR(20) DEFAULT NULL,
    CountryID VARCHAR(11) NOT NULL,
    FOREIGN KEY (CountryID)
        REFERENCES Countries (CountryID)
)  ENGINE=INNODB;

-- Inserting data for table 'Regions'

-- Inserting data for table 'Regions' for Poland

INSERT INTO Regions
	(RegionID, RegionNameEN, RegionNameLocal, RegionTypeEN, RegionTypeLocal, CountryID)
VALUES
	('DS', 'Lower Silesian', 'dolnośląskie', 'voivodeship', 'województwo', 'PL'),
    ('KP', 'Kuyavian-Pomeranian', 'kujawsko-pomorskie', 'voivodeship', 'województwo', 'PL'),
    ('LU', 'Lublin', 'lubelskie', 'voivodeship', 'województwo', 'PL'),
    ('LB', 'Lubusz', 'lubuskie', 'voivodeship', 'województwo', 'PL'),
    ('LD', 'Łódź', 'łódzkie', 'voivodeship', 'województwo', 'PL'),
    ('MA', 'Lesser Poland', 'małopolskie', 'voivodeship', 'województwo', 'PL'),
    ('MZ', 'Masovian', 'mazowieckie', 'voivodeship', 'województwo', 'PL'),
    ('OP', 'Opole', 'opolskie', 'voivodeship', 'województwo', 'PL'),
    ('PK', 'Subcarpathian', 'podkarpackie', 'voivodeship', 'województwo', 'PL'),
    ('PD', 'Podlaskie', 'podlaskie', 'voivodeship', 'województwo', 'PL'),
    ('PM', 'Pomeranian', 'pomorskie', 'voivodeship', 'województwo', 'PL'),
    ('SL', 'Silesian', 'śląskie', 'voivodeship', 'województwo', 'PL'), 
    ('SK', 'Holy Cross', 'świętokrzyskie', 'voivodeship', 'województwo', 'PL'),
	('WN', 'Warmian-Masurian', 'warmińsko-mazurskie', 'voivodeship', 'województwo', 'PL'),
	('WP', 'Greater Poland', 'wielkopolskie', 'voivodeship', 'województwo', 'PL'),
    ('ZP', 'West Pomeranian', 'zachodniopomorskie', 'voivodeship', 'województwo', 'PL');

-- Inserting data for table 'Regions' for Czech Republic

INSERT INTO Regions
	(RegionID, RegionNameEN, RegionNameLocal, RegionTypeEN, RegionTypeLocal, CountryID)
VALUES
	('A', 'Prague ', 'Hlavní město Praha', 'region', 'kraj', 'CZ'),
	('S', 'Central Bohemian Region', 'Středočeský kraj', 'region', 'kraj', 'CZ'),
	('C', 'South Bohemian Region', 'Jihočeský kraj', 'region', 'kraj', 'CZ'),
	('P', 'Plzeň Region', 'Plzeňský kraj', 'region', 'kraj', 'CZ'),
	('K', 'Karlovy Vary Region', 'Karlovarský kraj', 'region', 'kraj', 'CZ'),
	('U', 'Ústí nad Labem Region', 'Ústecký kraj', 'region', 'kraj', 'CZ'),
	('L', 'Liberec Region', 'Liberecký kraj', 'region', 'kraj', 'CZ'),
	('H', 'Hradec Králové Region', 'Královéhradecký kraj', 'region', 'kraj', 'CZ'),
	('E', 'Pardubice Region', 'Pardubický kraj', 'region', 'kraj', 'CZ'),
	('M', 'Olomouc Region', 'Olomoucký kraj', 'region', 'kraj', 'CZ'),
	('T', 'Moravian-Silesian Region', 'Moravskoslezský kraj', 'region', 'kraj', 'CZ'),
	('B', 'South Moravian Region', 'Jihomoravský kraj', 'region', 'kraj', 'CZ'),
	('Z', 'Zlín Region', 'Zlínský kraj', 'region', 'kraj', 'CZ'),
	('J', 'Vysočina Region', 'Kraj Vysočina', 'region', 'kraj', 'CZ');

-- Inserting data for table 'Regions' for Germany 

INSERT INTO Regions
	(RegionID, RegionNameEN, RegionNameLocal, RegionTypeEN, RegionTypeLocal, CountryID)
VALUES  
	('BW', 'Baden-Württemberg', 'Baden-Württemberg', 'state', 'Land', 'DE'),
    ('BY', 'Bavaria', 'Bayern', 'state', 'Land', 'DE'),
    ('BE', 'Berlin', 'Berlin', 'state', 'Land', 'DE'),
    ('BB', 'Brandenburg', 'Brandenburg', 'state', 'Land', 'DE'),
    ('HB', 'Bremen', 'Bremen', 'state', 'Land', 'DE'),
    ('HH', 'Hamburg', 'Hamburg', 'state', 'Land', 'DE'),
    ('HE', 'Hesse', 'Hessen', 'state', 'Land', 'DE'),
    ('NI', 'Lower Saxony', 'Niedersachsen', 'state', 'Land', 'DE'),
    ('MV', 'Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern', 'state', 'Land', 'DE'),
    ('NW', 'North Rhine-Westphalia', 'Nordrhein-Westfalen', 'state', 'Land', 'DE'),
    ('RP', 'Rhineland-Palatinate', 'Rheinland-Pfalz', 'state', 'Land', 'DE'),
    ('SL2', 'Saarland', 'Saarland', 'state', 'Land', 'DE'),
    ('SN', 'Saxony', 'Sachsen', 'state', 'Land', 'DE'),
    ('ST', 'Saxony-Anhalt', 'Sachsen-Anhalt', 'state', 'Land', 'DE'),
    ('SH', 'Schleswig-Holstein', 'Schleswig-Holstein', 'state', 'Land', 'DE'),
    ('TH', 'Thuringia', 'Thüringen', 'state', 'Land', 'DE');
    
-- Inserting data for table 'Regions' for France

INSERT INTO Regions
	(RegionID, RegionNameEN, RegionNameLocal, RegionTypeEN, RegionTypeLocal, CountryID)
VALUES
	('44', 'Grand Est', 'Grand Est', 'region', 'région', 'FR'),
	('75', 'Nouvelle-Aquitaine', 'Nouvelle-Aquitaine', 'region', 'région', 'FR'),
	('84', 'Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes', 'region', 'région', 'FR'),
	('27', 'Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté', 'region', 'région', 'FR'),
	('53', 'Brittany', 'Bretagne', 'region', 'région', 'FR'),
	('24', 'Centre-Val de Loire', 'Centre-Val de Loire', 'region', 'région', 'FR'),
	('11', 'Île-de-France', 'Île-de-France', 'region', 'région', 'FR'),
	('76', 'Occitanie', 'Occitanie', 'region', 'région', 'FR'),
	('32', 'Hauts-de-France', 'Hauts-de-France', 'region', 'région', 'FR'),
	('28', 'Normandy', 'Normandie', 'region', 'région', 'FR'),
	('52', 'Pays de la Loire', 'Pays de la Loire', 'region', 'région', 'FR'),
	('93', 'Provence-Alpes-Côte d\'Azur', 'Provence-Alpes-Côte d\'Azur', 'region', 'région', 'FR'),
	('94', 'Corsica', 'Corse', 'region', 'région', 'FR'),
	('03', 'French Guiana', 'Guyane', 'region', 'région', 'FR'),
	('01', 'Guadeloupe', 'Guadeloupe', 'region', 'région', 'FR'),
	('02', 'Martinique', 'Martinique', 'region', 'région', 'FR'),
	('06', 'Mayotte', 'Mayotte', 'region', 'région', 'FR'),
	('04', 'Réunion', 'La Réunion', 'region', 'région', 'FR');

-- Inserting data for table 'Regions' for Russia

INSERT INTO Regions
	(RegionID, RegionNameEN, RegionNameLocal, RegionTypeEN, RegionTypeLocal, CountryID)
VALUES
	('Central', 'Central Federal District', 'Tsentralny federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('South', 'Southern Federal District', 'Yuzhny federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('Northwest', 'Northwestern Federal District', 'Severo-Zapadny federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('FarEast', 'Far Eastern Federal District', 'Dalnevostochny federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('Siberia', 'Siberian Federal District', 'Sibirsky federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('Ural', 'Ural Federal District', 'Uralsky federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('Volga', 'Volga Federal District', 'Privolzhsky federalny okrug', 'Federal district', 'federalnyye okruga', 'RU'),
	('Caucasus', 'North Caucasian Federal District', 'Severo-Kavkazsky federalny okrug', 'Federal district', 'federalnyye okruga', 'RU');

-- --------------------------------------------------------

-- Table structure for table 'Departments'

CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID VARCHAR(11) NOT NULL PRIMARY KEY,
    DepartmentName VARCHAR(30) NOT NULL,
    ManagerID VARCHAR(11) DEFAULT NULL
);

-- Inserting data for table 'Departments'

INSERT INTO Departments
	(DepartmentID, DepartmentName, ManagerID)
VALUES
	('HR','Human Resources',''),
    ('IT','Information technology',''),
    ('FINAN','Finance and Accounting',''),
	('TRANS','Transportation','FILPLA'),
    ('PURCH', 'Purchasing', ''),
    ('SALES', 'Sales', '')
;

-- --------------------------------------------------------

-- Table structure for table 'Jobs'

CREATE TABLE IF NOT EXISTS Jobs (
    JobID VARCHAR(11) NOT NULL PRIMARY KEY,
    JobTitle VARCHAR(35) NOT NULL DEFAULT ' ',
    MinSalary DECIMAL(7 , 2 ) DEFAULT NULL,
    MaxSalary DECIMAL(7 , 2 ) DEFAULT NULL CHECK (MaxSalary <= 20000)
);

-- Inserting data for table 'Jobs'
	
INSERT INTO Jobs
	(JobID, JobTitle, MinSalary, MaxSalary)
VALUES
    ('Rail', 'Rail transport coordinator', '5000', '15000'),
    ('Road', 'Road transport coordinator', '5000', '15000'),
    ('Freight', 'Freight coordinator', '5000', '15000'),
    ('Analyst', 'Analyst - transportation', '4000', '10000'),
    ('TRManager', 'Transportation manager', '7000', '19000')
;

-- --------------------------------------------------------

-- Table structure for table 'Employees'

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID VARCHAR(6) NOT NULL PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(25) NOT NULL,
    PESEL VARCHAR(11), 
    Gender VARCHAR(6),
    Title VARCHAR(30) NOT NULL,
    TitleOfCourtesy VARCHAR(25),
    BirthDate DATE NOT NULL,
    HireDate DATE NOT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    RegionID VARCHAR(11) NOT NULL,
    CountryID VARCHAR(11) NOT NULL,
    MobilePhone VARCHAR(12) DEFAULT NULL,
    HomePhone VARCHAR(12) DEFAULT NULL,
    ManagerID VARCHAR(11) DEFAULT NULL,
    DepartmentID VARCHAR(11) DEFAULT NULL,
    JobID VARCHAR(11) NOT NULL,
    Salary DECIMAL(7 , 2 ) DEFAULT NULL,
    Notes MEDIUMTEXT,
    FOREIGN KEY (CountryID)
        REFERENCES Countries (CountryID),
	FOREIGN KEY (RegionID)
        REFERENCES Regions (RegionID),
	FOREIGN KEY (DepartmentID)
        REFERENCES Departments (DepartmentID)
        ON DELETE SET NULL,
    FOREIGN KEY (JobID)
        REFERENCES Jobs (JobID)
        ON DELETE NO ACTION
)  ENGINE=INNODB;

-- Inserting data for table 'Employees'

INSERT INTO Employees 
	(EmployeeID, FirstName, LastName, PESEL, Gender, Title, TitleOfCourtesy, BirthDate, HireDate, Address, City, PostalCode, RegionID, CountryID, MobilePhone, HomePhone, ManagerID, DepartmentID, JobID, Salary, Notes)
VALUES
	('KATNOW', 'Katarzyna', 'Nowak', '85031402355', 'Female', 'Rail transport coordinator', 'Mrs.', '1985-03-14', '2012-07-01', 'Address1', 'Warszawa', '01-256', 'MZ', 'PL', '48604757999', '', 'FILPLA', 'TRANS', 'Rail', '8000', ''),
	('MARKOW', 'Marek', 'Kowal', '80040315024', 'Male', 'Road transport coordinator', 'Mr.', '1980-04-03', '2013-02-01', 'Address2', 'Warszawa', '02-756', 'MZ', 'PL', '48502657889', '', 'FILPLA', 'TRANS', 'Road', '9000', ''),
	('PAWDOB', 'Paweł', 'Dobosz', '76120301156', 'Male', 'Freight coordinator', 'Mr.', '1976-12-03', '2016-06-01', 'Address3', 'Warszawa', '01-153', 'MZ', 'PL', '48602905904', '', 'FILPLA', 'TRANS', 'Freight', '7000', ''),
	('DARGAR', 'Darek', 'Gawron', '81080790044', 'Male', 'Analyst - transportation', 'Mr.', '1981-08-07', '2015-06-01', 'Address4', 'Warszawa', '02-645', 'MZ', 'PL', '486025690561', '', 'FILPLA', 'TRANS', 'Analyst', '5000', ''),
	('FILPLA', 'Filip', 'Płatek', '72041301193', 'Male', 'Transportation manager', 'Mr.', '1972-04-13', '2014-09-01', 'Address5', 'Warszawa', '02-665', 'MZ', 'PL', '48603756709', '', ' ', 'TRANS', 'TRManager', '15000', '')
;

-- Altering the Employees table - adding information regarding the number of supervised orders per person
/*
ALTER TABLE Employees ADD OrdersCount INT;
SELECT * FROM Employees;

UPDATE Employees e SET OrdersCount = (SELECT COUNT(*) FROM Orders o WHERE o.EmployeeID = e.EmployeeID);
*/

-- --------------------------------------------------------

-- Table structure for table 'Suppliers'

CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID VARCHAR(11) NOT NULL PRIMARY KEY,
    CompanyName VARCHAR(40) NOT NULL,
    ContactName VARCHAR(40) DEFAULT NULL,
    ContactTitle VARCHAR(30) DEFAULT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    RegionID VARCHAR(11) DEFAULT NULL,
    CountryID VARCHAR(11) NOT NULL,
    Phone VARCHAR(12) DEFAULT NULL,
	FOREIGN KEY (RegionID)
        REFERENCES Regions (RegionID),
    FOREIGN KEY (CountryID)
        REFERENCES Countries (CountryID)
)  ENGINE=INNODB;

-- Inserting data for table 'Suppliers'

INSERT INTO Suppliers 
	(SupplierID, CompanyName, ContactName, ContactTitle, Address, City, PostalCode, RegionID, CountryID, Phone)
VALUES
	('Plutzer', 'Plutzer Chemistry', 'Regina Winkler', 'Sales manager', 'Tiergartenstrae 5', 'Berlin', '10785', 'BE', 'DE', '0109984510'),
	('Plonsk', 'Płońsk SA', 'Krzysztof Szczęsny', 'Sales manager', 'Warszawska 134', 'Płońsk', '09-100', 'MZ', 'PL', '48607535832'),
	('Pruszcz', 'Pruszcz SA', 'Marlena Dobrowolna', 'Sales manager', 'Bydgoska 12', 'Pruszcz', '80-008', 'PM', 'PL', '48504123565'),
    ('Palova', 'Palova Ltd.', 'Ian Devling', 'Sales manager', '471 Serangon', 'Dětenice', '507-23', 'H', 'CZ', '420203456787')
;

-- --------------------------------------------------------

-- Table structure for table 'Categories'

CREATE TABLE IF NOT EXISTS Categories (
    CategoryID VARCHAR(11) NOT NULL PRIMARY KEY,
    CategoryName VARCHAR(40) NOT NULL,
    Description MEDIUMTEXT
);

-- Inserting data for table 'Categories'

INSERT INTO Categories
	(CategoryID, CategoryName, Description)
VALUES
	('SOD','Soda',''),
    ('SAL','Salt',''),
	('PPP','Plant protection products','agriculture, forestry, horticulture')
;
    
-- --------------------------------------------------------

-- Table structure for table 'Products'

CREATE TABLE IF NOT EXISTS Products (
    ProductID VARCHAR(11) NOT NULL PRIMARY KEY,
    ProductName VARCHAR(40) NOT NULL,
    SupplierID VARCHAR(11) NOT NULL,
    CategoryID VARCHAR(11) NOT NULL,
    FOREIGN KEY (SupplierID)
        REFERENCES Suppliers (SupplierID),
    FOREIGN KEY (CategoryID)
        REFERENCES Categories (CategoryID)
)  ENGINE=INNODB;

-- Inserting data for table 'Products'

INSERT INTO Products
	(ProductID, ProductName, SupplierID, CategoryID)
VALUES
	('STAB', 'Salt in tabs', 'Plutzer', 'SAL'),
    ('SANA', 'Salt with anticaking agent', 'Pruszcz', 'SAL'),
    ('BASO', 'Baking soda', 'Palova', 'SOD'),
    ('REP1', 'Repelent1', 'Plonsk', 'PPP'),
    ('REP2', 'Repelent2', 'Pruszcz', 'PPP')
;
-- --------------------------------------------------------

-- Table structure for table 'Customers'

CREATE TABLE IF NOT EXISTS Customers (
    CustomerID VARCHAR(11) NOT NULL PRIMARY KEY,
    CompanyName VARCHAR(40) NOT NULL,
    ContactName VARCHAR(40) DEFAULT NULL,
    ContactTitle VARCHAR(30) DEFAULT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    RegionID VARCHAR(11) DEFAULT NULL,
    CountryID VARCHAR(11) NOT NULL,
    MobilePnone VARCHAR(12) DEFAULT NULL,
    DeskPhone VARCHAR(12) DEFAULT NULL,
    FOREIGN KEY (RegionID)
        REFERENCES Regions (RegionID),
    FOREIGN KEY (CountryID)
        REFERENCES Countries (CountryID)
)  ENGINE=INNODB;

-- Inserting data for table 'Customers'

INSERT INTO Customers 
	(CustomerID, CompanyName, ContactName, ContactTitle, Address, City, PostalCode, RegionID, CountryID, MobilePnone, DeskPhone)
VALUES
	('MIN', 'MineIvo', 'Jean-Guy Lauzon', 'Purchasing manager', '203, Rue des Francs-Bourgeois', 'Paris', '75016', '11', 'FR', '103830068', ''),
    ('LAN', 'LandAged', 'Sebastian Bein', 'Production manager', 'Bogenallee 51', 'Frankfurt', '60488', 'HE', 'DE', '069 99275', ''),
	('PES', 'Pesticides Kelly', 'Kelly Jones', 'Purchasing manager', '210, Rue Marcel Hatet', 'Nantes', '44000', '52', 'FR', '', ''),
	('BIO', 'BioChem', 'Antonina Zaharova', 'Purchasing manager', 'Aviatorov St., 1', 'Bryansk', '241035', 'Central', 'RU', '', '+74832569658')
;

-- --------------------------------------------------------

-- Table structure for table 'Shippers'

CREATE TABLE IF NOT EXISTS Shippers (
    ShipperID INTEGER(3) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CompanyName VARCHAR(40) NOT NULL,
    ContactName VARCHAR(40) DEFAULT NULL,
    ContactTitle VARCHAR(30) DEFAULT NULL,
    Address VARCHAR(60) NOT NULL,
    City VARCHAR(15) NOT NULL,
    PostalCode VARCHAR(10) NOT NULL,
    RegionID VARCHAR(11) DEFAULT NULL,
    CountryID VARCHAR(11) NOT NULL,
    MobilePhone VARCHAR(12) DEFAULT NULL,
    DeskPhone VARCHAR(12) DEFAULT NULL,
	FOREIGN KEY (RegionID)
        REFERENCES Regions (RegionID),
    FOREIGN KEY (CountryID)
        REFERENCES Countries (CountryID)
)  ENGINE=INNODB;


-- Inserting data for table 'Shippers'

INSERT INTO Shippers
	(ShipperID, CompanyName, ContactName, ContactTitle, Address, City, PostalCode, RegionID, CountryID, MobilePhone, DeskPhone)
VALUES
	(1, 'EKO-TRANS', 'Aleksandra Bysiak', 'Key account manager', 'Address1', 'Warszawa', '02-645', 'MZ', 'PL', '+48503456982', ''),
    (2, 'Pekaes', 'Konrad Niemcewicz', 'Sales representative', 'Address2', 'Łódź', '90-050', 'LD', 'PL', '+48604123432', ''),
    (3, 'PKP Cargo', 'Jacek Walenty', 'Key accaunt manager', 'Address3', 'Warszawa', '01-245', 'MZ', 'PL', '', '0226328765'),
    (4, 'Polonia TRANS', 'Paulina Moskal', 'Sales director', 'Address4', 'Szczecin', '70-412', 'ZP', 'PL', '+48505609908', ''),
	(5, 'SeaShell', 'Renata Polak', 'Sales specialist', 'Address5', 'Gdańsk', '80-853', 'PM', 'PL', '+48502578764', ''),
	(6, 'Hoffmann Logistics', 'Marcel Duszyński', 'Key account manager', 'Address6', 'Poznań', '60-770', 'WP', 'PL', '+48605790654', '')
;

-- --------------------------------------------------------

-- Table structure for table 'Orders'

-- SET FOREIGN_KEY_CHECKS=0;
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CustomerID VARCHAR(11) NOT NULL,
    SupplierID VARCHAR(11) NOT NULL,
    ShipperID INTEGER(3) NOT NULL,
    EmployeeID VARCHAR(6) NOT NULL,
	ModeOfTransport VARCHAR(20),
    TransportStructure VARCHAR(20),
    ProductID VARCHAR(11) NOT NULL,
    Price DECIMAL(10 , 2 ) NOT NULL,
    Currency VARCHAR(11) NOT NULL,
    NetTonnage DECIMAL(6 , 2 ) DEFAULT NULL,
    OrderDate DATE,
    RequiredDate DATE,
    LoadingDate	DATE,
    ArrivalDate DATE,
    LoadingAddress VARCHAR(60) NOT NULL,
    LoadingCity VARCHAR(15) NOT NULL,
    LoadingPostalCode VARCHAR(10) NOT NULL,
    LoadingRegionID VARCHAR(11) DEFAULT NULL,
    LoadingCountryID VARCHAR(2) NOT NULL,
    ShipAddress VARCHAR(60) NOT NULL,
    ShipCity VARCHAR(30) NOT NULL,
    ShipPostalCode VARCHAR(10) NOT NULL,
    ShipRegionID VARCHAR(11) DEFAULT NULL,
    ShipCountryID VARCHAR(11) NOT NULL,
    FOREIGN KEY (CustomerID)
        REFERENCES Customers (CustomerID),
    FOREIGN KEY (SupplierID)
        REFERENCES Suppliers (SupplierID),
	FOREIGN KEY (ShipperID)
        REFERENCES Shippers (ShipperID),
    FOREIGN KEY (EmployeeID)
        REFERENCES Employees (EmployeeID),
	FOREIGN KEY (ProductID)
        REFERENCES Products (ProductID)
)  ENGINE=INNODB;

-- Inserting data for table 'Orders'

LOAD DATA LOCAL INFILE 'D:/Back-end Developer PWN/Project01/orders.csv' 
INTO TABLE Orders
fields terminated by ','
lines terminated by '\r\n'
ignore 1 lines;


-- Trigger on 'Orders' and 'Employees' tables

/*
create trigger oCount
after insert on 
Orders 
for each row
update Employees set OrdersCount = OrdersCount + 1 where Employees.EmployeeID = new.EmployeeID;

create trigger back_oCount 
after delete on 
Orders
for each row
update Employees set OrdersCount = OrdersCount - 1 where mployees.EmployeeID = old.EmployeeID;

*/ 

#drop trigger oCount
#drop trigger back_oCount;

-- --------------------------------------------------------
-- --------------------------------------------------------

-- Showing tables content 

-- --------------------------------------------------------
-- --------------------------------------------------------

SHOW TABLES;

-- Showing tables content from table 'LoginToDatabase'
DESCRIBE LoginToDatabase;

SELECT 
    *
FROM
    LoginToDatabase;
    
SELECT 
	* 
FROM 
	LoginToDatabase 
WHERE 
    login='abc' 
AND 
    passwd= '123';
  
-- Showing tables content from table 'Countries'  
DESCRIBE Countries;
SELECT 
    *
FROM
    Countries;

-- Showing tables content from table 'Regions' 
DESCRIBE Regions;
SELECT 
    *
FROM
    Regions;
  
-- Showing tables content from table 'Departments' 
DESCRIBE Departments;
SELECT 
    *
FROM
    Departments;
  
-- Showing tables content from table 'Jobs' 
DESCRIBE Jobs;
SELECT 
    *
FROM
    Jobs;
  
-- Showing tables content from table 'Employees' 
DESCRIBE Employees;
SELECT 
    *
FROM
    Employees; 
  
-- Showing tables content from table 'Suppliers' 
DESCRIBE Suppliers;
SELECT 
    *
FROM
    Suppliers;
  
-- Showing tables content from table 'Categories' 
DESCRIBE Categories;
SELECT 
    *
FROM
    Categories;
  
-- Showing tables content from table 'Products' 
DESCRIBE Products;
SELECT 
    *
FROM
    Products;
  
-- Showing tables content from table 'Customers' 
DESCRIBE Customers;
SELECT 
    *
FROM
    Customers;
   
-- Showing tables content from table 'Shippers' 
DESCRIBE Shippers;
SELECT 
    *
FROM
    Shippers;
  
-- Showing tables content from table 'Orders' 
DESCRIBE Orders;
SELECT 
    *
FROM
    Orders;
    
-- --------------------------------------------------------
-- --------------------------------------------------------

-- Joined tables

-- --------------------------------------------------------
-- --------------------------------------------------------


-- Join tables 'Orders' and 'Products' - ordered by ArrivalDate descending
SELECT 
	o.*,
	p.*
FROM
	Orders AS o
LEFT JOIN
	Products AS p
ON (o.ProductID = p.ProductID)
ORDER BY o.ArrivalDate DESC;

-- Join tables 'Orders' and 'Suppliers' - ordered by SupplierID, ProductID, ArrivalDate descending
SELECT 
	o.*,
	s.*
FROM
	Orders AS o
LEFT JOIN
	Suppliers AS s
ON (o.SupplierID = s.SupplierID)
ORDER BY o.SupplierID, o.ProductID, o.ArrivalDate DESC;

-- Join tables 'Orders' and 'Shippers' - grouped by ModeOfTransport, ShipperID, ArrivalDate descending
SELECT 
	o.*,
	s.*
FROM
	Orders AS o
LEFT JOIN
	Shippers AS s
ON (o.ShipperID = s.ShipperID)
ORDER BY o.ModeOfTransport, o.ShipperID, o.ArrivalDate DESC;
 
-- Join tables 'Orders' and 'Employees' - ordered by EmployeeID, ArrivalDate descending
SELECT 
	o.*,
	e.*
FROM
	Orders AS o
LEFT JOIN
	Employees AS e
ON (o.EmployeeID = e.EmployeeID)
ORDER BY o.EmployeeID, o.ArrivalDate DESC;

-- --------------------------------------------------------
-- --------------------------------------------------------

-- Create views per mean of transport

-- --------------------------------------------------------
-- --------------------------------------------------------

-- A view that selects only road transports 
CREATE VIEW 
	orderRoad
AS SELECT
	*
FROM
	Orders
WHERE
	ModeOfTransport = 'road';
    
-- --------------------------------------------------------

-- A view that selects only rail transports 
CREATE VIEW 
	orderRail
AS SELECT
	*
FROM
	Orders
WHERE
	ModeOfTransport = 'rail';
    
-- --------------------------------------------------------

-- A view that selects only sea transports 
CREATE VIEW 
	orderSea
AS SELECT
	*
FROM
	Orders
WHERE
	ModeOfTransport = 'sea';   

-- --------------------------------------------------------
-- --------------------------------------------------------

-- Delete table content

-- --------------------------------------------------------
-- --------------------------------------------------------

#DELETE FROM LoginToDatabase;
#DELETE FROM Countries;
#DELETE FROM Regions;
#DELETE FROM Departments;
#DELETE FROM Jobs;
#DELETE FROM Employees;
#DELETE FROM Suppliers;
#DELETE FROM Categories;
#DELETE FROM Products;
#DELETE FROM Customers;
#DELETE FROM Shippers;
#DELETE FROM Orders;
  
-- --------------------------------------------------------
-- --------------------------------------------------------

-- Statistics

-- --------------------------------------------------------
-- --------------------------------------------------------

-- Select freight shipments
SELECT 
    LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID
FROM
    Orders
WHERE
    ModeOfTransport = 'sea'
GROUP BY ProductID, ModeOfTransport, LoadingCountryID
ORDER BY LoadingDate DESC;

-- --------------------------------------------------------

-- Select road shipments
SELECT 
    LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID
FROM
    Orders
WHERE
    ModeOfTransport = 'road'
GROUP BY ProductID, ModeOfTransport, LoadingCountryID
ORDER BY LoadingDate DESC;

-- --------------------------------------------------------

-- Select rail shipments
SELECT 
    LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID
FROM
    Orders
WHERE
    ModeOfTransport = 'rail'
GROUP BY ProductID, ModeOfTransport, LoadingCountryID
ORDER BY LoadingDate DESC;

-- --------------------------------------------------------

-- Total logistic cost per year, per country
SELECT 
    YEAR(LoadingDate) AS LoadingYear, LoadingCountryID, SUM(price) AS TotalCostsLoadingCountry
FROM
    Orders
GROUP BY LoadingYear, LoadingCountryID
ORDER BY LoadingYear DESC, TotalCostsLoadingCountry DESC;
 
-- --------------------------------------------------------

-- Total logistics cost per month, per country 
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, LoadingCountryID, SUM(Price) AS TotalCostsLoadingCountry
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, LoadingCountryID
ORDER BY LoadingYear DESC, LoadingMonth ASC, TotalCostsLoadingCountry DESC;
 
-- --------------------------------------------------------

-- Average price per ton in a month per 'ModeOfTransport'
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ModeOfTransport, Round(AVG(Price/NetTonnage),2) AS AveragePricePerTon
FROM
    Orders
GROUP BY LoadingYear DESC, LoadingMonth ASC, ModeOfTransport;

-- --------------------------------------------------------

-- Count of all orders per quarter per 'ModeOfTransport'
SELECT 
    YEAR(LoadingDate) AS LoadingYear,
    ELT(QUARTER(LoadingDate), 'I', 'II', 'III', 'IV') AS LoadingQuarter,
    ModeOfTransport,
    COUNT(*) AS OrdersCount
FROM
    Orders
GROUP BY LoadingYear DESC , LoadingQuarter ASC, ModeOfTransport; 

-- --------------------------------------------------------

-- Average price per ton of all orders per quarter per 'ModeOfTransport'
SELECT 
    YEAR(LoadingDate) AS LoadingYear,
    ELT(QUARTER(LoadingDate), 'I', 'II', 'III', 'IV') AS LoadingQuarter,
    ModeOfTransport,
    ROUND(AVG(Price/NetTonnage),2) AS AveragePricePerTon
FROM
    Orders
GROUP BY LoadingYear DESC , LoadingQuarter ASC, ModeOfTransport; 

-- --------------------------------------------------------

-- Total logistic cost per supplier per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, SupplierID, SUM(Price) AS TotalCosts
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, SupplierID
ORDER BY LoadingYear DESC, LoadingMonth ASC, SupplierID, TotalCosts;

-- --------------------------------------------------------

-- Sum of tons shipped per supplier per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, SupplierID, SUM(NetTonnage) AS TotalTonnage
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, SupplierID
ORDER BY LoadingYear DESC, LoadingMonth ASC, SupplierID, TotalTonnage;

-- --------------------------------------------------------

-- Average logistic cost per ton per supplier per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, SupplierID, ROUND(AVG(Price/NetTonnage),2) AS AverageCostsPerTon
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, SupplierID
ORDER BY LoadingYear DESC, LoadingMonth ASC, SupplierID, AverageCostsPerTon;

-- --------------------------------------------------------

-- Total logistic cost per customer per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, CustomerID, SUM(Price) AS TotalCosts
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, CustomerID
ORDER BY LoadingYear DESC, LoadingMonth ASC, CustomerID, TotalCosts;

-- --------------------------------------------------------

-- Sum of tons shipped per customer per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, CustomerID, SUM(NetTonnage) AS TotalTonnage
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, CustomerID
ORDER BY LoadingYear DESC, LoadingMonth ASC, CustomerID, TotalTonnage;

-- --------------------------------------------------------

-- Average logistic cost per ton per customer per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, CustomerID, ROUND(AVG(Price/NetTonnage),2) AS AverageCostsPerTon
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, CustomerID
ORDER BY LoadingYear DESC, LoadingMonth ASC, CustomerID, AverageCostsPerTon;

-- --------------------------------------------------------

-- Total logistic cost per shipper per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ShipperID, SUM(Price) AS TotalCosts
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, ShipperID
ORDER BY LoadingYear DESC, LoadingMonth ASC, ShipperID, TotalCosts;

-- --------------------------------------------------------

-- Sum of tones shipped per shipper per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ShipperID, SUM(NetTonnage) AS TotalTonnage
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, ShipperID
ORDER BY LoadingYear DESC, LoadingMonth ASC, ShipperID, TotalTonnage;

-- --------------------------------------------------------

-- Average logistic cost per ton per shipper per month
SELECT 
    YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ShipperID, ROUND(AVG(Price/NetTonnage),2) AS AverageCostsPerTon
FROM
    Orders
GROUP BY LoadingYear, LoadingMonth, ShipperID
ORDER BY LoadingYear DESC, LoadingMonth ASC, ShipperID, AverageCostsPerTon;
-- --------------------------------------------------------

-- Select shipments bigger than 100 tones
SELECT 
    LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID
FROM
    Orders
WHERE
    NetTonnage >= 100
ORDER BY LoadingDate DESC, OrderID ASC;

-- --------------------------------------------------------

-- Select shipments with cost higher than 100000
SELECT 
    LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID
FROM
    Orders
WHERE
    Price >= 100000
ORDER BY LoadingDate DESC, OrderID ASC;

-- --------------------------------------------------------

-- List of ten most expensive shipments

SELECT DISTINCT
    LoadingDate, OrderID AS MostExpensiveShipmentsID, ProductID, Price, NetTonnage, LoadingCountryID
FROM
    Orders AS a
WHERE
    10 >= (SELECT 
            COUNT(DISTINCT Price)
        FROM
            Orders AS b
        WHERE
            b.Price >= a.Price
            )
ORDER BY Price DESC;

-- SHOW VARIABLES LIKE 'secure_file_priv';
-- C:\ProgramData\MySQL\MySQL Server 5.7\my.ini
-- Change in the above file 'secure_file_priv=""'

-- Export MySQL data to Excel File

SET @TS = DATE_FORMAT(NOW(),'_%Y_%m_%d_%H_%i_%s');
 
SET @FOLDER = 'D:/Back-end Developer PWN/Project01/'; 
SET @PREFIX = 'orders';
SET @EXT    = '.csv';

SET @Command =  CONCAT("SELECT * FROM orders INTO OUTFILE '",@FOLDER,@PREFIX,@TS,@EXT,
    "' FIELDS ENCLOSED BY '\' TERMINATED BY ',' ESCAPED BY '\'",
    "  LINES TERMINATED BY '\r\n';");
    
PREPARE statement FROM @Command;

EXECUTE statement;



-- ((SELECT 'Order ID', '', '') UNION

/*
(SELECT 'Order Number','Order Date','Status')
UNION 
(SELECT orderNumber,orderDate, status
FROM orders
INTO OUTFILE 'C:/tmp/orders.csv'
FIELDS ENCLOSED BY '"' TERMINATED BY ';' ESCAPED BY '"'
LINES TERMINATED BY '\r\n');
*/

-- --------------------------------------------------------
-- --------------------------------------------------------