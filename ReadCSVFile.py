#! /usr/bin/env/python
import csv
import time
import pandas
from collections import defaultdict

orderBaseDict = {}
orderIdDict = defaultdict(list)
prodIdDict = {}
deptIdDict = {}
allDetailsList = []
filename = 'order_products__prior.csv'
filename2 = 'departments.csv'
csv_delimiter = ','

print(time.strftime("%Y-%m-%d %H:%M:%S"))
count1 = 0
count2 = 0
with open(filename2) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #has_header = csv.Sniffer().has_header(csvfile.read(1024))
    #if has_header:
    #    next(readCSV)
    for row in readCSV:
        count1 += 1
        #prodId = row[0]
        #prodName = row[1]
        #deptId = row[3]
        #prodIdDict[prodId] = (prodName, deptId)
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print("Num rows: " + str(count1))

def open_with_pandas_read_csv(filename):
    df = pandas.read_csv(filename, sep=csv_delimiter)
    data = df.values
    prodList = []
    print(df.loc[df['order_id'] == 2].values[0])
    for row in df.loc[df['order_id'] == 2].values:
        prodList.append(row[1])
    print(prodList)
open_with_pandas_read_csv(filename)
print(time.strftime("%Y-%m-%d %H:%M:%S"))
