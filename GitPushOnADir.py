# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# This script runs "git pull origin master" on all directories under DEV_GIT

#http://stackoverflow.com/questions/431684/how-do-i-cd-in-python
#TODO: 
# 1. Get Path from User AND
# 2. Get "commit message" from user
# 3. Perform the following commands
#    a. goto the given path
#    b. git status
#    c. git add --all
#    d. git commit -m $msg
#    e. git push origin master

import os
from subprocess import call

myPwd = os.getcwd()
print("\n\n" + myPwd)

os.chdir("/Users/pragadh/PRAGADH/DEV/Algos")
print("\n\n" + os.getcwd())
call(["git status"], shell=True)

os.chdir(myPwd)
print("\n\n" + os.getcwd())
