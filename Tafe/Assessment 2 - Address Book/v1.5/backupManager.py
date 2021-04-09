# Python Assessment 2 v1.5
# Backup Manager Module
# Brendan McCann - J145887
# 09/04/2021


import addressbook as ab
import os
from datetime import datetime
import shutil


def saveBackup():
    backupName = ("./Backups/" + datetime.now().strftime("%b-%d-%Y-%H-%M-%S") + ".bak")

    if ab.recordCount() < 1:
        print("\n*** No data to save ***")
    else:
        if not os.path.exists("./Backups/"):
            os.makedirs(os.path.dirname(backupName), exist_ok=True)

        shutil.copy(ab.fileName, backupName)
        print("\n" + (datetime.now().strftime("%b-%d-%Y-%H-%M-%S") + ".bak" + " saved"))


def loadBackup():
    backupList = getListofBackups()
    if len(backupList) > 0 and os.path.exists("./Backups/"):
        if len(backupList) > 1:
            printListofBackups(backupList)
            uInput = ""
            while not uInput.isnumeric():
                uInput = input("Please enter number of backup to load: ")
            while int(uInput) > (len(backupList) - 1) or int(uInput) < 0:
                uInput = input("Please enter number of backup to load: ")

            backupName = ("./Backups/" + backupList[int(uInput)])
            shutil.copy(backupName, ab.fileName)
            print(f"\n{backupList[int(uInput)]} loaded!")
        else:
            backupName = ("./Backups/" + backupList[0])
            shutil.copy(backupName, ab.fileName)
            print(f"\n{backupList[0]} loaded")
    else:
        print("\n*** No backups found ***")


def deleteBackup():
    valid = ["c", "cancel", "a", "all"]
    backupList = getListofBackups()
    if len(backupList) > 0 and os.path.exists("./Backups/"):
        printListofBackups(backupList)
        uInput = ""

        while uInput not in valid:
            try:
                int(uInput)
            except ValueError:
                uInput = input("\n(C)ancel, (A)ll\nPlease enter number of backup to delete: ").lower()
            else:
                if int(uInput) > (len(backupList) - 1) or int(uInput) < 0:
                    uInput = ""
                else:
                    break

        if uInput in valid[0:2]:
            return
        elif uInput in valid[2:5]:
            shutil.rmtree("./Backups/")
            print("\nAll backups deleted")
        else:
            toDelete = ("./Backups/" + backupList[int(uInput)])
            os.remove(toDelete)
            print(f"\n{backupList[int(uInput)]} deleted")
            return

    else:
        print("\n*** No backups to delete ***")
          

def getListofBackups():
    if os.path.exists("./Backups/"):
        _, _, backupList = next(os.walk("./Backups/"))
        return backupList
    else:
        return [0]


def printListofBackups(backupList):
    print("\nCurrent Backups")
    for x in range(len(backupList)):
        print(str(x) + ": " + backupList[x])
    print("")

def wasTodayBackedUp():
    backupList = getListofBackups()
    if os.path.exists("./Backups/") and len(backupList) > 0:
        todaysDate = datetime.now().strftime("%b-%d-%Y")
        for x in backupList:
            if todaysDate in x:
                return True
    else:
        return False
                

def getCommand():
    validCommands = ["1", "2", "3", "H", "HELP", "M", "MAIN", "Q", "QUIT"]
    
    while True:
        print("")
        uInput = input("Please specify command: ").upper()
        if uInput not in validCommands:
            print("Invalid command, enter H for help")
            getCommand()
        else:
            if uInput == "H" or uInput == "HELP":
                os.system('cls' if os.name == 'nt' else 'clear')
                menu()
            elif uInput == "M" or uInput == "MAIN":
                break
            elif uInput == "Q" or uInput == "QUIT":
                quit()
            elif uInput == "1":
                saveBackup()
                getCommand()
            elif uInput == '2':
                loadBackup()
                ab.buildIndex()
                getCommand()
            else:
                deleteBackup()
                getCommand()

        return False
                         

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("===================================================")
    print("        Python Assessment 2 - Address Book v1.5")
    print("               Brendan McCann - J145887")
    print("                   Backup Manager")
    print("===================================================")
    print("[1] - Save Backup")
    print("[2] - Load Backup")
    print("[3] - Delete Backup")
    print("[H] - Help - Show This Menu")
    print("[M] - Return to Main Menu")
    print("[Q] - Quit Program")

    getCommand()
