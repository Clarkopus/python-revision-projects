"""
charcount1.py
counts occurrences of each character in a line of text
using ASCII codes as a method of counting
created by Guy Clark 27/12/16
"""

from sys import stdout

occs = [0] * 128
line = input("Please input a line of text\n")
for c in line :
    if ord(c)<=127 :
        occs[ord(c)] += 1
# Make the user store the name of the output file in a variable to use later
outFile = input("Enter the name of the output file: ")
# Try to open the document and set its flag to 'write' mode
try:
    fOut = open(outFile, 'w')
    print("output will be sent to output file -", outFile)
# If that fails print the error and use the standard output.
except:
    fOut = stdout
    print("File -", outFile, "Failed to be written to. Using standard output instead")

print("the word was:", line, file=fOut)
if occs[32] > 1 or occs[32] == 0:
    print("The line contained", occs[32], "spaces", file=fOut)
else:
    print("the line contained", occs[32], "space", file=fOut)

i = 33
while i<128 :
    if occs[i]!=0 :
        print("The number of occurrences of", chr(i), "was", occs[i], file=fOut)
    i = i+1

fOut.close()