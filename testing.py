# This is a program that generates SQL's CREATE TABLE commands from an .xlsx sheet which contains the Data Dictionary
import openpyxl

TableNames = ["Buyer"]
CreateTableStatement = "CREATE TABLE {}\n(\n{}\n);"  # First field is table name while second field is the fields of the table, which is to be entered
SQL_SelectStatement = r"SELECT * From {};"
ExampleStatement = "facID char(3),\nfacName char(50)"
tableName = "Buyer"
print(CreateTableStatement.format(tableName, ExampleStatement) + '\n')
#
# outputFileName = "SQL_CreateTable.txt"
# outputFile = open(fileName, 'w')
#
#
# for i in range(0, 4):
#     outputFile.write("\n" + SQL_SelectStatement.format(TableNames[i]) + "\n")

# outputFile.close()
