# This is a program that generates SQL's CREATE TABLE commands from an .xlsx sheet which contains the Data Dictionary
import openpyxl

TableNames = ["Buyer"]
SQL_SelectStatement = r"SELECT * From {};"

outputFileName = "SQL_CreateTable.txt"
outputFile = open(fileName, 'w')


for i in range(0, 4):
    outputFile.write("\n" + SQL_SelectStatement.format(TableNames[i]) + "\n")

outputFile.close()
