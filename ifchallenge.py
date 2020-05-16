# Make a program to take a name and age of a user and validate if they are suitable for 18-30 holiday club

name = input("What is your name? ")
age = int(input("What is your age? "))

if 18 <= age <= 30:
    print("Welcome on holiday {}".format(name))
else:
    print("Sorry you do not meet the criteria")