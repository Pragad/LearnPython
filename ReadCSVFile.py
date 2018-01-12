#! /usr/bin/env/python
import csv
import time
from collections import defaultdict

orderBaseDict = {}
orderIdDict = defaultdict(list)
prodIdDict = {}
deptIdDict = {}
allDetailsList = []

print(time.strftime("%Y-%m-%d %H:%M:%S"))
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
print(time.strftime("%Y-%m-%d %H:%M:%S"))
