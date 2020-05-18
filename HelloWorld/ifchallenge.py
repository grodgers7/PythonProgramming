# Make a program to take a name and age of a user and validate if they are suitable for 18-30 holiday club

# name = input("What is your name? ")
# age = int(input("What is your age? "))
#
# if 18 <= age <= 30:
#     print("Welcome on holiday {}".format(name))
# else:
#     print("Sorry you do not meet the criteria")

# for i in range(21):
#     if i > 0 and i % 3 != 0 and i % 5 != 0:
#         print(i)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
