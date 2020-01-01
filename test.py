# This is a program that generates SQL's CREATE TABLE commands from an .xlsx sheet which contains the Data Dictionary
# Input file is .xlsx format while output file is .txt format

import openpyxl
from openpyxl import Workbook
import os
import os.path

# From previous testing.py stuff
TableNames = ["Buyer"]
CreateTableStatement = "CREATE TABLE {}\n(\n{}\n);"  # First field is table name while second field is the fields of the table, which is to be entered
SQL_SelectStatement = r"SELECT * From {};"
ExampleStatement = "facID char(3),\nfacName char(50)"
subStatement = ""
tableName = "Buyer"
print(CreateTableStatement.format(tableName, ExampleStatement) + '\n')


# openpyxl stuff
currentDirectory = os.getcwd()
print(currentDirectory)
os.chdir(os.path.join(currentDirectory, 'SQL-Create-Table-Command-Converter'))
wb = openpyxl.load_workbook('Sample Data.xlsx')
ws = wb.active  # Uses the active worksheet, by default it is 0


# Last row with valid records
lastRow = ws.max_row - 1
print(lastRow)  # max_row indicates the first row which is empty

# First row is row no: 2
for row in list(range(2, lastRow + 1)):
    for col in list(range(1, 12)):  # Columns: A to K
        pass

wb.close()
