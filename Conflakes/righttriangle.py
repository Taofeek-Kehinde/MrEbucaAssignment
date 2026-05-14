"""
Read number from user

Loop from 1 to number

For each row i, print i stars separated by space

"""

number = int(input("Enter a number: "))
for index in range(1, number + 1):
    print("* " * index)

