import random

highest = 10
answer = random.randint(1, highest)

print("What is your name? ")
name = input()
guess = 0             # initialise to any number that wil not equal the answer
print("Hi {0}, please guess a number between 1 and {1}: ".format(name, highest))


while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be lower
            print("Please guess lower")
if guess == 0:
    print("Game Over")



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