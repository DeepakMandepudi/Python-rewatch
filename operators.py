

#Integers
print(123)

#Commonly when we write large numbers,
# at least in the UK or in the US, we'd like to put commas in between the thousands.
# So when we think of large numbers with these commas in between to split it into
# an easier to understand number. In Python,
# we can replace those commas simply with underscores and it will be interpreted
# by the computer as if you had written this.
# So the computer actually removes those underscores and ignores it.
print(123456789)
print(123_456_789)

#Boolean
#"False" is a String, not a boolean. Booleans are either True or False.
# Booleans don't have quotation marks around them,
# otherwise it would turn them into a String. So it should be bool = False

a=12
b=3
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # print float
print(a // b)   # integer division. roundup to minus infinity
print(a % b)    # modulo : remainder after integer division
print(a ** b)   #exponential: a to the power b (12^3)

print( 7 / 4)        #gives float number
print(round(7/4))    #round off to nearest int (1.66 ~ 2)
print(round(7/4, 3)) #round it to 3 decimal places
print(round(2.45637, 3))
print(round(7/5), 3) #this is different. it rounds 7/4 and print that value space 3. beware with code

#order of operations: PEMDAS () ** * / + -
#But [(), **] [*, /] [+,-] have same level of precedence
#go from LEFT TO RIGHT. if we have /, * then what ever operand comes first do that.

#  TASK 1
#Write a program that adds the digits in a 2 digit number.
#e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

first_digit=int(two_digit_number [0])
second_digit=int(two_digit_number[1])

print(first_digit + second_digit)

# TASK 2

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#BMI = Weight (kg)/height^2 (m^2)
#NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.
# See examples below.
#Example Input 1
#1.75
#80
#means: weight = 80 and height = 1.75

#Example Output 1
# 26
#Since: 80 ÷ (1.75 x 1.75) = 26.122448979591837


#Solution: in python, check type of the variable every time before starting the code.

height = input()
weight = input()

# initially in the task, height and weight are in string type. so changing according to input
new_height= float(height)
new_weight= int(weight)
#converted according to task.
BMI = (new_weight/(new_height ** 2))
print(int(BMI))

