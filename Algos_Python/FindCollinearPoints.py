#! /usr/bin/env/python
# Author: Pragad Thirumurthi
import csv
import math

# https://www.quora.com/Given-N-points-on-the-plane-what-is-an-efficient-algorithm-to-find-all-the-sets-of-3-or-more-collinear-points
# https://stackoverflow.com/questions/4557840/find-all-collinear-points-in-a-given-set
# https://www.geeksforgeeks.org/count-maximum-points-on-same-line/
# https://stackoverflow.com/questions/25342885/finding-the-maximum-number-of-points-that-lie-on-the-same-straight-line-in-a-2d
# https://math.stackexchange.com/questions/701862/how-to-find-if-the-points-fall-in-a-straight-line-or-not

#-------------------------------------------------------------------------------
# Read input CSV File and store it in a list in the form of a tuple
#-------------------------------------------------------------------------------
def readInputCSVFile(listOfPoints):
    # Reading the input CVS file and creating tuple of pair of points
    with open('test_example.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            xCord = row[0]
            yCord = row[1]
            listOfPoints.append((float(xCord), float(yCord)))

#-------------------------------------------------------------------------------
# Write output to a CSV file
# Format the output and write to CSV file
#-------------------------------------------------------------------------------
def writeOutputToCSVFile(resultListOfPoints):
    with open('test_output.csv', 'w') as csvfile:
        lineId = 1
        for listOfPoints in resultListOfPoints:
            line = str(lineId)+"," 
            lineId = lineId + 1
            for point in listOfPoints:
                line += str(point[0]) + "," + str(point[1])+","
            line = line[:-1]
            csvfile.write(line)
            csvfile.write('\n')

#-------------------------------------------------------------------------------
# Given three points, this function returns if they are collinear or not
# To compare floats, using math.isclose function as equality comparison will
# fail due to the way floating numbers get stored
#-------------------------------------------------------------------------------
def arePointsCollinear(p1, p2, p3):
    lhs = (p1[1] - p2[1]) * (p1[0] - p3[0])
    rhs = (p1[1] - p3[1]) * (p1[0] - p2[0])
    if math.isclose(lhs, rhs, rel_tol=1e-5):
        return True
    else:
        return False

#-------------------------------------------------------------------------------
# Brute force approach
# For each pair of point, find if more point lie along the same line
# Time Complexity: O(N^3)
# This is a straight forward approach. This can be made better by improving
# the time complexity
#-------------------------------------------------------------------------------
def findCollinearPointsBruteForce(listOfPoints):
    resultListOfPoints = []
    listOfDist = []
    tmpList = []
    for index1 in range(len(listOfPoints)):
        for index2 in range(index1 + 1, len(listOfPoints)):
            # Clear the list to start with
            tmpList = []
            point1 = listOfPoints[index1]
            point2 = listOfPoints[index2]
            tmpList.append(point1)
            tmpList.append(point2)
            for index3 in range(index2 + 1, len(listOfPoints)):
                if index1 == index3 or index2 == index3:
                    continue
                point3 = listOfPoints[index3]
                if arePointsCollinear(point1, point2, point3):
                    tmpList.append(point3)

            # If we already have a bigger line that contains all the points, then
            # ignore the current list of points
            if len(tmpList) >= 3:
                tmpCount = 0
                for entry in tmpList:
                    for origList in resultListOfPoints:
                        if entry in origList:
                            tmpCount = tmpCount + 1
                            break;
                if tmpCount == len(tmpList):
                    continue;

                # Create a set out of the points and add it to the result list
                setOfPoints = set()
                for entry in tmpList:
                    setOfPoints.add(entry)
                resultListOfPoints.append(setOfPoints)
    return resultListOfPoints

#-------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------
def main():
    # Assuming all points from the CSV file would fit in memory
    # This approach will fail if the CSV file can't be fit in memory
    # The below list stores pairs of points from the input CSV file
    listOfPoints = []

    readInputCSVFile(listOfPoints)
    resultListOfPoints = findCollinearPointsBruteForce(listOfPoints)
    writeOutputToCSVFile(resultListOfPoints)

#-------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

