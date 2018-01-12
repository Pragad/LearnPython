source = "/Users/pragad/ItsMine/Dev_Git/LearnPython/TestFileSystem/1/"
target = "/Users/pragad/ItsMine/Dev_Git/LearnPython/TestFileSystem/2/"
#pat = "-x \".*\""
#bashCommand = 'diff -x ".*" -r ' + source + ' ' + target
#bashCommand = "diff " + pat + " -r " + source + " " + target
bashCommand = "diff -x .* -r " + source + ' ' + target
print bashCommand

import subprocess

process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
if output:
    print "Directories do not match: " + output
else:
    print "Directories match"
