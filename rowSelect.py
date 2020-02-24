import csv
print("This script is designed to let you select row(s) from a csv file containing a user provided value.")

while True:
    userFileVal = input("\n Display rows containing a value in  a CSV file,"
    "\n \n What is the name of the csv file you would like to work with? (Don't enter the file extension.):  ")
    try:
    	checkExists = open (userFileVal+'.csv','r').readline()
    except (FileNotFoundError) as err:
        print("File not found.")
    else:
        break
userSelectIn = input("What value would you like to profile? ")
userSelect = userSelectIn.lower()
outFileName = input('What would you like to name the output file? Please enter a valid csv file name: ')
with open (userFileVal+'.csv','r') as csvInputFile:
    with open (outFileName + '.csv', 'w', newline='') as csvOutputFile:
        filereader = csv.reader(csvInputFile)
        filewriter = csv.writer(csvOutputFile)
        for line in filereader:
            filewriter.writerow(line)
            for line in filereader:
                for cell in line:
                    if cell.lower() == userSelect:
                        filewriter.writerow(line)
with open (outFileName + '.csv', 'r') as passbackFile:
    nextFileReader = csv.reader(passbackFile)
