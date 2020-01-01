# This is a program that generates SQL's CREATE TABLE commands from an .xlsx sheet which contains the Data Dictionary
# Input file is .xlsx format while output file is .txt format

import openpyxl
from openpyxl import Workbook
import os

# openpyxl stuff
wb = Workbook()
ws = wb.active  # Uses the active worksheet, by default it is 0


TableNames = ["Buyer"]
CreateTableStatement = "CREATE TABLE {}\n(\n{}\n);"
SQL_SelectStatement = r"SELECT * From {};"

outputFileName = "SQL_CreateTable.txt"
outputFile = open(fileName, 'w')

# os stuff
currentDirectory = os.getcwd()

for i in range(0, 4):
    outputFile.write(SQL_SelectStatement.format(TableNames[i]) + "\n")

outputFile.close()
