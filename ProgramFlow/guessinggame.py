answer = 5

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print("You got it first time")

# Adding a second guess
print("What is your name? ")
name = input()
print("Hi {0}, please guess a number between 1 and 10: ".format(name))
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be higher
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be higher
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry wrong answer")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry wrong answer")
# else:
#     print("You got it first time")