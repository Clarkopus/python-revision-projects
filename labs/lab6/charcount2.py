"""
charcount1.py
counts occurrences of each character in a line of text
using ASCII codes as a method of counting
created by Guy Clark 27/12/16
"""

from sys import stdout
# User is asked to input a string of text into the application
# The application then will loop through every character and increment that characters ASCII value in the occs list
occs = [0] * 128
line = input("Please input a line of text\n")
for c in line :
    if ord(c)<=127 :
        occs[ord(c)] += 1

# User is then asked to enter the file name where that output will be saved
# The application then goes through a try loop to make sure that the application gives the correct errors
# Inside this try statement block the variable fOut will be used to store the information about what file is going
# to be used and what type of flag it has (in this case the write flag)
# If this fails the application will give out the error message and use the standard output instead
outFile = input("Enter the name of the output file: ")
try:
    fOut = open(outFile, 'w')
    print("output will be sent to output file -", outFile)

except:
    fOut = stdout
    print("File -", outFile, "Failed to be written to. Using standard output instead")

# The application then prints out all the information the user needs while still going through the same if statements
print("the word was:", line, file=fOut)
if occs[32] > 1 or occs[32] == 0:
    print("The line contained", occs[32], "spaces", file=fOut)
else:
    print("the line contained", occs[32], "space", file=fOut)

# Finally the application finish in a for loop to print all the characters in the user string
i = 33
while i<128 :
    if occs[i]!=0 :
        print("The number of occurrences of", chr(i), "was", occs[i], file=fOut)
    i = i+1

fOut.close()