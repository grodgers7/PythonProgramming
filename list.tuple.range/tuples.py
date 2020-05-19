# ordered set of data, immutable, cannot be edited e.g. cannot append to or change
# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))
# tuples can hold mixed data types, without error
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # trying to edit a tuple like you would replace items in a list will return an error
# # metallica[0] = "Master of Puppets"
#
# # can change with slicing as the example below shows
# imdelda = imelda[0], "Imelda May", imelda[2]
# print(imdelda)

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
# metallica2[0] = "Master of Puppets"                       #replacing a vlue in a list
# print(metallica2)

# unpacking the tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)