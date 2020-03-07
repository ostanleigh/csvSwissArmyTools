import csv
from os import path

print("\n Extract Columns from CSV File."
      "\n This script is designed to let a user select columns by using column header names."
      "\n The script assumes:"
      "\n 1) You know the file name."
      "\n 2) The desired file is located in the same directory as this script."
      "\n 3) The file contains a header where column names already exist."
      "\n 4) You know the exact case sensitive names of the file and column names you wish to select."
      "\n"
      "\n The output file will be saved to the same directory as the input file."
      "")
while True:
    userFileVal = input(
        "\n What is the name of the csv file you would like to work with? (Don't enter the file extension.):  ")
    try:
        filename = path.exists(userFileVal + '.csv')
    except (FileNotFoundError) as err:
        print("Wrong file or file path")
    else:
        break
userCountS = input("How many columns would you like to profile? Enter an integer: ")
userCount = int(userCountS)
userCols = [ ]
for x in range(0, userCount):
    userSelect = input("Enter column you would like to profile?: ")
    userCols.append(userSelect)
print(f"These are the columns you have selected: {userCols}")
outFileName = input("What do you want to name your output file? Please enter a valid csv file name: ")


def selectIndexes(rawHead, userCols, counter):
    selectIndex = dict()
    for item in rawHead:
        if item in userCols:
            selectIndex[ item ] = counter
        # print(f"selectIndex[item] is: {selectIndex[item]}")
        counter += 1
    return (selectIndex)


with open(userFileVal + '.csv', 'r') as csvInputFile:
    filereader = csv.reader(csvInputFile)
    rawHead = next(filereader)
userIndexes = selectIndexes(rawHead, userCols, 0)
print(f"The Selected columns and their corresponding index values are: {userIndexes}")
indexes = [ ]
for x in rawHead:
    for key in userIndexes:
        if key == x:
            indexes.append(userIndexes[ key ])
print(f"The index values for the selected columns are: {indexes}")
with open('songs.csv', 'r') as csvInputFile:
    with open(outFileName + '.csv', 'w', newline='') as csvOutputFile:
        filereader = csv.reader(csvInputFile)
        fileweriter = csv.writer(csvOutputFile)
        for line in filereader:
            outCols = [ ]
            for index in indexes:
                outCols.append(line[ index ])
            fileweriter.writerow(outCols)
