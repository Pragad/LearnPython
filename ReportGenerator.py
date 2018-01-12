#! /usr/bin/env/python
# Author Pragad Thirumurthi

# Sort CSV files using bash sort
# sort --field-separator=',' --key=5,6 orders.csv > orders_sorted.csv

# This program requires following csv files to be present
# products.csv, departments.csv, order_products__train.csv, orders_sorted.csv

# The program does not use order_products__prior.csv right now

import csv
from collections import defaultdict

orderBaseDict = {}
orderIdDict = defaultdict(list)
prodIdDict = {}
deptIdDict = {}
allDetailsList = []

df = pandas.read_csv('order_products__prior.csv', sep=',')
print(df.loc[df['department_id'] == 15].values[0][1])

with open('products.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    if has_header:
        next(readCSV)
    for row in readCSV:
        prodId = row[0]
        prodName = row[1]
        deptId = row[3]
        prodIdDict[prodId] = (prodName, deptId)

with open('departments.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # Couldn't sniff header in the csv file
    #has_header = csv.Sniffer().has_header(csvfile.read(1024))
    #if has_header:
    #    next(readCSV)
    for row in readCSV:
        if row[0] == "department_id":
            continue
        deptId = row[0]
        dept = row[1]
        deptIdDict[deptId] = dept

# Also read from other_products__prior.csv
with open('order_products__train.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    has_header = csv.Sniffer().has_header(csvfile.read(1024))
    if has_header:
        next(readCSV)
    for row in readCSV:
        orderId = row[0]
        prodId = row[1]
        orderIdDict[orderId].append(prodId)

with open('orders_sorted.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # Couldn't sniff header in the csv file
    #has_header = csv.Sniffer().has_header(csvfile.read(1024))
    #if has_header:
    #    next(readCSV)
    oldDow = None
    oldHod = None
    oldUserId = None
    totalCount = 0
    frozen = 0
    other = 0
    bakery = 0
    produce = 0
    alcohol = 0
    international = 0
    beverages = 0
    pets = 0
    dryGoodsPasta = 0
    bulk = 0
    personalCare = 0
    meatSeafood = 0
    pantry = 0
    breakfast = 0
    cannedGoods = 0
    dairyEggs = 0
    household = 0
    babies = 0
    snacks = 0
    deli = 0
    missing = 0

    for row in readCSV:
        orderId = row[0]
        userId = row[1]
        table = row[2]
        order_num = row[3]
        dow = row[4]
        hod = row[5]

        prodList = []
        if table == "test":
            continue
        elif table == "prior":
            for row in df.loc[df['order_id'] == orderId].values:
                prodList.append(row[1])
        elif table == "train":
            prodList = orderIdDict[orderId]
        #print("OrderID: " + str(orderId) + "; dow: " + dow + "; hod: " + hod + "; user: " + userId)
        for prod in prodList:
            deptId = prodIdDict.get(prod, None)
            if deptId is None:
                continue
            deptId = deptId[1]
            deptName = deptIdDict[deptId]

            if oldDow is None or oldDow == dow:
                if oldHod is None or oldHod == hod:
                    #if userId == oldUserId:
                    # Dummy if
                    if False:
                        continue
                    else:
                        totalCount += 1
                        if deptName == "frozen":
                            frozen += 1
                        elif deptName == "other":
                            other += 1
                        elif deptName == "bakery":
                            bakery += 1
                        elif deptName == "produce":
                            produce += 1
                        elif deptName == "alcohol":
                            alcohol += 1
                        elif deptName == "international":
                            international += 1
                        elif deptName == "beverages":
                            beverages += 1
                        elif deptName == "pets":
                            pets += 1
                        elif deptName == "dry goods pasta":
                            dryGoodsPasta += 1
                        elif deptName == "bulk":
                            bulk += 1
                        elif deptName == "personal care":
                            personalCare += 1
                        elif deptName == "meat seafood":
                            meatSeafood += 1
                        elif deptName == "pantry":
                            pantry += 1
                        elif deptName == "breakfast":
                            breakfast += 1
                        elif deptName == "canned goods":
                            cannedGoods += 1
                        elif deptName == "dairy eggs":
                            dairyEggs += 1
                        elif deptName == "household":
                            household += 1
                        elif deptName == "babies":
                            babies += 1
                        elif deptName == "snacks":
                            snacks += 1
                        elif deptName == "deli":
                            deli += 1
                        elif deptName == "missing":
                            missing += 1
                        oldHod = hod
                        oldDow = dow

                # Once we go to next hour
                else:
                    oldHod = hod
                    oldUserId = userId
                    frozen  = frozen / totalCount * 100
                    other  = other / totalCount * 100
                    bakery  = bakery / totalCount * 100
                    produce  = produce / totalCount * 100
                    alcohol  = alcohol / totalCount * 100
                    international  = international / totalCount * 100
                    beverages  = beverages / totalCount * 100
                    pets  = pets / totalCount * 100
                    dryGoodsPasta  = dryGoodsPasta / totalCount * 100
                    bulk  = bulk / totalCount * 100
                    personalCare  = personalCare / totalCount * 100
                    meatSeafood  = meatSeafood / totalCount * 100
                    pantry  = pantry / totalCount * 100
                    breakfast  = breakfast / totalCount * 100
                    cannedGoods  = cannedGoods / totalCount * 100
                    dairyEggs  = dairyEggs / totalCount * 100
                    household  = household / totalCount * 100
                    babies  = babies / totalCount * 100
                    snacks  = snacks / totalCount * 100
                    deli  = deli / totalCount * 100
                    missing  = missing / totalCount * 100
                    finalValuesList = [frozen, other, bakery, produce, alcohol, international, beverages, pets, dryGoodsPasta, bulk, personalCare, meatSeafood, pantry, breakfast, cannedGoods, dairyEggs, household, babies, snacks, deli, missing]
                    finalValuesList.sort(reverse=True)
                    print("Day " + dow + ":")
                    print("\t Hour " + hod + ":")
                    print("\t\t" + str(finalValuesList))
            else:
                oldDow = dow
