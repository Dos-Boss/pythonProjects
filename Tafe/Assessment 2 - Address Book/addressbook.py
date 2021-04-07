# Python Assessment 2
# Address Book Module v1.0
# Brendan McCann - J145887
# 05/04/2021

import pickle
import shutil


fileName = "addrbook.bin"
backupCreated = bool

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

def recordCount():
    count = 0

    for item in readFile(fileName):
        count += 1
    return count


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


def createRecord():
    print("\n*** Adding Record ***\n")
    name = input("Please enter name: ").capitalize()
    email = input("Please enter email address: ")
    phone = input("Please enter phone number: ")
    addr = input("Please enter home address: ")

    newRec = Record(name, email, phone, addr)
    addRecord(newRec)

    print("\n*** Record Successfully Added! ***")


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
            print("*** Name not found! ***\n")
    else:
        x = givenIndex

    if lowerList.count(name) == 1 or givenIndex is not None:
        del index["Index"][x]
        del index["Register"][x]
        del index["Name"][x]
        del index["Email"][x]
        del index["Phone"][x]
        del index["Address"][x]

        return 1

    elif lowerList.count(name) > 1 and givenIndex is None:
        foundLocations = [i for i, x in enumerate(lowerList) if x == name]
        print(f"\n*** {len(foundLocations)} occurances of {name.capitalize()} found! ***\n")
        with open(fileName, 'rb') as file:
            for x in range(len(foundLocations)):
                file.seek(index["Register"][foundLocations[x]])
                y = pickle.load(file)
                print(f"Index {foundLocations[x]} | " + y.getInfo() + "\n")

        while True:
            uInput = input("\n(C)ancel, (A)ll\nPlease enter index number of record you wish to delete: ")
            if uInput.lower() == "c" or uInput.lower() == "cancel":
                return
            elif uInput.lower() == "a" or uInput == "all":
                registersToDel = []
                indexToDel = 0

                for x in range(len(foundLocations)):
                    registersToDel.append(index["Register"][foundLocations[x]])

                for x in registersToDel:
                    indexToDel = index["Register"].index(x)
                    delRecord(index["Name"][indexToDel], indexToDel)
                return 2
            else:
                try:
                    if int(uInput) in foundLocations:
                        delRecord(name, int(uInput))
                        return 1
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
                print("\n*** Match found! ***")
                print(f"\nIndex: {x} | " + y.getInfo() + "\n")
            return
        else:
            foundLocations = [i for i, x in enumerate(lowerList) if x == name]
            print(f"\n*** {len(foundLocations)} Occurances of {name.capitalize()} Found! ***\n")
            with open(fileName, 'rb') as file:
                for x in range(len(foundLocations)):
                    file.seek(index["Register"][foundLocations[x]])
                    y = pickle.load(file)
                    print(f"Index: {foundLocations[x]} | " + y.getInfo() + "\n")
    else:
        print("\n*** No matches found ***")


# Wipes data from index and pickled file
def selfDestruct():
    if recordCount() < 1:
        print("\n*** Records already clear ***")
        return

    valid = ["y", "n"]
    confirm = ""
    destruct = False

    print("\n*** This will erase ALL data in current address book ***\n")

    while confirm not in valid:
        confirm = input("Create backup before proceeding? y/n: ").lower()

    if confirm == 'y':
        if saveBackup():
            destruct = True
        else:
            confirm = ""
            while confirm not in valid:
                confirm = input("\nWipe all data anyway? y/n: ").lower()
                if confirm == 'y':
                    destruct = True
                else:
                    return

    if confirm == 'n':
        confirm = ""
        while confirm not in valid:
            confirm = input("\nWipe all data anyway? y/n: ").lower()
        if confirm == 'y':
            destruct = True
        else:
            return

    if destruct:
        global index
        index.clear()
        index = {"Index": [],
                 "Register": [],
                 "Name": [],
                 "Email": [],
                 "Phone": [],
                 "Address": []}
        pickleFromIndex()
        buildIndex()
        print("\n*** All data successfully wiped! ***")


def saveBackup():
    if recordCount() < 1:
        print("\n*** No data to save! ***")
    else:
        try:
            open("addrbook.bak")
        except FileNotFoundError:
            shutil.copy(fileName, "addrbook.bak")
            print("\n*** Backup successfully saved! ***")
            return True
        else:
            valid = ["y", "n"]
            confirm = ""

            while confirm not in valid:
                confirm = input("\nOverwrite current backup? y/n: ")

            if confirm == 'y':
                shutil.copy(fileName, "addrbook.bak")
                print("\n*** Backup successfully saved! ***")
                return True
            else:
                return False

        
def loadBackup():
    try:
        open("addrbook.bak")
    except FileNotFoundError:
        print("\n*** No data to backup! ***")
    else:
        shutil.copy("addrbook.bak", fileName)
        buildIndex()
        print("\n*** Backup successfully restored! ***")
        return
