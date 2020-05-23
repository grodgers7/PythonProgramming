my_list = ["a", "b", "c", "d"]
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "123456789"

newString = ''
for c in my_list:
    newString += c + ", "           # output will have a trailing comma which is not what we really want
print(newString)
newString = ", ".join(letters)
print(newString)

# same thing but using joing to add onto the beginning of text
newString = "  ".join(numbers)   # will append the numbers to the beginning

print(newString)
