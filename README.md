# SQL Insert Statement Converter (SQL)
Python script that converts records in tables (eg: .xlsx tables) to SQL's INSERT statements.

## Introduction
In a Database class, the lecturer required us to convert records from 4 tables (.xlsx tables) to SQL INSERT statements. Instead of inserting the values manually and formatting it properly, I wrote a Python script that does the job.

_Here are the 4 tables:_
1. Item Table
![Item Table](https://github.com/TheCornelius/SQL-Insert-Statement-Converter/blob/master/Table_Images/ItemsTable.PNG)

2. Sales Table<br />
![Sales Table](/Table_Images/SalesTable.png)
3. Buyer Table
![Buyer Table](./Table_Images/BuyerTable.png)
4. Invoice Table
![Invoice Table](./Table_Images/InvoiceTable.png)

## What I Did
1) Copied the contents of the table and saved it as .txt files (File Names: Items.txt, Sales.txt, Buyer.txt, Invoice.txt). <br />
2) Used Python to read through the .txt files and produce the INSERT statements with appropriate formatting. The program will then output the INSERT statements respective of each table into new .txt files (File Names: ItemsTable.txt, SalesTable.txt, BuyerTable.txt, InvoiceTable.txt).

## User Manual
1) Download this repository as a zip file (or clone it). <br />
2) Run "SQL_InsertValue.py"
