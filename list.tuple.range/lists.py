# ipAddress = input("Please enter and IP address: ")
# print(ipAddress.count("."))
# parrot_list = ["non pinin", "no more", "a stiff", "bereft of life"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# # numbers.sort()            # the next two lines do the exact same thing
# print(sorted(numbers))
# print(numbers)
##################################
# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
#
# another_even = list(even)
#
# print(another_even)
#
# print(another_even == even)         # should return a boolean
#
# even.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value, end="")
