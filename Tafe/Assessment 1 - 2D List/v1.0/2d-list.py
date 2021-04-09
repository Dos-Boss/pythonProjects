# Python Tafe Assessment 1 - v1.0
# Brendan McCann
# 10/02/2021

import random

hours = 24
days = 31

lstTemps = []
for i in range(days):
  x = []
  for j in range(hours):
    x.append(round(random.gauss(25, 5), 1))
  lstTemps.append(x)

def averageNoonTemp(lst):
  tempSum = 0
  for i in range(len(lst)):
    tempSum += lst[i][11]
  aTemp = tempSum / len(lst)
  print("The average afternoon temperature is: {:.2f} degrees \n".format(aTemp))

def sortList(lst):
  for i in range(len(lst)):
    lst[i].sort()

# This algorithm relies on a sorted array. 
# It sets the search boundary with start, mid and end.
# The mid value is then compared with x(the value we are searching for).
# Depending on the above result, the boundary is then cut in half, 
# getting rid of the redundant data. This process repeats until our 
# desired value is located or deemed to be absent from the array.
def binarySearch(lst,x):
  start = 0
  mid = 0
  end = len(lst) - 1

  while start <= end:
    mid = (start + end) // 2

    if lst[mid] < x:
      start = mid + 1
    elif lst[mid] > x:
      end = mid - 1
    else:
      print("Temperature of {0} degrees found at index {1} \n".format(x, mid))
      return 
  print("\nTemperature of {0} degrees not found ".format(x))
  return 

def printLowHigh(lst):
  lows = []
  highs = []

  for i in range(len(lst)):
    lows.append(lst[i][0])
    highs.append(lst[i][hours - 1])
  print("Lows: {0}\n".format(lows))
  print("Highs: {0}\n".format(highs))

def testInput(x):
    while True:
        try:
            x = float(x)
        except ValueError:
            x = input("Invalid input, please try again: ")
        else:
            x = round(float(x),1)
            return x

averageNoonTemp(lstTemps)
sortList(lstTemps)
printLowHigh(lstTemps)
input = testInput(input("Enter temperature to search: "))
# Search for inputted temp in day 5's data
binarySearch(lstTemps[4], float(input))
