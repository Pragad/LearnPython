#! /usr/bin/env/python

#-------------------------------------------------------------------------------------------
# findGCD(numsList)
#       Function to calculate the gcd of numbers
#-------------------------------------------------------------------------------------------
def findGCD(numA, numB):
    if (numA < numB):
        return findGCD(numB, numA)

    if (numA % numB == 0):
        return numB
    else:
        return findGCD(numB, numA % numB)

#-------------------------------------------------------------------------------------------
# findGCDList(numsList)
#       Function to calculate the gcd of numbers
#-------------------------------------------------------------------------------------------
def findGCDList(numsList):
    
    myTmpList = numsList[:]
    myTmpList.sort()

    index = 0
    if (len(numsList) == 0):
        return 0

    tmpGCD = numsList[0]

    for index in range(len(numsList)):
        tmpGCD = findGCD(tmpGCD, numsList[index])

    return tmpGCD

#-------------------------------------------------------------------------------------------
# numsBetweenTwoSets(myStr):
#       We say that a positive integer x, is between sets if the below conditions are met.
#       Given two lists, find the number of integers that are between the two sets such that
#       1. All elements in ListA are factors of x.
#       2. x is a factor of all elements in ListB
#
#       LOGIC:
#       - Find LCM of ListA ---> (1)
#       - Find GCD of ListB ---> (2)
#       - Find multiple of LCM that could be between (1) and (2)
#-------------------------------------------------------------------------------------------
def numsBetweenTwoSets(listA, listB):
    print("Gcd of two numbers: ")
    gcd = findGCD(4, 5)
    print(gcd)

    numsList = [6, 21, 15, 60]
    print("Gcd of List: ")
    gcd = findGCDList(numsList)
    print(gcd)

    return gcd
    

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    print("My Practice Problems")

    # Declare a list
    listA = []
    listB = []

    # Hackerrank Contest W25 Problem 1
    # Find the number of numbers that could be between to sets
    sumList = numsBetweenTwoSets(listA, listB)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


