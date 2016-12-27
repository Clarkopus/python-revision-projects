"""
charcount1.py
counts occurrences of each character in a line of text
using ASCII codes as a method of counting
created by Guy Clark 27/12/16
"""


occs = [0] * 128
line = input("Please input a line of text\n")
for c in line :
    if ord(c)<=127 :
        occs[ord(c)] += 1

if occs[32] > 1 or occs[32] == 0:
    print("The line contained", occs[32], "spaces")
else:
    print("the line contained", occs[32], "space")

i = 33
while i<128 :
    if occs[i]!=0 :
        print("The number of occurrences of", chr(i), "was", occs[i])
    i = i+1
