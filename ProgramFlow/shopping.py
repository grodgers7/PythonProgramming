shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        # continue                    # if item in the list continue to top of loop not exectuing any more code
        break                       # if item in the list exit from the for loop

    print("Buy " + item)
