# Python Assessment 2
# Address Book Module v1.0
# Brendan McCann - J145887
# 05/04/2021

import pickle


fileName = "addrbook.bin"


class Record:
    def __init__(self, name, email, phone, addr):
        self.name = name
        self.email = email
        self.phone = phone
        self.addr = addr

    def getInfo(self):
        return("Name: " + self.name + " | " +
               "Email: " + self.email + " | " +
               "Phone: " + self.phone + " | " +
               "Address: " + self.addr)


# Startup command to check if the .bin file exists, if not, an empty dummy file is created.
def checkExists():
    try:
        with open(fileName, 'rb') as file:
            return True
    except FileNotFoundError:
        x = open(fileName, 'x')


# Checks if item being added is first in an array
# if so, it is added as 'write' (effectively overwriting any existing pickle file)
# if it's not, then the additional items are appended.
def addRecord(rec, isFirst=False):
    if isFirst is True:
        with open(fileName, 'wb') as outList:
            pickle.dump(rec, outList, pickle.HIGHEST_PROTOCOL)
    else:
        with open(fileName, 'ab') as outList:
            pickle.dump(rec, outList, pickle.HIGHEST_PROTOCOL)
    buildIndex()
    

# Handles adding an array of Records
def addRecords(recList):
    isFirst = True

    for rec in recList:
        if isFirst is True:
            isFirst = False
            addRecord(rec, True)
        else:
            addRecord(rec)


# Creates a list of names from the index file in lowercase for comparisons
def getLowerList():
    lowerList = []
    for x in range(len(index["Name"])):
        lowerList.append(index["Name"][x].lower())
    return lowerList


def delRecord(name, givenIndex=None):
    lowerList = getLowerList()

    if givenIndex is None:
        try:
            x = lowerList.index(name)
        except ValueError:
            print("Name not found!\n")
    else:
        x = givenIndex

    if lowerList.count(name) == 1 or givenIndex is not None:
        del index["Index"][x]
        del index["Register"][x]
        del index["Name"][x]
        del index["Email"][x]
        del index["Phone"][x]
        del index["Address"][x]
        # Rebuild pickled file from adjusted index dictionary.
        pickleFromIndex()
        print("\nRecord deleted successfully")

    elif lowerList.count(name) > 1 and givenIndex is None:
        occLocations = [i for i, x in enumerate(lowerList) if x == name]
        print(f"\n*** {len(occLocations)} occurances of {name.capitalize()} found! ***\n")
        with open(fileName, 'rb') as file:
            for x in range(len(occLocations)):
                file.seek(index["Register"][occLocations[x]])
                y = pickle.load(file)
                print(f"Index {occLocations[x]} | " + y.getInfo() + "\n")

        while True:
            uInput = input("\n'c' to Cancel\nPlease enter index number of record you wish to delete: ")
            if uInput == "c":
                return
            try:
                if int(uInput) in occLocations:
                    delRecord(name, int(uInput))
                    return
                else:
                    pass
            except ValueError:
                pass
          
            
def getRecord(name):
    lowerList = getLowerList()

    if name.lower() in lowerList:
        if lowerList.count(name) < 2:
            x = lowerList.index(name)
            with open(fileName, 'rb') as file:
                file.seek(index["Register"][x])
                y = pickle.load(file)
                print(f"\nRecord found at index {x}.")
                print(y.getInfo())
            return
        else:
            occLocations = [i for i, x in enumerate(lowerList) if x == name]
            print(f"\n*** {len(occLocations)} occurances of {name.capitalize()} found! ***\n")
            with open(fileName, 'rb') as file:
                for x in range(len(occLocations)):
                    file.seek(index["Register"][occLocations[x]])
                    y = pickle.load(file)
                    print(f"Index: {occLocations[x]} | " + y.getInfo() + "\n")
    else:
        print("\nNo record found.")


# Prints a number equal to the amount of items in pickle file
def recordCount():
    count = 0

    for item in readFile(fileName):
        count += 1
    return count


# When iterated through, examines contents of pickle file and adds entry register points to an array.
def readFile(path):
    global lstIndex
    lstIndex = []

    with open(path, 'rb') as file:
        try:
            while True:
                lstIndex.append(file.tell())
                yield pickle.load(file)
        except EOFError:
            pass
    

def printAllRecords():
    recordCount()

    with open(fileName, 'rb') as file:
        for x in range(len(lstIndex)):
            try:
                file.seek(lstIndex[x])
                y = pickle.load(file)
                print(f"Index: {x} | " + y.getInfo())
            except EOFError:
                break


# Constructs a dictionary of pickled information
def buildIndex():
    global index
    index = {"Index": [],
             "Register": [],
             "Name": [],
             "Email": [],
             "Phone": [],
             "Address": []}

    # Recount number of records and update register index array.
    recordCount()

    with open(fileName, 'rb') as file:
        for x in range(len(lstIndex)):
            try:
                file.seek(lstIndex[x])
                y = pickle.load(file)
                index["Index"].append(x)
                index["Register"].append(lstIndex[x])
                index["Name"].append(y.name)
                index["Email"].append(y.email)
                index["Phone"].append(y.phone)
                index["Address"].append(y.addr)
            except EOFError:
                break


# Creates an array of Records from the index dictionary and parses it for pickling.
def pickleFromIndex():
    toAdd = []
    with open(fileName, 'wb') as file:
        for x in range(len(index["Index"])):
            name = index["Name"][x]
            email = index["Email"][x]
            phone = index["Phone"][x]
            addr = index["Address"][x]

            newRec = Record(name, email, phone, addr)
            toAdd.append(newRec)
        addRecords(toAdd)
