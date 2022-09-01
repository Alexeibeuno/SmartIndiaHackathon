# Import of the mysql database connection model
import pymysql
# Data required to set a connection with a database
import SecretPass

import subprocess
import sys
import datetime
import csv

# --------------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------------

# Class to connect to a database
class TransportConnect:
    def __init__(self):
        try:
            self.conn = pymysql.connect(host = 'localhost', user = 'root', passwd = SecretPass.passwd, db ='Transport', charset ='utf8')
            print('Connection established')
            self.c = self.conn.cursor()
            self.dblogin()
            self.conn.close()
        except:
            print('Invalid login data')
# Login to a database using login and password
    def dblogin(self):
        login = input('Enter login: ')
        passwd = input('Enter password')
        #self.c = self.conn.cursor()
        self.c.execute('SELECT * FROM LoginToDatabase WHERE login=%s and passwd=%s', (login,passwd))
        logRes = self.c.fetchall()
        #print(logRes)
        if(len(logRes) == 1):
            print('Signed')
            self.menu()
        else:
            print('Invalid login information')
            self.dblogin

# --------------------------------------------------------
# MAIN MENU
# --------------------------------------------------------
    def menu(self):
        while (True):
            print('Please choose the information you are intrested in: ')
            dec = input('E - Exit the program\n ST - Simple tables\n MT - Merged tables\n SA - Statistics\n').upper()
            if (dec == 'ST'):
                self.simpletables()
            elif (dec == 'MT'):
                self.mergedtables()
            elif (dec == 'SA'):
                self.statistics()
            elif (dec == 'E'):
                print('You have left the program. Thank you.')
                break
            else:
                print('You have entered invalid data')
# --------------------------------------------------------
# SIMPLE TABLES MENU
# --------------------------------------------------------
    def simpletables(self):
        while (True):
            print('Please choose the table you are intrested in :')
            dec = input(
                'Q - go back to main menu\n CA - categories\n CN - countries\n CU - customers\n D - departments\n E - employees\n J - jobs\n O - orders\n P - products\n R- regions\n SH - shippers\n SU - suppliers\n').upper()
            if (dec == 'CA'):
                self.categories()
            elif (dec == 'CN'):
                self.countries()
            elif (dec == 'CU'):
                self.customers()
            elif (dec == 'D'):
                self.departments()
            elif (dec == 'E'):
                self.employees()
            elif (dec == 'J'):
                self.jobs()
            elif (dec == 'O'):
                self.orders()
            elif (dec == 'P'):
                self.products()
            elif (dec == 'R'):
                self.regions()
            elif (dec == 'SH'):
                self.shippers()
            elif (dec == 'SU'):
                self.suppliers()
            elif (dec == 'Q'):
                print('You went back to main menu')
                self.menu()
                break
            else:
                print('You have entered invalid data')

# 'Categories' table menu
    def categories(self):
        while (True):
            print('CATEGORIES - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n').upper()
            if (dec == 'S'):
                self.select_categories()
            elif (dec == 'I'):
                self.insert_categories()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Categories' table content
    def select_categories(self):
        self.c.execute('SELECT * FROM Categories')
        categor = self.c.fetchall()
        i = 1
        for row in categor:
            print('|%3i|%11s|%40s|%100s' % (i, row[0], row[1], row[2]))
            i += 1
        self.categories()

# Insert into 'Categories' table
    def insert_categories(self):
        print('Please enter the details of a new product category: ')
        try:
            categoryID = input('CategoryID: ')
            categoryName = input('CategoryName: ')
            description = input('Description: ')
            self.c.execute('INSERT INTO Categories (CategoryID, CategoryName, Description) VALUES (%s,%s,%s)',
                           (categoryID, categoryName, description))
            self.conn.commit()
            self.categories()

        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_categories()

# Export a .csv file from 'Categories'
    #def export_categories(self):


# 'Countries' table menu
    def countries(self):
        while (True):
            print('COUNTRIES - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n').upper()
            if (dec == 'S'):
                self.select_countries()
            elif (dec == 'I'):
                self.insert_countries()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Countries' table content
    def select_countries(self):
        self.c.execute('SELECT * FROM Countries')
        countr = self.c.fetchall()
        i = 1
        for row in countr:
            print('|%3i|%11s|%20s|%20s|%20s' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.countries()

# Insert into 'Countires' table
    def insert_countries(self):
        print('Please enter the details of a new country: ')
        try:
            countryID = input('CountryID: ')
            countryNameEN = input('CountryNameEN: ')
            countryNamePL = input('CountryNamePL: ')
            countryNameLocal = input('CountryNameLocal: ')
            self.c.execute(
                'INSERT INTO Countries (CountryID, CountryNameEN, CountryNamePL, CountryNameLocal) VALUES (%s,%s,%s,%s)',
                (countryID, countryNameEN, countryNamePL, countryNameLocal))
            self.conn.commit()
            self.countries()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_countries()

# 'Customers' table menu
    def customers(self):
        while (True):
            print('CUSTOMERS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n').upper()
            if (dec == 'S'):
                self.select_customers()
            elif (dec == 'I'):
                self.insert_customers()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Customers' table content
    def select_customers(self):
        self.c.execute('SELECT * FROM Customers')
        custom = self.c.fetchall()
        i = 1
        for row in custom:
            print('|%3i|%11s|%40s|%40s|%30s|%60s|%15s|%10s|%11s|%11s|%12s|%12s' % (
            i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            i += 1
        self.customers()

# Insert into 'Customers' table
    def insert_customers(self):
        print('Please enter the details of a new customer: ')
        try:
            customerID = input('CustomerID: ')
            companyName = input('CompanyName: ')
            contactName = input('ContactName: ')
            contactTitle = input('ContactTitle: ')
            address = input('Address: ')
            city = input('City: ')
            postalCode = input('PostalCode: ')
            regionID = input('RegionID: ')
            countryID = input('CountryID: ')
            mobilePnone = input('MobilePnone: ')
            deskPhone = input('DeskPhone: ')
            self.c.execute(
                'INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, PostalCode, RegionID, CountryID, MobilePnone, DeskPhone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (customerID, companyName, contactName, contactTitle, address, city, postalCode, regionID, countryID, mobilePnone, deskPhone))
            self.conn.commit()
            self.customers()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_customers()

# 'Departments' table menu
    def departments(self):
        while (True):
            print('DEPARTMENTS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n').upper()
            if (dec == 'S'):
                self.select_departments()
            elif (dec == 'I'):
                self.insert_departments()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Departments' table content
    def select_departments(self):
        self.c.execute('SELECT * FROM Departments')
        departm = self.c.fetchall()
        i = 1
        for row in departm:
            print('|%3i|%11s|%30s|%11s' % (i, row[0], row[1], row[2]))
            i += 1
        self.departments()

# Insert into 'Departments' table
    def insert_departments(self):
        print('Please enter the details of a new department: ')
        try:
            departmentID = input('DepartmentID: ')
            departmentName = input('DepartmentName: ')
            managerID = input('ManagerID: ')
            self.c.execute('INSERT INTO Departments (DepartmentID, DepartmentName, ManagerID) VALUES (%s,%s,%s)',
                           (departmentID, departmentName, managerID))
            self.conn.commit()
            self.departments()

        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_departments()

# 'Employees' table menu
    def employees(self):
        while (True):
            print('EMPLOYEES - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n D - delete').upper()
            if (dec == 'S'):
                self.select_employees()
            elif (dec == 'I'):
                self.insert_employees()
            elif (dec == 'D'):
                self.delete_employees()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Employees' table content
    def select_employees(self):
        self.c.execute('SELECT * FROM Employees')
        employ = self.c.fetchall()
        i = 1
        for row in employ:
            print(
                '|%3i|%6s|%20s|%25s|%11s|%6s|%30s|%25s|%10s|%10s|%60s|%15s|%10s|%11s|%11s|%12s|%12s|%11s|%11s|%11s|%7.2f|%100s' % (
                i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20]))
            i += 1
        self.employees()

# Insert into 'Employees' table
    def insert_employees(self):
        print('Please enter the details of a new employee: ')
        try:
            employeeID = input('EmployeeID: ')
            firstName = input('FirstName: ')
            lastName = input('LastName: ')
            pesel = input('PESEL: ')
            gender = input('Gender: ')
            title = input('Title: ')
            titleOfCourtesy = input('TitleOfCourtesy: ')
            birthDate = input('BirthDate: ')
            hireDate = input('HireDate: ')
            address = input('Address: ')
            city = input('City: ')
            postalCode = input('PostalCode: ')
            regionID = input('RegionID: ')
            countryID = input('CountryID: ')
            mobilePhone = input('MobilePhone: ')
            homePhone = input('HomePhone: ')
            managerID = input('ManagerID: ')
            departmentID = input('DepartmentID: ')
            jobID = input('JobID: ')
            salary = input('Salary: ')
            notes = input('Notes: ')
            self.c.execute(
                'INSERT INTO Employees (EmployeeID, FirstName, LastName, PESEL, Gender, Title, TitleOfCourtesy, BirthDate, HireDate, Address, City, PostalCode, RegionID, CountryID, MobilePhone, HomePhone, ManagerID, DepartmentID, JobID, Salary, Notes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%7.2f,%s)',
                (employeeID, firstName, lastName, pesel, gender, title, titleOfCourtesy, birthDate, hireDate, address, city,
                 postalCode, regionID, countryID, mobilePhone, homePhone, managerID, departmentID, jobID, salary, notes))
            self.conn.commit()
            self.employees()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_employees()

# Delete from 'Employees' table
    def delete_employees(self):
        self.select_employees()
        print('Please enter PESEL of an employee you want to delete or Q - go back to Employees menu')
        pesel = input('PESEL = ').upper()
        self.c.execute('DELETE FROM Employees WHERE pesel =%s', pesel)
        dec = input('Are you sure you want to delete a record? Y/N').upper()
        if (dec == 'Y'):
            self.conn.commit()
            print('Record deleted')
        elif (dec == 'Q'):
            print('You went back to Employees menu')
            self.employees()
        else:
            self.conn.rollback()
            print('Back in the delete menu')

# 'Jobs' table menu
    def jobs(self):
        while (True):
            print('JOBS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n').upper()
            if (dec == 'S'):
                self.select_jobs()
            elif (dec == 'I'):
                self.insert_jobs()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Jobs' table content
    def select_jobs(self):
        self.c.execute('SELECT * FROM Jobs')
        job = self.c.fetchall()
        i = 1
        for row in job:
            print('|%3i|%11s|%35s|%7.2f|%7.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.jobs()

# Insert into 'Jobs' table
    def insert_jobs(self):
        print('Please enter the details of a new job: ')
        try:
            jobID = input('JobID: ')
            jobTitle = input('JobTitle: ')
            minSalary = input('MinSalary: ')
            maxSalary = input('MaxSalary: ')
            self.c.execute('INSERT INTO Jobs (JobID, JobTitle, MinSalary, MaxSalary) VALUES (%s,%s,%7.2f,%7.2f)',
                           (jobID, jobTitle, minSalary,maxSalary))
            self.conn.commit()
            self.jobs()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_jobs()

# 'Orders' table menu
    def orders(self):
        while (True):
            print('ORDERS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert\n D - delete').upper()
            if (dec == 'S'):
                self.select_orders()
            elif (dec == 'I'):
                self.insert_orders()
            elif (dec == 'D'):
                self.delete_orders()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Orders' table content
    def select_orders(self):
        self.c.execute('SELECT * FROM Orders')
        ord = self.c.fetchall()
        i = 1
        for row in ord:
            print(
                '|%3i|%11i|%11s|%11s|%3i|%6s|%20s|%20s|%11s|%10.2f|%11s|%6.2f|%10s|%10s|%10s|%10s|%60s|%15s|%10s|%11s|%2s|%60s|%30s|%10s|%11s|%11s' % (
                i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24]))
            i += 1
        self.orders()
        self.orders()

# Insert into 'Orders' table
    def insert_orders(self):
        print('Please enter the details of a new order: ')
        try:
            orderID = input('OrderID: ')
            customerID = input('CustomerID: ')
            supplierID = input('SupplierID: ')
            shipperID = input('ShipperID: ')
            employeeID = input('EmployeeID: ')
            modeOfTransport = input('ModeOfTransport: ')
            transportStructure = input('TransportStructure: ')
            productID = input('ProductID: ')
            price = input('Price: ')
            currency = input('Currency: ')
            netTonnage = input('NetTonnage: ')
            orderDate = input('OrderDate: ')
            requiredDATE = input('RequiredDATE: ')
            loadingDate = input('LoadingDate: ')
            arrivalDate = input('ArrivalDate: ')
            loadingAddress = input('LoadingAddress: ')
            loadingCity = input('LoadingCity: ')
            loadingPostalCode = input('LoadingPostalCode: ')
            loadingRegionID = input('LoadingRegionID: ')
            loadingCountryID = input('JobID: ')
            shipAddress = input('ShipAddress: ')
            shipCity = input('ShipCity: ')
            shipPostalCode = input('ShipPostalCode: ')
            shipRegionID = input('ShipRegionID: ')
            shipCountryID = input('NotesShipCountryID: ')
            self.c.execute(
                'INSERT INTO Orders (OrderID, CustomerID, SupplierID, ShipperID, EmployeeID, ModeOfTransport, TransportStructure, ProductID, Price, Currency, NetTonnage, OrderDate, RequiredDATE, LoadingDate, ArrivalDate, LoadingAddress, LoadingCity, LoadingPostalCode, LoadingRegionID, LoadingCountryID, ShipAddress, ShipCity, ShipPostalCode, ShipRegionID, ShipCountryID) VALUES (%i,%s,%s,%i,%s,%s,%s,%s,%f,%s,%f,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (orderID, customerID, supplierID, shipperID, employeeID, modeOfTransport, transportStructure, productID, price, currency,
                 netTonnage, orderDate, requiredDATE, loadingDate, arrivalDate, loadingAddress, loadingCity, loadingPostalCode,
                 loadingRegionID, loadingCountryID, shipAddress, shipCity, shipPostalCode, shipRegionID, shipCountryID))
            self.conn.commit()
            self.orders()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_orders()

# Delete from 'Orders' table
    def delete_orders(self):
        self.select_orders()
        print('Please enter orderID of an order you want to delete or Q - go back to Orders menu')
        orderid = input('orderID = ')
        self.c.execute('DELETE FROM Orders WHERE OrderID =%i', orderid)
        dec = input('Are you sure you want to delete a record? Y/N').upper()
        if (dec == 'Y'):
            self.conn.commit()
            print('Record deleted')
        elif (dec == 'Q'):
            print('You went back to Orders menu')
            self.orders()
        else:
            self.conn.rollback()
            print('Back in the delete menu')

# 'Products' table menu
    def products(self):
        while (True):
            print('PRODUCTS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert').upper()
            if (dec == 'S'):
                self.select_products()
            elif (dec == 'I'):
                self.insert_products()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Products' table content
    def select_products(self):
        self.c.execute('SELECT * FROM Products')
        prod = self.c.fetchall()
        i = 1
        for row in prod:
            print('|%3i|%11s|%40s|%11s|%11s' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.products()

# Insert into 'Products' table
    def insert_products(self):
        print('Please enter the details of a new product: ')
        try:
            productID = input('ProductID: ')
            productName = input('ProductName: ')
            supplierID = input('SupplierID: ')
            categoryID = input('CategoryID: ')
            self.c.execute('INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID) VALUES (%s,%s,%s,%s)',
                           (productID, productName, supplierID, categoryID))
            self.conn.commit()
            self.products()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_products()

# 'Regions' table menu
    def regions(self):
        while (True):
            print('REGIONS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert D - delete').upper()
            if (dec == 'S'):
                self.select_regions()
            elif (dec == 'I'):
                self.insert_regions()
            elif (dec == 'D'):
                self.delete_regions()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Regions' table content
    def select_regions(self):
        self.c.execute('SELECT * FROM Regions')
        reg = self.c.fetchall()
        i = 1
        for row in reg:
            print('|%3i|%11s|%50s|%50s|%20s|%20s|%11s' % (i, row[0], row[1], row[2], row[3], row[4], row[5]))
            i += 1
        self.regions()

# Insert into 'Regions' table
    def insert_regions(self):
        print('Please enter the details of a new region: ')
        try:
            regionID = input('RegionID: ')
            regionNameEN = input('RegionNameEN: ')
            regionNameLocal = input('RegionNameLocal: ')
            regionTypeEN = input('RegionTypeEN: ')
            regionTypeLocal = input('RegionTypeLocal: ')
            countryID = input('CountryID: ')
            self.c.execute(
                'INSERT INTO Regions (RegionID, RegionNameEN, RegionNameLocal, RegionTypeEN, RegionTypeLocal, CountryID) VALUES (%s,%s,%s,%s,%s,%s)',
                (regionID, regionNameEN, regionNameLocal, regionTypeEN, regionTypeLocal, countryID))
            self.conn.commit()
            self.regions()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_regions()

# Delete from 'Regions' table
    def delete_regions(self):
        self.select_regions()
        print('Please enter regionID of a region you want to delete or Q - go back to Regions menu')
        regionid = input('RegionID = ')
        self.c.execute('DELETE FROM Regions WHERE RegionID =%i', regionid)
        dec = input('Are you sure you want to delete a record? Y/N').upper()
        if (dec == 'Y'):
            self.conn.commit()
            print('Record deleted')
        elif (dec == 'Q'):
            print('You went back to Regions menu')
            self.regions()
        else:
            self.conn.rollback()
            print('Back in the delete menu')

# 'Shippers' table menu
    def shippers(self):
        while (True):
            print('SHIPPERS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert').upper()
            if (dec == 'S'):
                self.select_shippers()
            elif (dec == 'I'):
                self.insert_shippers()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Shippers' table content
    def select_shippers(self):
        self.c.execute('SELECT * FROM Shippers')
        shipp = self.c.fetchall()
        i = 1
        for row in shipp:
            print('|%3i|%3i|%40s|%40s|%30s|%60s|%15s|%10s|%11s|%11s|%12s|%12s' % (
            i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            i += 1

# Insert into Shippers table
    def insert_shippers(self):
        print('Please enter the details of a new shipper: ')
        try:
            shipperID = input('ShipperID: ')
            companyName = input('CompanyName: ')
            contactName = input('ContactName: ')
            contactTitle = input('ContactTitle: ')
            address = input('Address: ')
            city = input('City: ')
            postalCode = input('PostalCode: ')
            regionID = input('RegionID: ')
            countryID = input('CountryID: ')
            mobilePhone = input('MobilePhone: ')
            deskPhone = input('DeskPhone: ')
            self.c.execute(
                'INSERT INTO Shippers (ShipperID, CompanyName, ContactName, ContactTitle, Address, City, PostalCode, RegionID, CountryID, MobilePhone, DeskPhone) VALUES (%i,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (shipperID, companyName, contactName, contactTitle, address, city, postalCode, regionID, countryID, mobilePhone, deskPhone))
            self.conn.commit()
            self.shippers()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_shippers()

# 'Suppliers' table menu
    def suppliers(self):
        while (True):
            print('SUPPLIERS - Please choose what you want to do:')
            dec = input('Q - go back to simple tables menu\n S - show\n I - insert').upper()
            if (dec == 'S'):
                self.select_suppliers()
            elif (dec == 'I'):
                self.insert_suppliers()
            elif (dec == 'Q'):
                print('You went back to simple tables menu')
                self.simpletables()
                break
            else:
                print('You have entered invalid data')

# Show 'Suppliers' table content
    def select_suppliers(self):
        self.c.execute('SELECT * FROM Suppliers')
        supp = self.c.fetchall()
        i = 1
        for row in supp:
            print('|%3i|%11s|%40s|%40s|%30s|%60s|%15s|%10s|%11s|%11s|%12s' % (
                i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            i += 1
        self.suppliers()

# Insert into 'Suppliers' table
    def insert_suppliers(self):
        print('Please enter the details of a new supplier: ')
        try:
            supplierID = input('SupplierID: ')
            companyName = input('CompanyName: ')
            contactName = input('ContactName: ')
            contactTitle = input('ContactTitle: ')
            address = input('Address: ')
            city = input('City: ')
            postalCode = input('PostalCode: ')
            regionID = input('RegionID: ')
            countryID = input('CountryID: ')
            phone = input('Phone: ')
            self.c.execute(
                'INSERT INTO Suppliers(SupplierID, CompanyName, ContactName, ContactTitle, Address, City, PostalCode, RegionID, CountryID, Phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                (supplierID, companyName, contactName, contactTitle, address, city, postalCode, regionID, countryID, phone))
            self.conn.commit()
        except:
            print("Oops!  That was no valid data. Try again...")
            self.insert_suppliers()
# --------------------------------------------------------
# MERGED TABLES
# --------------------------------------------------------
    def mergedtables(self):
        while (True):
            print('MERGED TABLES - Please choose what you want to do:')
            dec = input('Q - go back to main menu\n A - Orders & Products\n B - Orders & Suppliers\n C - Orders & Shippers\n D - Orders & Employees').upper()
            if (dec == 'A'):
                self.join1()
            elif (dec == 'B'):
                self.join2()
            elif (dec == 'C'):
                self.join3()
            elif (dec == 'D'):
                self.join4()
            elif (dec == 'Q'):
                print('You went back to main menu')
                self.menu()
                break
            else:
                print('You have entered invalid data')

# Join tables Orders & Products
    def join1(self):
        self.c.execute('SELECT o.*,	p.* FROM Orders AS o LEFT JOIN Products AS p ON (o.ProductID = p.ProductID) ORDER BY o.ArrivalDate DESC;')
        ordersProducts = self.c.fetchall()
        i = 1
        for row in ordersProducts:
            print(
                 '|%3i|%11i|%11s|%11s|%3i|%6s|%20s|%20s|%11s|%10.2f|%11s|%6.2f|%10s|%10s|%10s|%10s|%60s|%30s|%10s|%11s|%2s|%60s|%15s|%10s|%11s|%11s|%11s|%40s|%11s|%11s' % (
                i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
                 row[25],row[26],row[27]))
            i += 1
        self.mergedtables()

# Join tables Orders & Suppliers
    def join2(self):
        self.c.execute(
            'SELECT o.*, s.* FROM Orders AS o LEFT JOIN Suppliers AS s ON (o.SupplierID = s.SupplierID) ORDER BY o.SupplierID, o.ProductID, o.ArrivalDate DESC;')
        ordersSuppliers = self.c.fetchall()
        i = 1
        for row in ordersSuppliers:
            print(
                '|%3i|%11i|%11s|%11s|%3i|%6s|%20s|%20s|%11s|%10.2f|%11s|%6.2f|%10s|%10s|%10s|%10s|%60s|%15s|%10s|%11s|%2s|%60s|%30s|%10s|%11s|%11s|%11s|%40s|%40s|%30s|%60s|%15s|%10s|%11s|%11s|%12s' % (
                    i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                    row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
                    row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33]))
            i += 1
        self.mergedtables()

# Join tables Orders & Shippers
    def join3(self):
        self.c.execute(
            'SELECT o.*, s.* FROM Orders AS o LEFT JOIN Shippers AS s ON (o.ShipperID = s.ShipperID) ORDER BY o.ModeOfTransport, o.ShipperID, o.ArrivalDate DESC;')
        ordersShippers = self.c.fetchall()
        i = 1
        for row in ordersShippers:
            print(
                '|%3i|%11i|%11s|%11s|%3i|%6s|%20s|%20s|%11s|%10.2f|%11s|%6.2f|%10s|%10s|%10s|%10s|%60s|%15s|%10s|%11s|%2s|%60s|%30s|%10s|%11s|%11s|%3i|%40s|%40s|%30s|%60s|%15s|%10s|%11s|%11s|%12s|%12s' % (
                    i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13],
                     row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25],
                    row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35]
                    ))
            i += 1
        self.mergedtables()

# Join tables Orders & Employees
    def join4(self):
        self.c.execute(
            'SELECT o.*, e.* FROM Orders AS o LEFT JOIN Employees AS e ON (o.EmployeeID = e.EmployeeID) ORDER BY o.EmployeeID, o.ArrivalDate DESC;')
        ordersEmployees = self.c.fetchall()
        i = 1
        for row in ordersEmployees:
            print(
                '|%3i|%11i|%11s|%11s|%3i|%6s|%20s|%20s|%11s|%10.2f|%11s|%6.2f|%10s|%10s|%10s|%10s|%60s|%15s|%10s|%11s|%2s|%60s|%30s|%10s|%11s|%11s|%6s|%20s|%25s|%11s|%6s|%30s|%25s|%10s|%10s|%60s|%15s|%10s|%11s|%11s|%12s|%12s|%11s|%11s|%11s|%7.2f|%255s' % (
                    i, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12],
                    row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                    row[23], row[24], row[25],
                    row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37],
                    row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45]
                   ))
            i += 1
        self.mergedtables()

# --------------------------------------------------------
# STATISTICS
# --------------------------------------------------------
    def statistics(self):
        while (True):
            print('STATISTICS - Please choose what you want to do:')
            dec = input('Q - go back to main menu\n \
            1 - Select freight shipments\n \
            2 - Select road shipments\n \
            3 - Select rail shipments\n \
            4 - Total logistic cost per year, per country\n \
            5 - Total logistics cost per month, per country\n \
            6 - Average price per ton in a month per ModeOfTransport\n \
            7 - Count of all orders per quarter per ModeOfTransport\n \
            8 - Average price per ton of all orders per quarter per ModeOfTransport\n \
            9 - Total logistic cost per supplier per month\n \
            10 - Sum of tons shipped per supplier per month\n \
            11 - Average logistic cost per ton per supplier per month\n \
            12 - Total logistic cost per customer per month\n \
            13 - Sum of tones shipped per customer per month\n \
            14 - Average logistic cost per ton per customer per month\n \
            15 - Total logistic cost per shipper per month\n \
            16 - Sum of tons shipped per shipper per month\n \
            17 - Average logistic cost per ton per shipper per month\n \
            18 - Select shipments bigger than 100 tones\n \
            19 - Select shipments with cost higher than 100000\n \
            20 - List of ten most expensive shipments\
            ').upper()
            if (dec == '1'):
                self.stat1()
            elif (dec == '2'):
                self.stat2()
            elif (dec == '3'):
                self.stat3()
            elif (dec == '4'):
                self.stat4()
            elif (dec == '5'):
                self.stat5()
            elif (dec == '6'):
                self.stat6()
            elif (dec == '7'):
                self.stat7()
            elif (dec == '8'):
                self.stat8()
            elif (dec == '9'):
                self.stat9()
            elif (dec == '10'):
                self.stat10()
            elif (dec == '11'):
                self.stat11()
            elif (dec == '12'):
                self.stat12()
            elif (dec == '13'):
                self.stat13()
            elif (dec == '14'):
                self.stat14()
            elif (dec == '15'):
                self.stat15()
            elif (dec == '16'):
                self.stat16()
            elif (dec == '17'):
                self.stat17()
            elif (dec == '18'):
                self.stat18()
            elif (dec == '19'):
                self.stat19()
            elif (dec == '20'):
                self.stat20()
            elif (dec == 'Q'):
                print('You went back to main menu')
                self.menu()
                break
            else:
                print('You have entered invalid data')

# Select freight shipments
    def stat1(self):
        print('Freight shipments')
        self.c.execute('SELECT LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID FROM Orders WHERE ModeOfTransport = "sea" GROUP BY ProductID, ModeOfTransport, LoadingCountryID ORDER BY LoadingDate DESC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%11i|%11s|%20s|%10.2f|%6.2f|%2s' % (i, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
        self.statistics()

# Select road shipments
    def stat2(self):
        print('Road shipments')
        self.c.execute('SELECT LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID FROM Orders WHERE ModeOfTransport = "sea" GROUP BY ProductID, ModeOfTransport, LoadingCountryID ORDER BY LoadingDate DESC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%11i|%11s|%20s|%10.2f|%6.2f|%2s' % (i, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
        self.statistics()

# Select rail shipments
    def stat3(self):
        print('Rail shipments')
        self.c.execute('SELECT LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID FROM Orders WHERE ModeOfTransport = "rail" GROUP BY ProductID, ModeOfTransport, LoadingCountryID ORDER BY LoadingDate DESC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%11i|%11s|%20s|%10.2f|%6.2f|%2s' % (i, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
        self.statistics()

# Total logistic cost per year, per country
    def stat4(self):
        print('Total logistic cost per year, per country')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, LoadingCountryID, SUM(price) AS TotalCostsLoadingCountry FROM Orders GROUP BY LoadingYear, LoadingCountryID ORDER BY LoadingYear DESC, TotalCostsLoadingCountry DESC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%2s|%10.2f' % (
            i, row[0], row[1], row[2]))
            i += 1
        self.statistics()

# Total logistics cost per month, per country
    def stat5(self):
        print('Total logistics cost per month, per country')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, LoadingCountryID, SUM(Price) AS TotalCostsLoadingCountry FROM Orders GROUP BY LoadingYear, LoadingMonth, LoadingCountryID ORDER BY LoadingYear DESC, LoadingMonth ASC, TotalCostsLoadingCountry DESC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%2s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Average price per ton in a month per ModeOfTransport
    def stat6(self):
        print('Average price per ton in a month per ModeOfTransport')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ModeOfTransport, Round(AVG(Price/NetTonnage),2) AS AveragePricePerTon FROM Orders GROUP BY LoadingYear DESC, LoadingMonth ASC, ModeOfTransport;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%20s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Count of all orders per quarter per ModeOfTransport
    def stat7(self):
        print('Count of all orders per quarter per ModeOfTransport')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, ELT(QUARTER(LoadingDate), "I", "II", "III", "IV") AS LoadingQuarter, ModeOfTransport, COUNT(*) AS OrdersCount FROM Orders GROUP BY LoadingYear DESC, LoadingQuarter ASC, ModeOfTransport;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%20s|%20i' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Average price per ton of all orders per quarter per ModeOfTransport
    def stat8(self):
        print('Average price per ton of all orders per quarter per ModeOfTransport')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, ELT(QUARTER(LoadingDate), "I", "II", "III", "IV") AS LoadingQuarter, ModeOfTransport, ROUND(AVG(Price/NetTonnage),2) AS AveragePricePerTon FROM Orders GROUP BY LoadingYear DESC , LoadingQuarter ASC, ModeOfTransport;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%20s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Total logistic cost per supplier per month
    def stat9(self):
        print('Total logistic cost per supplier per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, SupplierID, SUM(Price) AS TotalCosts FROM Orders GROUP BY LoadingYear, LoadingMonth, SupplierID ORDER BY LoadingYear DESC, LoadingMonth ASC, SupplierID, TotalCosts;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%11s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Sum of tons shipped per supplier per month
    def stat10(self):
        print('Sum of tons shipped per supplier per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, SupplierID, SUM(NetTonnage) AS TotalTonnage FROM Orders GROUP BY LoadingYear, LoadingMonth, SupplierID ORDER BY LoadingYear DESC, LoadingMonth ASC, SupplierID, TotalTonnage;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%11s|%6.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Average logistic cost per ton per supplier per month
    def stat11(self):
        print('Average logistic cost per ton per supplier per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, SupplierID, ROUND(AVG(Price/NetTonnage),2) AS AverageCostsPerTon FROM Orders GROUP BY LoadingYear, LoadingMonth, SupplierID ORDER BY LoadingYear DESC, LoadingMonth ASC, SupplierID, AverageCostsPerTon;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%11s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Total logistic cost per customer per month
    def stat12(self):
        print('Total logistic cost per customer per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, CustomerID, SUM(Price) AS TotalCosts FROM Orders GROUP BY LoadingYear, LoadingMonth, CustomerID ORDER BY LoadingYear DESC, LoadingMonth ASC, CustomerID, TotalCosts;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%11s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Sum of tones shipped per customer per month
    def stat13(self):
        print('Sum of tones shipped per customer per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, CustomerID, SUM(NetTonnage) AS TotalTonnage FROM Orders GROUP BY LoadingYear, LoadingMonth, CustomerID ORDER BY LoadingYear DESC, LoadingMonth ASC, CustomerID, TotalTonnage;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%11s|%6.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Average logistic cost per ton per customer per month
    def stat14(self):
        print('Average logistic cost per ton per customer per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, CustomerID, ROUND(AVG(Price/NetTonnage),2) AS AverageCostsPerTon FROM Orders GROUP BY LoadingYear, LoadingMonth, CustomerID ORDER BY LoadingYear DESC, LoadingMonth ASC, CustomerID, AverageCostsPerTon;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%11s|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Total logistic cost per shipper per month
    def stat15(self):
        print('Total logistic cost per shipper per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ShipperID, SUM(Price) AS TotalCosts FROM Orders GROUP BY LoadingYear, LoadingMonth, ShipperID ORDER BY LoadingYear DESC, LoadingMonth ASC, ShipperID, TotalCosts;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%3i|%10.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Sum of tons shipped per shipper per month
    def stat16(self):
        print('Sum of tons shipped per shipper per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ShipperID, SUM(NetTonnage) AS TotalTonnage FROM Orders GROUP BY LoadingYear, LoadingMonth, ShipperID ORDER BY LoadingYear DESC, LoadingMonth ASC, ShipperID, TotalTonnage;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%3i|%6.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Average logistic cost per ton per shipper per month
    def stat17(self):
        print('Average logistic cost per ton per shipper per month')
        self.c.execute('SELECT YEAR(LoadingDate) AS LoadingYear, MONTH(LoadingDate) AS LoadingMonth, ShipperID, ROUND(AVG(Price/NetTonnage),2) AS AverageCostsPerTon FROM Orders GROUP BY LoadingYear, LoadingMonth, ShipperID ORDER BY LoadingYear DESC, LoadingMonth ASC, ShipperID, AverageCostsPerTon;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%4s|%2s|%3i|%6.2f' % (i, row[0], row[1], row[2], row[3]))
            i += 1
        self.statistics()

# Select shipments bigger than 100 tones
    def stat18(self):
        print('Select shipments bigger than 100 tones')
        self.c.execute('SELECT LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID FROM Orders WHERE NetTonnage >= 100 ORDER BY LoadingDate DESC, OrderID ASC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%11i|%11s|%20s|%10.2f|%6.2f|%2s' % (i, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
        self.statistics()

# Select shipments with cost higher than 100000
    def stat19(self):
        print('Select shipments with cost higher than 100000')
        self.c.execute('SELECT LoadingDate, OrderID, ProductID, ModeOfTransport, Price, NetTonnage, LoadingCountryID FROM Orders WHERE Price >= 100000 ORDER BY LoadingDate DESC, OrderID ASC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%11i|%11s|%20s|%10.2f|%6.2f|%2s' % (i, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            i += 1
        self.statistics()

# List of ten most expensive shipments
    def stat20(self):
        print('List of ten most expensive shipments')
        self.c.execute('SELECT DISTINCT LoadingDate, OrderID AS MostExpensiveShipmentsID, ProductID, Price, NetTonnage, LoadingCountryID FROM Orders AS a WHERE 10 >= (SELECT COUNT(DISTINCT Price) FROM Orders AS b WHERE b.Price >= a.Price) ORDER BY Price DESC;')
        tbl = self.c.fetchall()
        i = 1
        for row in tbl:
            print('|%3i|%10s|%11i|%20s|%10.2f|%6.2f|%2s' % (i, row[0], row[1], row[2], row[3], row[4], row[5]))
            i += 1
        self.statistics()

o = TransportConnect()


