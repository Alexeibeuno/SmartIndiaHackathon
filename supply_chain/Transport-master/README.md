# Transport

A project using MySQL and Python to facilitate the work regarding transports in a logistics department.

There are diffrent levels of access: for admin, user and manager.
The MySQL project includes the following tables: LoginToDatabase, Countries, Regions, Departments, Jobs, Employees, Suppliers, Categories,  Products, Customers, Shippers, Orders.

In Python user can choose to display and insert records to simple tables. For choosen tables a deletion of records is possible.
The user can also choose to display merged tables and statistics run on preselected tables, such as:

1.	Select freight shipments
2.	Select road shipments
3.	Select rail shipments
4.	Total logistic cost per year, per country
5.	Total logistics cost per month, per country 
6.	Average price per ton in a month per 'ModeOfTransport'
7.	Count of all orders per quarter per 'ModeOfTransport'
8.	Average price per ton of all orders per quarter per 'ModeOfTransport'
9.	Total logistic cost per supplier per month
10.	Sum of tones shipped per supplier per month
11.	Average logistic cost per ton per supplier per month
12.	Total logistic cost per customer per month
13.	Sum of tones shipped per customer per month
14.	Average logistic cost per ton per customer per month
15.	Total logistic cost per shipper per month
16.	Sum of tones shipped per shipper per month
17.	Average logistic cost per ton per shipper per month
18.	Select shipments bigger than 100 tones
19.	Select shipments with cost higher than 100000
20.	List of ten most expensive shipments