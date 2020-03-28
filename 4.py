"""
Goal: Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""
num = int(input("choose a number to divide: "))

listRange = list(range(1,num+1))

newList = []

for number in listRange:
    if num % number == 0:
        newList.append(number)

print(newList)
