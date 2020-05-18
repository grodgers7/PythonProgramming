# string = "1234567890"
#
# for char in string:
#     print(char)
#
# # my_iterator = iter(string)
# # print(my_iterator)
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
#
# for char in iter(string):
#     print(char)

my_list = [0, 1, 2, 3, 4, 5]
my_iterator = iter(my_list)
for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)
