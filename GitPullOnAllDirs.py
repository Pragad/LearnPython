# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# This script runs "git pull origin master" on all directories under DEV_GIT

#http://stackoverflow.com/questions/431684/how-do-i-cd-in-python
#TODO: 
# 1. Get Path from User
# 2. Perform "git pull origin master" on the path
import os
from subprocess import call

myPwd = os.getcwd()
print("\n\n" + myPwd)

os.chdir("/Users/pragadh/PRAGADH/DEV/Algos")
print("\n\n" + os.getcwd())
call(["git pull origin master"], shell=True)

os.chdir("/Users/pragadh/PRAGADH/DEV/LearnCpp")
print("\n\n" + os.getcwd())
call(["git pull origin master"], shell=True)

os.chdir("/Users/pragadh/PRAGADH/DEV/LearnPython")
print("\n\n" + os.getcwd())
call(["git pull origin master"], shell=True)

os.chdir("/Users/pragadh/PRAGADH/DEV/LearnJava")
print("\n\n" + os.getcwd())
call(["git pull origin master"], shell=True)

os.chdir("/Users/pragadh/PRAGADH/DEV/OtherLearnings")
print("\n\n" + os.getcwd())
call(["git pull origin master"], shell=True)

os.chdir(myPwd)
print("\n\n" + os.getcwd())


