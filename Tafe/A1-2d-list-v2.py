# Brendan McCann - J145887
# Python Assessment 1 - V2.0
# 31/03/2021

import random
import copy

hours = 24
days = 31

lstTemps = []

# Generate list of random temps.
def genList():
    lstTemps.clear()
    for day in range(days):
        buildList = []
        for hour in range(hours):
            buildList.append(round(random.gauss(25, 5), 1))
        lstTemps.append(buildList)


# Returns a sorted clone of a given list.
def getSortedList(lst):
    lstSortedTemps = copy.deepcopy(lst)
    
    for day in range(len(lstSortedTemps)):
        lstSortedTemps[day].sort()
    return lstSortedTemps


# Get average afternoon (12th hour) temp.
def avgNoonTemp(lst):
    tempSum = 0
    for day in range(len(lst)):
        tempSum += lst[day][11]
    avgTemp = tempSum / days
    print("\nThe average afternoon temperature is: {:.1f} degrees".format(avgTemp))


# Generate and print lists of daily lows/highs from sorted list
def printLowHigh(lst):
    lstLows = []
    lstHighs = []

    for i in range(len(lst)):
        lstLows.append(lst[i][0])
        lstHighs.append(lst[i][hours - 1])
    
    print("\nLows: " + ", ".join(map(str, lstLows)))
    print("\nHighs: " + ", ".join(map(str, lstHighs)))


# This algorithm relies on a sorted list.
# It sets the search boundary with start, mid and end.
# The mid value is then compared with the temp we are searching for.
# Depending on the above result, the boundary is then cut in half,
# getting rid of the redundant data. This process repeats until our
# desired value is located or deemed to be absent from the array
def binarySearch(lst, day, temp):
    start = 0
    mid = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < temp:
            start = mid + 1
        elif lst[mid] > temp:
            end = mid - 1
        else:
            print(f"\nDay {day}:")
            print("Temperature of {0} degrees found!, occured on hour {1}.".format(temp, mid + 1))
            return
    print(f"\nDay {day}:")
    print("Temperature of {0} degrees did not occur.".format(temp))
    return

# Validates user input for Binary Search temp.
def validateBSTemp(temp):
    try:
        temp = round(float(temp), 1)
    except ValueError:
        temp = validateBSTemp(input("Please enter temperature to search for: "))
    return round(float(temp), 1)

# Validates user input for Binary Search day.
def validateBSDay(day):

    if day.isnumeric():
        if int(day) > 0 and int(day) < 32:
            return day
        else:
            return validateBSDay(input("Please enter a day to search (1-31) or (A)ll: ").upper())
    elif day == "A" or day == "ALL":
        return day
    else:
        return validateBSDay(input("Please enter a day to search (1-31) or (A)ll: ").upper())

# Main loop to interpret user's command.
def getCommand():
    
    validCommands = ["0", "1", "2", "3", "H", "HELP", "Q", "QUIT"]

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
            elif uInput == "0":
                genList()
                print("\nTemp list regenerated!")
            elif uInput == "1":
                avgNoonTemp(lstTemps)
            elif uInput == "2":
                printLowHigh(getSortedList(lstTemps))
            elif uInput == "3":
                tempToSearch = validateBSTemp(input("\nPlease enter temperature to search for: "))
                dayToSearch = validateBSDay(input("\nPlease enter a day to search (1-31) or (A)ll: ").upper())

                if dayToSearch.isnumeric():
                    binarySearch(getSortedList(lstTemps)[int(dayToSearch) - 1], dayToSearch, tempToSearch)
                else:
                    for day in range(days):
                        binarySearch(getSortedList(lstTemps)[day], day + 1, tempToSearch)

# Displays menu and calls program loop.
def main():
    print("***************************************************")
    print("        Python Assessment 1 - 2D List v2.0")
    print("              Brendan McCann - J145887")
    print("***************************************************")
    print("[0] - Regenerate list of temps")
    print("[1] - Show average afternoon temp")
    print("[2] - Show daily Lows/Highs")
    print("[3] - Search for specific temp")
    print("[H] - Help - Show this menu")
    print("[Q] - Quit")
    
    getCommand()

genList()
main()
