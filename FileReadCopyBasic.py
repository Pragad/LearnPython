# !/usr/bin/python

import os, sys, random
import shutil
# https://stackoverflow.com/questions/489861/locking-a-file-in-python
#from filelock import FileLock
#https://pythonhosted.org/lockfile/lockfile.html
from lockfile import LockFile

# Open a file
fd = os.open("foo.txt", os.O_RDWR)
	
# Reading text
ret = os.read(fd, 12)
print ret

#assert os.path.exists("foo1.txt")

#with FileLock("myfile.txt"):
#    # work with the file as it is now locked
#    print("Lock acquired.")

lock = LockFile("myfile.txt")
with lock:
    print lock.path, 'is locked.'

with open("foo.txt", "r") as f:
    f.seek(135);
    print f.read(6);

    f.seek(0, 2)
    eof = f.tell()
    print eof

    offset = random.randint(0, eof)
    numBytes = random.randint(0, eof - offset)
    print "Offset=%d numBytes=%d" % (offset, numBytes)
    f.seek(offset)
    print f.read(numBytes)

    shutil.copyfile("foo.txt", "foo.txt" + ".old")
    #shutil.copytree("bar", "bar" + ".old")

# Generate Random dir inside a dir
def __newname():
    random = random.Random(seed)
    l = random.randint(1, 16)
    n = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in xrange(l)]
    return "".join(n)

def __newsubpath(path):
    while True:
        p = os.path.join(path, __newname())
        if not os.path.exists(p):
            return p

def __getdir_recurse(path):
    try:
        n = random.choice(os.listdir(path))
    except:
        return path
    p = os.path.join(path, n)
    if os.path.isdir(p):
        return __getdir_recurse(p)
    else:
        return path

def __getdir(path):
    p = __getdir_recurse(path).replace(path, '')
    print "new path:" , p
    parts = p.split(os.sep)
    print "parts1:" , parts
    r = random.randint(1, len(parts))
    print "rand:" , r
    parts = parts[0:r]
    print "parts2:" , parts
    return os.path.join(path, *parts)

def __getsubpath(path):
    try:
        n = random.choice(os.listdir(path))
    except:
        return path
    return os.path.join(path, n)

basepath = "/Users/pragad/ItsMine/Dev_Git/LearnPython/deleteThisDir"

#basepath = __newsubpath(__getdir(basepath))
print __getdir(basepath)

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

# This get a deeper directory path
def getdir_recurse(path):
    try:
        dirent = list(listdir_nohidden(path))
        print dirent
        n = random.choice(dirent)
        print n
    except Exception as e:
        print e

newpath = "/Users/pragad/ItsMine/Dev_Git/LearnPython"
getdir_recurse(newpath)

def listfiles(path):
    fullFilesList = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    filesList = [f for f in fullFilesList if not f.startswith('.')]
    return filesList

print listfiles(newpath)
