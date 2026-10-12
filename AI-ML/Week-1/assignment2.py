# List 
#Sum of Numbers
# Find the sum of all numbers:

# numbers = [5, 10, 15, 20]

# sum = sum(numbers)
# print(sum)

# Find Maximum
# Find the largest number in:

# numbers = [12, 45, 7, 23, 89]

# numbers.sort(reverse = True)
# print(numbers[0])

# numbers = [12, 45, 7, 23, 89]

# maximum = max(numbers)

# print("The largest number is", maximum)

# Tuple
# Count how many times 2 appears:

# numbers = (2, 4, 2, 6, 2, 8)
# count = numbers.count(2)
# print("Number of time 2 appears is ", count)

# Dictionary

# Simple Marks Dictionary
# Create:

# marks = {
#     "English": 75,
#     "Math": 85,
#     "Python": 90
# }

# # Print the marks in Python.

# marks["English"] = 90

# print(marks)

# for key,value in marks.items():
#     print(key)

# Set
# Difference
# Find the elements that are in A but not in B:

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# C = A.difference(B)

# print(C)


# IF-Condition
# 1-Write a Python program that takes a number from the user and checks whether it is positive or negative.

# num = float(input("Enter a nmumber: "))

# if num > 0:
#     print("Number is positive")
# else:
#     print("Number is Negative")

# 2-Write a program that takes a number and checks whether it is even or odd.

# num = int(input("Enter a Nmumber: "))

# if num % 2 == 0:
#     print("The number is Even")
# else:
#     print("The number is Odd")

# 3-Write a program that asks the user's age. If the age is 18 or greater, print "You are eligible to vote".

# age = float(input("Enter ypur age: "))

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# 4-Write a program that takes the temperature. If the temperature is greater than 30, print "It is hot".

# temp = float(input("Enter temperature: "))
# if temp > 30:
#     print("It is hot today.")
# else:
#     print("Weather is Normal today")

#5-Write a program that takes two numbers and prints the number that is greater.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("First number is greater.")
elif num2 > num1:
    print("Second number is greater.")
else:
    print("Both are equal.")