import json
import sys

print("This script is designed to create a list of dictionaries from a CSV File.")
print("This script assumes you can meet the following requirements to run:")
print("		1) The file you are working with has clearly defined headers.")
print("		2) You can review the headers ('.head') ")
print("		3) You wish to leverage the headers as keys, create a dict per row, and use the row values as Dict vals.")

while True:
    userFileVal = input("\n Nested Dictionary Counter,"
    "\n \n What is the name of the json file you would like to work with? (Don't enter the file extension.):  ")
    try:
        checkExists = open(userFileVal + '.json', 'r').readline()
    except (FileNotFoundError) as err:
        print("File not found.")
    else:
        break

with open (userFileVal+'.json','r') as jsonInputFile:
    filereader = json.load(jsonInputFile)
if isinstance (filereader,dict):
    parseObj = filereader
elif isinstance(filereader[0],dict):
    parseObj = filereader[0]
else:
    print("File contents not a dictionary or list of dictionaries. Check file contents.")
    sys.exit()

def depth(d):
    if (not isinstance(d, dict) or not d):
        return 0
    else:
        return max(depth(v) for k, v in d.items()) + 1
print('Formula Below----------')
print(depth(parseObj))
