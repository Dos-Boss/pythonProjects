# Python Assessment 2 v1.5
# Main
# Brendan McCann - J145887
# 09/04/2021

import backupManager as bm
import addressbook as ab
import os

        
def getCommand():
    validCommands = ["1", "2", "3", "4", "5", "6", "7", "8", "H", "HELP", "Q", "QUIT"]
    
    while True:
        print("")
        uInput = input("Please specify command: ").upper()
        if uInput not in validCommands:
            print("Invalid command, enter H for help")
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
                ab.createRecord()
            elif uInput == "4":
                result = 0
                if ab.recordCount() > 0:
                    uInput = input("\nPlease enter name to remove: ")
                    result = ab.delRecord(uInput)
                else:
                    print("\n*** No data to delete! ***")
                    
                if result == 1:
                    print("\n*** Record deleted successfully! ***")
                elif result == 2:
                    print("\n*** Records deleted successfully! ***")
                ab.pickleFromIndex()
            elif uInput == "5":
                if ab.recordCount() > 0:
                    ab.getRecord(input("\nPlease enter name to lookup: "))
                else:
                    print("\n*** No data to search! ***")
            elif uInput == "6":
                ab.selfDestruct()
            elif uInput == "7":
                while bm.menu():
                    pass
                else:
                    main()
            else:
                return


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================================")
    print("        Python Assessment 2 - Address Book v1.5")
    print("               Brendan McCann - J145887")
    print("                      Main Menu")
    print("===================================================")
    print("[1] - Print Current Record Count")
    print("[2] - Print All Records")
    print("[3] - Add a Record")
    print("[4] - Delete a Record")
    print("[5] - Lookup Record")
    print("[6] - Clear Records")
    print("[7] - Backup Manager")
    print("[H] - Help - Show This Menu")
    print("[Q] - Quit Program")
    
    getCommand()


ab.checkExists()
ab.buildIndex()
main()
