split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
#or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# triple quotes allows us to not escape any characters. Makes a string easier read in the code
print("""The pet shop owner said "No, no, \
 'e's uh,...he's resting".""")

another_split_string = """This string has been
split over
several
lines."""
# When adding a \ to the end of a split string it formats it as a line ending but prints as an entire string. Good for code visibility and no
# horizontal scrolling
another_split_string1 = """This string has been \
split over \
several \
lines."""

print(another_split_string)
print(another_split_string1)
#can escape a backslash with another back slash
#r is for a raw string but the first method is preferable

print("C:\\Users\\gavinrodgers\\notes.txt")
print(r"C:\Users\gavinrodgers\notes.txt")