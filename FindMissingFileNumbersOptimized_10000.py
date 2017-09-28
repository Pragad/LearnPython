#! /usr/bin/env/python
import mmap
import re

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    filePath = input("Enter file path: ")
    endFileNum = input("Enter end file number: ")
    filesMissing = []
    filesPresent = []
    filesMissingCount = 0
    filesPresentCount = 0
    present_ones = set()

    #>>> myRegex=r'(.*)file_(.)' + re.escape(str(TEXTTO)) + r'\.txt'
    #>>> searchObj=re.search(myRegex,line)
    #>>> print(searchObj)
    #<_sre.SRE_Match object; span=(0, 15), match='asdffile__0.txt'>

    # https://stackoverflow.com/questions/46476537/python-how-to-search-a-string-in-a-large-file
    my_regex = re.compile('.*file_.(\d+)\.txt.*')
    for line in open(filePath):
        match = my_regex.match(line)
        if match:
            present_ones.add(int(match.group(1)))

    for x in range(int(endFileNum)):
        if x not in present_ones:
            filesMissing.append(x)
            filesMissingCount += 1
        else:
            filesPresent.append(x)
            filesPresentCount += 1
    #print("Files Present: ")
    #print(filesPresent)
    print("Files Present Count: %d" % filesPresentCount)
    print("Files Missing: ")
    print(filesMissing)
    print("Files Missing Count: %d" % filesMissingCount)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

