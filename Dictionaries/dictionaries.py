fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
#
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# del fruit["grape"]
# print(fruit)
# # del fruit           # removes the dictionary and
# print("=" * 40)
# fruit.clear()
print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# for snack in fruit:
#     print(fruit[snack])

ordered_key = list(fruit.keys())        # creating a list with the dictionary as thi sis the only way to sort it right now dure to an error in python upto version 3.6
ordered_key.sort()
ordered_key = sorted(list(fruit.keys()))
for f in ordered_key:
    print(f + " - " + fruit[f])
