# print(range(100))
#
# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)
#
# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals)
#
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)             # range of numbers from 1 to 10000, skipping every second number to make them odd
# print(odd)
#
# print(odd[985])                      # print the number from the 985th index
#
#
# sevens = range(7, 1000000, 7)
# x = int(input("Pkease enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by 7".format(x))
# else:
#     print("{} is not divisible by 7".format(x))
#
# print(small_decimals)
#
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))

### showing how range can be split two ways via index and

decimals = range(0, 100)
my_range = decimals[3:40:3]         # using the slice method
print(decimals)
print(my_range)

print(range(3, 40, 3))
print(my_range == range(3, 40, 3))
