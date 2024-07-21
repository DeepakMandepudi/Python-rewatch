#Strings
print("hello")
print("123", '12')
#print(123 + "hey") error bcz left operand is int, right is str
# *** INDEXING ***
print("Hello"[0]) #[] starts with 0.
print("12345", "deepak" [4])
word = "Norwegian Blue"

print(f"{word [3]}\n{word [4]}\n\n{word [3]}\n{word [6]}\n{word [8]}")
#instead of \n\n, we can also use index 9. bcz its space in index 9 :)
print()
# NEGATIVE INDEXING
print(word [-1])
print(f"{word [-8]} {word [-4]} {word [-3]}")
#Another way is we can subtract the normal index to total word count like to get w, do 3-14 or just -11 bot are same

print(word[3 -14]) # or word [-11] both are same
print(word [4 -14])

#  **** SLICING (START, STOP, STEP) ******
# START
#Well we can get the first word by getting the slice from position 0,
# and it extends up to (but not including) right side index/position.
print(word [4:11])
#even if we do not include start index, it automatically begins from 0th index. so bopth 26, 27 lines are crct
print(word [0:9])
print(word [:9])
print(word [10:14])
# STOP
#if we leave the stop value, its same like line 28. but here we give where to start and end at end of last char
print(word[3:])

print(word[:5] + word[5:]) #print from start to 4th index (up to 5 but not 5). and concatinate and 5th to end.

print(word[:])
#print from start and end at last char (complete string printed out)

#   NEGATIVE SLICING
print(word[-4:2]) #print nothing bcz we cannot go backwards from the starting position
#the start value must be greater than the stop value
#instead we can write like this -4:-2
print(word[-4:-2])
#this prints from index -4 and that's B, up to(but not including)the second-to-last character in the string, which is u.
print(word[-4:12])
#prints the same thing but this time it's interpreted as from index -4, up to but not including index position 12.
print(word[-4:-8]) #nothing
print(word[-14:-8])


# STEP
#word = "Norwegian Blue"
print(word[0:6:2]) #NRE
# So the slice starts at index 0, which is the capital N,
# extends all the characters up to (but not including) index 6, which is the i,
# we step through the sequence in steps of 2. {2 steps: N to R, R to E}
# E to I is not possible bcz we said upto 6th index but not 6th.

print(word[2:8:3])
print(word[2:9:3])

#  BACKWARD SLICING

letter ="abcdefghijklmnopqrstuvwxyz"
print(letter[25:0:-1])
#Because we're using a negative step (-1),
# the start value must be greater than the stop value

# Our slice starts at index position 25 (z), and it extends down to index position 0,
# but doesn't include the character at that position (a).
# We're stepping by -1, which produces all the letters from z down to b
print(letter[25:0:-2])

# Remember that negative stop values count backwards from the end of the sequence.
print(letter[25:-1:-2])
# Minus 1 means the last character in the string, which means we've requested a slice that extends from the z up to,
# but not including, the z, and therefore we get nothing.
print(letter[25:0:-1])
print(letter[25::-1])
#Python will default to the start or end of the sequence,
# if we don't specify start or stop values. So it's clever enough to work out that it should
# reverse the defaults when we're using a negative step.

# **** With a negative step, the start value will default to the end of the string,
# and the stop value defaults to the start of the string.
# That means we can ommit our start value as well.

print(letter[::-1])

#I can say about slicing backwards. Just use a negative step and make sure the start value is greater than the stop value.

print(letter[25:17:-1])
print(letter[:-9:-1])
print(letter[25:-9:-1])
print(letter[25:-2:-1])
print(letter[0:1:1])