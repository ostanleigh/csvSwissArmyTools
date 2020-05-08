import csv
import json
from os import path

print("This script is designed to create a list of dictionaries from a CSV File.")
print("This script assumes you can meet the following requirements to run:")
print("		1) The file you are working with has clearly defined headers.")
print("		2) You can review the headers ('.head') ")
print("		3) You wish to leverage the headers as keys, create a dict per row, and use the row values as Dict vals.")
while True:
    userFileVal = input("\n Dynamic Dictionaries from CSV file,"
    "\n \n What is the name of the csv file you would like to work with? (Don't enter the file extension.):  ")
    try:
        filename = path.exists(userFileVal+'.csv')
    except FileNotFoundError:
        print("Wrong file or file path")
    else:
        break
#filename = input("What is the name of the csv file you would like to work with? (Don't enter the file extension.) ? ")
userEvalIn = input("Do you want to remove any columns or characters from the left of the header? Y or N?: ")
userEval = str.lower(userEvalIn)
if userEval == 'y':
    startIndex = int(input("How many fields should be trimmed from left margin? Enter an integer: "))
    # If  file corruption introduces characters, or redundant file based index is in place
    # Can add lines to support further indexing / slicing as needed
else:
    startIndex = 0
outFileName = input("What do you want to name your output file? Please enter a valid csv file name: ")
with open (userFileVal+'.csv', 'r') as csvInputFile:
    filereader = csv.reader(csvInputFile)
    headerRaw = next(filereader)
    header = headerRaw
    header = headerRaw[startIndex:]
    print(f"header is: {header}")
    with open (outFileName+'.json','w',newline='') as jsonOutputFile:
        filereader = csv.reader(csvInputFile)
        outDicts = [ ]
        for line in filereader:
            keyValsRaw = next(filereader)
            keyVals = keyValsRaw[ startIndex: ]
            # If  file corruption introduces characters, or redundant index is in place
            # keyVals = keyValsRaw[1:]
            # use further indexing / slicing as needed
            headerKeys = dict.fromkeys(header)
            zipObj = zip(headerKeys, keyVals)
            dictObj = dict(zipObj)
            outDicts.append(dictObj)
        filewriter = json.dump(outDicts,jsonOutputFile)
print("Close")



