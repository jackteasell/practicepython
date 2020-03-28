"""
Practicepython.org problem #1
Goal: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
import datetime
name = input("What is your name?")
age = int(input("What is your age?"))
today = datetime.datetime.now()
print("You will be 100 years old in the year: " , 100+((today.year) - age))



