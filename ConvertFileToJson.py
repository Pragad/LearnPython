#-----------------------------------------------------------------------------------------
#  Author: Pragad Thiru
#
#  Execution Instructions: python EarnUp_PragadThiru_ConvertFileToJson.py
#-----------------------------------------------------------------------------------------

#! /usr/bin/env/python
import json
import sys
from collections import OrderedDict
from collections import defaultdict

#-----------------------------------------------------------------------------------------
# Class 1
#-----------------------------------------------------------------------------------------
class ConvertFileToJson:
    'Convert File to Json Class'

    #-------------------------------------------------------------------------------------
    # Constructor
    #   _inFileName     : Input File Name
    #   _outFileName    : Output File Name
    #   _inFileLines    : List of the entire input file
    #   _allTransDict   : Json formatted result in Dictionary
    #-------------------------------------------------------------------------------------
    def __init__(self, name, age = 1):
        self._inFileName = name
        self._outFileName = "ZBGoutputJSON.txt"
        self._inFileLines = []
        self._allTransDict = OrderedDict()

    #-------------------------------------------------------------------------------------
    # This is the function that does all the work
    #   1. Open file and read lines
    #   2. Parse the lines and convert to correct Json format and populate in Dictionary
    #   3. Write the result to file
    #-------------------------------------------------------------------------------------
    def convertToJson(self):
        self.openAndReadFile()
        self.parseLinesAndConvertToJsonDict()
        self.writeOutputToFile()

    #-------------------------------------------------------------------------------------
    # Utility function to format the date
    #-------------------------------------------------------------------------------------
    def formatDate(self, transDate):
        
        # This is an easier way to convert from MM/DD/YYYY to YYYY-MM-DD
        # But we might have two digit year. So can't use the below technique
        # datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")

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

        return newDate

    #-------------------------------------------------------------------------------------
    # Utility function to open and read the file
    # This will copy all the lines into a list of lines
    #-------------------------------------------------------------------------------------
    def openAndReadFile(self):
        try:
            with open(self._inFileName) as f:
                self._inFileLines = f.readlines()
        except (OSError, IOError) as e:
            print("Exception Opening File: ", e)
            sys.exit()
                
    #-------------------------------------------------------------------------------------
    # Utility function to take each line and convert it into the right format
    # After converting to right format it will put the line into the dictionary
    #-------------------------------------------------------------------------------------
    def parseLinesAndConvertToJsonDict(self):
        isStartTagSeen = False
        isEndTagSeen = False
        isTransStart = False

        transDescription = None
        transType = None
        transOriginAccnt = None
        transOriginRoute = None
        transDestAccnt = None
        transDestRoute = None
        transAmount = None

        # Identify the lines between "START ZBG and END ZBG"
        # Once you see '==', mark beginning of a transaction
        for index in range(len(self._inFileLines)):

            # Check if the line contains the 'Start Tag or End Tag'
            if self._inFileLines[index].rstrip('\n') == '*START ZBG*':
                isStartTagSeen = True
                isEndTagSeen = False

                # We can continue as we don't want to insert the TAG
                continue

            elif self._inFileLines[index].rstrip('\n') == '*END ZBG*':
                isStartTagSeen = False
                isEndTagSeen = True

                # We can continue as we don't want to insert the TAG
                continue

            # We should insert lines that are only within START ZBG and END ZBG
            if (isStartTagSeen) and (not isEndTagSeen):
                # Check if the lines contains ':'. If so, split it and add the entries
                if (":" in self._inFileLines[index]) and (not isTransStart):
                    
                    # Format the date to correct format
                    if self._inFileLines[index].split(':')[0].strip().rstrip('\n') == 'Date':
                        transDate = self._inFileLines[index].split(':')[1].strip().rstrip('\n')
                        transNewDate = self.formatDate(transDate)
                        self._allTransDict[self._inFileLines[index].split(':')[0]] = transNewDate

                    else:
                        self._allTransDict[self._inFileLines[index].split(':')[0]] = self._inFileLines[index].split(':')[1].strip().rstrip('\n')
                        continue

                # Check if the lines contains '=='. If so mark beginning of transaction
                elif self._inFileLines[index].rstrip('\n').strip() == '==':
                    if isTransStart == True:

                        # Reached end of transaction. Put all entries in a dictionary
                        # Add the dictionary to the final dictionary
                        tmpTransDict = OrderedDict()
                        tmpTransDict['Description'] = transDescription
                        tmpTransDict['OriginAccount'] = transOriginAccnt
                        tmpTransDict['OriginRouting'] = transOriginRoute
                        tmpTransDict['DestinationAccount'] = transDestAccnt
                        tmpTransDict['DestinationRouting'] = transDestRoute
                        tmpTransDict['Amount'] = transAmount

                        self._allTransDict.setdefault(transType, []).append(tmpTransDict)
                        continue
                    else:
                        isTransStart = True;
                        continue

                # Once a transaction has started copy each individual items into
                # corresponding variables.
                # This way, once the end of transaction is reached we can copy all the
                # variable we have into the dictionary
                if isTransStart == True:
                    if self._inFileLines[index].split(':')[0] == 'Description':
                        transDescription = self._inFileLines[index].split(':')[1].lstrip().rstrip('\n')
                        
                    elif self._inFileLines[index].split(':')[0] == 'Type':
                        transType = self._inFileLines[index].split(':')[1].lstrip().rstrip('\n')
                        if transType == 'Debit':
                            transType = 'Debits'
                        elif transType == 'Credit':
                            transType = 'Credits'
                        
                    elif self._inFileLines[index].split(':')[0] == 'Origin':
                        transOriginAccnt = self._inFileLines[index].split(':')[1].split('/')[0].strip().rstrip('\n')
                        transOriginRoute = self._inFileLines[index].split(':')[1].split('/')[1].strip().rstrip('\n')
                        
                    elif self._inFileLines[index].split(':')[0] == 'Destination':
                        transDestAccnt = self._inFileLines[index].split(':')[1].split('/')[0].strip().rstrip('\n')
                        transDestRoute = self._inFileLines[index].split(':')[1].split('/')[1].strip().rstrip('\n')
                        
                    elif self._inFileLines[index].split(':')[0] == 'Amount':
                        transAmount = (int(self._inFileLines[index].split(':')[1].lstrip().rstrip('\n')) / 100)
 

    #-------------------------------------------------------------------------------------
    # Save to file:
    #-------------------------------------------------------------------------------------
    def writeOutputToFile(self):
        with open(self._outFileName, 'w') as f:
            jsonString = json.dumps(self._allTransDict, sort_keys=False, indent=4, separators=(',', ': '))

            #print(jsonString)
            json.dump(self._allTransDict, f, sort_keys=False, indent=4, separators=(',', ': '))

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    objConvertFile = ConvertFileToJson("ZBGtransactions.txt");
    objConvertFile.convertToJson()

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

