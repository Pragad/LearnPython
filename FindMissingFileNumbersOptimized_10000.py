#! /usr/bin/env/python
import mmap
import re

#-------------------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------------------
def main():
    filePath = input("Enter file path: ")
    endFileNum = input("Enter end file number: ")
    filesMissingCount = 0
    filesPresentCount = 0
    fileNumbersMissing = set()
    filesNumbersPresent = set()
    fileNamesPresent = set()

    #>>> myRegex=r'(.*)file_(.)' + re.escape(str(TEXTTO)) + r'\.txt'
    #>>> searchObj=re.search(myRegex,line)
    #>>> print(searchObj)
    #<_sre.SRE_Match object; span=(0, 15), match='asdffile__0.txt'>

    # https://stackoverflow.com/questions/46476537/python-how-to-search-a-string-in-a-large-file
    my_regex = re.compile('.*file_.(\d+)\.txt.*')
    for line in open(filePath):
        match = my_regex.search(line)
        if match:
            filesNumbersPresent.add(int(match.group(1)))
            start = line.find('file_')
            end = line.find('txt', start)
            fileNamesPresent.add(line[start:end+3])

    for x in range(int(endFileNum)):
        if x not in filesNumbersPresent:
            fileNumbersMissing.add(x)
            filesMissingCount += 1
        else:
            filesPresentCount += 1
    print("Files Present: ")
    print(fileNamesPresent)
    #print(filesNumbersPresent)
    print("Files Present Count: %d" % filesPresentCount)
    print("Files Missing: ")
    print(fileNumbersMissing)
    print("Files Missing Count: %d" % filesMissingCount)

#-------------------------------------------------------------------------------------------
# Start Main
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

