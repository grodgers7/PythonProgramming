shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# for index in range(6):
# for index in range(len(shopping_list)):             # index is a new item created, len function gets the length of
#     if shopping_list[index] == item_to_find:        # the list (6) and stores 0-6 as the range up to but not including 6
#         found_at = index
#         break                                       # adding a break point because after running the debugger we can see
#                                                     # code continues to run in the for loop even though spam is found


# more simplified version of the above lines, showing how strongly written python is
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:                            # checking that item was found, if not found print item & message
    print("{} found at position {}".format(item_to_find, found_at))
else:
    print("{} not found".format(item_to_find))
