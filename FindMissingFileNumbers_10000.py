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

    #>>> myRegex=r'(.*)file_(.)' + re.escape(str(TEXTTO)) + r'\.txt'
    #>>> searchObj=re.search(myRegex,line)
    #>>> print(searchObj)
    #<_sre.SRE_Match object; span=(0, 15), match='asdffile__0.txt'>

    for x in range(int(endFileNum)):
        myRegex = r'(.*)file(.*)' + re.escape(str(x)) + r'\.txt'
        myRegex = bytes(myRegex, 'utf-8')
        if re.search(myRegex, s):
            filesPresent.append(x)
        else:
            filesMissing.append(x)
    print(filesPresent)
    print(filesMissing)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

