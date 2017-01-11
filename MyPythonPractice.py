#! /usr/bin/env/python
import json
import datetime
from collections import defaultdict

#-------------------------------------------------------------------------------------------
# getInputList(myList):
#        Get Input Numbers to a list
#-------------------------------------------------------------------------------------------
# Main Function
def getInputList(myList):
    # Get a list of numbers until the user enters a blank line
    line = input("Enter list of numbers: \n")

    #while (line not in ['\n', '\r\n']):
    while (line):
        myList.append(int(line))

        line = input()

        if (line in ('\n', '\r\n')):
            break

#-------------------------------------------------------------------------------------------
# printList(myList)
#       Function to print a list
#       Print a list using three methods
#-------------------------------------------------------------------------------------------
def printList(myList):

    # METHOD 1
    print(myList)

    # METHOD 2
    for elmt in myList:
        # Extra comma at end makes sure that it gets printed on the same line
        print(elmt, ', ', end=''),
    print()

    # METHOD 3
    for index in range(len(myList)):
        # Extra comma at end makes sure that it gets printed on the same line
        print(myList[index], ', ', end=''),
    print()


#-------------------------------------------------------------------------------------------
# sumOfNum(myList)
#       Function to calculate the sum of numbers
#-------------------------------------------------------------------------------------------
def sumOfNum(myList):
    sumList = 0

    for elmt in myList:
        sumList += elmt

    return sumList

#-------------------------------------------------------------------------------------------
# sort(myList)
#       Function to sort a list
#-------------------------------------------------------------------------------------------
def sortList(myList):

    # Copy a list
    tmpList = myList[:]
    tmpList.sort()
    print("Tmp List")
    print(tmpList)

#-------------------------------------------------------------------------------------------
# findFirstRepeatedChar(myStr):
#       Find First Repeated Char
#-------------------------------------------------------------------------------------------
def findFirstRepeatedChar(myStr):
    strDict = {}
    repChar = ''

    for c in myStr:
        if (c in strDict):
            repChar = c
            break;
        else:
            strDict[c] = 1

    if (repChar):
        print("First Repeated Char in \"%s\" : %c" % (myStr, repChar))
    else:
        print("No Repeated Char in \"%s\"" % myStr)

#-------------------------------------------------------------------------------------
# Utility function to print lines in Json format
#-------------------------------------------------------------------------------------
def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=False, indent=4, separators=(',', ': '))

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    print("hello")

    # Declare a list
    myList = []

    # Fill the list with Numbers
    getInputList(myList)

    # Print the List
    printList(myList)

    # Calculate the Sum of Numbers in the List
    sumList = sumOfNum(myList)

    # Problem 1
    # Use the inbuilt sum function to get the sum
    print(sum(myList))
    print(sumList)

    # Problem 2
    # Find First Repeated Character in a String
    myStr = "helola"
    repChar = findFirstRepeatedChar(myStr)

    # Problem 3
    # Sort a list using Builtin method
    numsList = [3, 5, 2, 1, 8, 4]
    sortList(numsList)
    print("Original List")
    print(numsList)

    # Problem 4
    # Adding Variables to list and adding List to Dict
    transType = "debit"
    desc = "restaurant"
    accNo = 123
    accRo = 56
    amt = 9877
    myList = [desc, accNo, accRo, amt]
    myDict1 = {}
    myDict1["Desc"] = desc
    myDict1["AccNo"] = accNo
    myDict1["AccRo"] = accRo
    myDict1["Amount"] = amt

    transType2 = "debit"
    desc2 = "games"
    accNo2 = 100
    accRo2 = 56
    amt2 = 1000
    myList2 = [desc2, accNo2, accRo2, amt2]
    myDict2 = {}
    myDict2["Desc"] = desc2
    myDict2["AccNo"] = accNo2
    myDict2["AccRo"] = accRo2
    myDict2["Amount"] = amt2

    #myDictFinal = {}
    #myDictFinal.setdefault(transType, []).append(myList)
    #myDictFinal.setdefault(transType2, []).append(myList2)

    myDictFinal = {}
    myDictFinal.setdefault(transType, []).append(myDict1)
    myDictFinal.setdefault(transType2, []).append(myDict2)

    #myDict2 = defaultdict(myList)
    #myDict2[transType2].append(myList2)

    #print(myList)
    #print(myList)
    print(myDict1)
    print(myDict2)
    print(myDictFinal)
    print(get_pretty_print(myDictFinal))

    # Problem 5
    # Convert mm/dd/yy to YYYY-MM-DD
    print(datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d"))

    #transDate = "9/9/16"
    transDate = "09/29/2016"
    dateMonth = transDate.split('/')[0]
    dateDay = transDate.split('/')[1]
    dateYear = transDate.split('/')[2]

    # Assumption that the year will be 2000 plus
    if len(dateMonth) == 1:
        dateMonth = '0' + dateMonth

    if len(dateDay) == 1:
        dateDay = '0' + dateDay

    if len(dateYear) == 2:
        # If the year is between 50 and 99, then it is likely to be 1950 - 1999
        if (50 <= int(dateYear) >= 99):
            dateYear = str(int(dateYear) + 1900)
        else:
            dateYear = str(int(dateYear) + 2000)

    newDate = dateYear + '-' + dateMonth + '-' + dateDay
    print(transDate)
    print(newDate)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

