#! /usr/bin/env/python
import mmap
import re

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    filePath = input("Enter file path: ")
    endFileNum = input("Enter end file number: ")
    print(filePath)
    print(endFileNum)
    filesMissing = []
    filesPresent = []
    f = open(filePath, 'rb', 0)
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for x in range(int(endFileNum)):
        searchString = "file" + str(x).zfill(3) + ".txt"
        b = bytes(searchString, 'utf-8')
        if re.search(b, s):
            filesPresent.append(searchString)
        else:
            filesMissing.append(searchString)
    print(filesPresent)
    print(filesMissing)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

