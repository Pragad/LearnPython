# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# This script runs "git pull origin master" on all directories under DEV_GIT

#http://stackoverflow.com/questions/431684/how-do-i-cd-in-python
import os
from subprocess import call

myPwd = os.getcwd()
print("\n\n" + myPwd)

os.chdir("C:\PRAGADHE\DEV_GIT\Algos")
print("\n\n" + os.getcwd())
os.system('git status')

os.chdir("C:\PRAGADHE\DEV_GIT\LearnCpp")
print("\n\n" + os.getcwd())
os.system('git status')

os.chdir("C:\PRAGADHE\DEV_GIT\LearnPython")
print("\n\n" + os.getcwd())
os.system('git status')

os.chdir("C:\PRAGADHE\DEV_GIT\LearnJava")
print("\n\n" + os.getcwd())
os.system('git status')

os.chdir("C:\PRAGADHE\DEV_GIT\OtherLearnings")
print("\n\n" + os.getcwd())
os.system('git status')

os.chdir(myPwd)
print("\n\n" + os.getcwd())