# This program was written during Lab 6 of Database Fundamentals - to convert the records of different tables inside the tutorial document to SQL INSERT commands
# Variables in this program are in the global scope, which will be accessed from the different functions that are defined

# These lists uses these indexes to keep track of different table records: {0-Invoice 1-Buyer 2-Sales 3-Items}
raw_strings = [r"INSERT INTO Invoice VALUES ({}, '{}', {}, {}, {}, {});", r"INSERT INTO Buyer VALUES ({}, '{}', '{}', '{}');", r"INSERT INTO Sales VALUES ({}, '{}', '{}');", r"INSERT INTO Sales VALUES ({}, '{}', '{}', {}, {}, '{}');"]
inputFileNames = ["Items.txt", "Sales.txt", "Buyer.txt", "Invoice.txt"]
outputFileNames = ["ItemsTable.txt", "SalesTable.txt", "BuyerTable.txt", "InvoiceTable.txt"]
outputCommands = [r"lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]", r"lines[0], lines[1], lines[2], lines[3]", r"lines[0], lines[1], lines[2]", r"lines[0], lines[1], lines[2], lines[3], lines[4], lines[5]"]
strings = []
lines = []
fileLines = []
command = ""  # String used with exec() to convert string to Python code

def readFromFile(i):
    """This function is used to read table records from a .txt file, the filenames are in the 'inputFileNames' list.
        This function takes a parameter - index of 'inputFileNames'.
    """
    with open(inputFileNames[i], 'r') as f:
        fileLines = f.readlines()
        for element in fileLines:
            lines = element.replace('\n', '').split('\t')
            command = "strings.append(raw_strings[i].format(" + outputCommands[i] + "))"
            exec(command)

def outputToFile(i):
    """This function is used to write SQL codes to a .txt file, the filenames are in the 'outputFileNames' list
        This function takes a parameter - index of 'outputFileNames'.
    """
    with open(outputFileNames[i], 'w') as f:
        for string in strings:
            f.write(string + '\n')

def clearLists():
    """This function is used to clear the lists used for operation in every iteration of the for loop (to prevent existing data from interrupting future data)"""
    strings.clear()
    lines.clear()
    fileLines.clear()

# Main Function Used For Formatting {Invoice, Buyer, Sales, Items} Tables
def main():
    for i in list(range(0, 4)):
        readFromFile(i)
        outputToFile(i)
        clearLists()

main()
