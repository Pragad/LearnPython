#! /usr/bin/env/python
import os

baseFileName = raw_input("Enter base folder name: ")

myPwd = os.getcwd()

for index in range(0, 50):
    if not os.path.exists(baseFileName + str(index)):
        os.makedirs(baseFileName + str(index))

        os.chdir(myPwd + '/' + baseFileName + str(index))
        myPwd = os.getcwd()

        for fileNameIdx in range(0, 100):
            fileOpen = open(baseFileName + str(index) + "_" + str(fileNameIdx), "w+")
            fileOpen.write("abcdefghijklmnopqrstuvwxy")
            fileOpen.close
