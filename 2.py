"""
Goal: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
"""

num = int(input("Even or odd? Pick a number: "))

if (num%2 == 0):
    print("The number is even")
else:
    print("The number is odd")