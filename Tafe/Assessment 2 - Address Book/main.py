# Python Assessment 2
# Main v1.0
# Brendan McCann - J145887
# 05/04/2021

import addressbook as ab


def addRecord():
    print("\nAdding record:")
    name = input("Please enter name: ").capitalize()
    email = input("Please enter email address: ")
    phone = input("Please enter phone number: ")
    addr = input("Please enter home address: ")

    newRec = ab.Record(name, email, phone, addr)
    ab.addRecord(newRec)

    print("\nRecord succefully added!")

        
def getCommand():
    validCommands = ["0", "1", "2", "3", "4", "5", "H", "HELP", "Q", "QUIT"]
    
    while True:
        uInput = input("\nPlease specify command: ").upper()
        if uInput not in validCommands:
            print("Invalid Command, enter H for help")
            getCommand()
        else:
            if uInput == "Q" or uInput == "QUIT":
                quit()
            elif uInput == "H" or uInput == "HELP":
                main()
            elif uInput == "1":
                print("\nCurrent record count: " + str(ab.recordCount()))
            elif uInput == "2":
                print("\nRecord List:")
                ab.printAllRecords()
            elif uInput == "3":
                addRecord()
            elif uInput == "4":
                ab.delRecord(input("\nPlease enter name to remove: "))
            elif uInput == "5":
                ab.getRecord(input("\nPlease enter name to lookup: "))
            else:
                return


def main():
    print("***************************************************")
    print("        Python Assessment 2 - Address Book v1.0")
    print("               Brendan McCann - J145887")
    print("***************************************************")
    print("[1] - Print current record count")
    print("[2] - Print all records")
    print("[3] - Add a record")
    print("[4] - Delete a record")
    print("[5] - Lookup record")
    print("[H] - Help - Show this menu")
    print("[Q] - Quit")
    
    getCommand()

ab.checkExists()
ab.buildIndex()
main()
