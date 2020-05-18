# list = ["1. Learn Python", "2. Learn Java", "3. Go swimming", "4. Have dinner", "5. Go to bed", "0. Exit"]
#
# answer = ""
# print("Please choose your option from the list below:")
# for i in range(len(list)):
#     print(list[i])
#     while answer not in list:
#         continue
#     if
# answer = input()
# if answer in list:
#     print("You selected {}".format(answer))

# choice = "-"
# while True:
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
#
#     choice = input()

choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
