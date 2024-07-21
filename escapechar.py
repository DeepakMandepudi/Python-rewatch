splitstring = "This is the \nexample of \nsplit string"
print(splitstring)

tabbedstring = "10\t11\t12\t13\t14\t15"
print(tabbedstring)

print("he said 'today' is his bday 'e's uh,..")

# we get error if we run this line:
# print('he said "today" is his bday 'e's uh,..')
#instead we use '\'

print('he said "today" is his bday "No, no \'e\'s uh,..".')
#or
print("he said 'today' is his bday \"No, no 'e's uh,..\".")

print("he said \"today\" is his bday \"No, no 'e's uh,..\".")
#or we can use triple quotes instead.
print("""he said "today" is his bday "No, no 'e's uh,..".""")

anotherstringsplit = ("""This line has been
split into
several multiple
lines""")
print(anotherstringsplit)

# add space '\' after each line and lets make above string in one line
anotherstringsplit = ("""This line has been \
split into \
several multiple \
lines""")
print(anotherstringsplit)

#what if we use the above method for line 19? we get the same in one line :)
print("""he said "today" is his bday \
"No, no 'e's uh,..".""")

# How to use \n, \t in the line as the string instead of escape characters? lets see below example

#print("c:\users\tailor\notebook.txt")
#ofcourse you'll get error.
#There are 2 methods to overcome
#1. by putting other backslash before initial one '\\'
print("c:\\users\\tailor\\notebook.txt")

# 2.'r' at the prefix: raw string's are intended to use with regular expressions
print(r"c:\users\tailor\notebook.txt")

#in general better use 1st method to escape backslash character