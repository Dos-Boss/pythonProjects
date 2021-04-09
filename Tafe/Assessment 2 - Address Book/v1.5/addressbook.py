# Python Assessment 2 v1.5
# Address Book Module
# Brendan McCann - J145887
# 09/04/2021

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


def checkExists():
    try:
        with open(fileName, 'rb') as file:
            return True
    except FileNotFoundError:
        open(fileName, 'x')


def buildIndex():
    global index
    index = {"Index": [],
             "Register": [],
             "Name": [],
             "Email": [],
             "Phone": [],
             "Address": []}

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


def addRecord(rec, isFirst=False):
    if isFirst is True:
        with open(fileName, 'wb') as outList:
            pickle.dump(rec, outList, pickle.HIGHEST_PROTOCOL)
    else:
        with open(fileName, 'ab') as outList:
            pickle.dump(rec, outList, pickle.HIGHEST_PROTOCOL)
    buildIndex()
    

def addRecords(recList):
    isFirst = True

    for rec in recList:
        if isFirst is True:
            isFirst = False
            addRecord(rec, True)
        else:
            addRecord(rec)


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
            print("\n*** Name not found! ***\n")
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


def selfDestruct():
    if recordCount() < 1:
        print("\n*** No records to clear ***")
        return

    valid = ["y", "n"]
    confirm = ""
    destruct = False

    from backupManager import wasTodayBackedUp
  
    while confirm not in valid:
        if not wasTodayBackedUp():
            print("\n*** No backup made today ***")
            confirm = input("\nCreate backup before proceeding? y/n: ").lower()

            if confirm == 'y':
                from backupManager import saveBackup
                saveBackup()
                destruct = True
            else:
                confirm = ""
                while confirm not in valid:
                    confirm = input("\nClear all data anyway? y/n: ").lower()
                    if confirm == 'y':
                        destruct = True
                    else:
                        return
        else:
            confirm = 'y'
            destruct = True

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
        print("\n*** All data successfully cleared! ***")
