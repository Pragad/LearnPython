#! /usr/bin/env/python
import json
import sys
from collections import OrderedDict
from collections import defaultdict

#-------------------------------------------------------------------------------------
# Utility function to print lines in Json format
#-------------------------------------------------------------------------------------
def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=False, indent=4, separators=(',', ': '))


linesOrderDict = OrderedDict()

lines = ['*START ZBG*\n', 'Date: 9/9/16\n', 'Description: Payments for John Smith\n', '==\n', 'Description: Mortgage\n', 'Type: Debit\n', 'Origin: 245987 / 21000\n', 'Destination: 987243 / 4259\n', 'Amount: 150500\n', '== \n', 'Description: Gym membership \n', 'Type: Debit\n', 'Origin: 245987 / 21000\n', 'Destination: 59784 / 08345\n', 'Amount: 23700\n', '== \n', 'Description: Credit card return\n', 'Type: Credit\n', 'Origin: 983750 / 73980\n', 'Destination: 987243 / 4259\n', 'Amount: 249030\n', '==\n', '*END ZBG*\n']

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


print(lines)
print("\n")

for index in range(len(lines)):

    # Check if the line contains the 'Start Tag or End Tag'
    if lines[index].rstrip('\n') == '*START ZBG*':
        isStartTagSeen = True
        isEndTagSeen = False

        # We can continue as we don't want to insert the TAG
        continue

    elif lines[index].rstrip('\n') == '*END ZBG*':
        isStartTagSeen = False
        isEndTagSeen = True

        # We can continue as we don't want to insert the TAG
        continue

    # We should insert lines that are only within START ZBG and END ZBG
    if (isStartTagSeen) and (not isEndTagSeen):
        #print("1. Line:", lines[index].rstrip('\n'), ";")
        if (":" in lines[index]) and (not isTransStart):
            linesOrderDict[lines[index].split(':')[0]] = lines[index].split(':')[1].strip().rstrip('\n')
            continue

        elif lines[index].rstrip('\n').strip() == '==':
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

                linesOrderDict.setdefault(transType, []).append(tmpTransDict)
                continue
            else:
                isTransStart = True;
                continue

        if isTransStart == True:
            if lines[index].split(':')[0] == 'Description':
                transDescription = lines[index].split(':')[1].lstrip().rstrip('\n')
                
            elif lines[index].split(':')[0] == 'Type':
                transType = lines[index].split(':')[1].lstrip().rstrip('\n')
                
            elif lines[index].split(':')[0] == 'Origin':
                transOriginAccnt = lines[index].split(':')[1].split('/')[0].strip().rstrip('\n')
                transOriginRoute = lines[index].split(':')[1].split('/')[1].strip().rstrip('\n')
                
            elif lines[index].split(':')[0] == 'Destination':
                transDestAccnt = lines[index].split(':')[1].split('/')[0].strip().rstrip('\n')
                transDestRoute = lines[index].split(':')[1].split('/')[1].strip().rstrip('\n')
                
            elif lines[index].split(':')[0] == 'Amount':
                transAmount = (int(lines[index].split(':')[1].lstrip().rstrip('\n')) / 100)
                
print(linesOrderDict)
print(get_pretty_print(linesOrderDict))

