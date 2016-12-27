"""
charcount1.py
counts occurrences of each character in a line of text
using ASCII codes as a method of counting
created by Guy Clark 27/12/16
"""

# set up list with 128 ints, all initially 0
# For loop to loop through the user string and record what characters have been found using ASCII code numbers
# If the character "c" is smaller than the int value 127 then increment that ASCII code in the list

occs = [0] * 128
line = input("Please input a line of text\n")
for c in line :
    if ord(c)<=127 :
        occs[ord(c)] += 1

# As a note, the ASCII code 32 has been stored so we can easily identify spaces
# Since printable ASCII codes start at 33 we start our loop at the value of the variable i (33)
# loop through until you reach the value 128
# if the variable in the list doesn't equal 0 (if it has been used) print outcome
# Increment i to continue the loop

if occs[32] > 1 or occs[32] == 0:
    print("The line contained", occs[32], "spaces")
else:
    print("the line contained", occs[32], "space")

i = 33
while i<128 :
    if occs[i]!=0 :
        print("The number of occurrences of", chr(i), "was", occs[i])
    i = i+1
