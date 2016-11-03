#! /usr/bin/env/python

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

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

