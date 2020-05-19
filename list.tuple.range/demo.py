# a = b = c = d = 12
# print(c)
# a, b = 12, 13
# print(a, b)
#
# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))


imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for i in tracks:
    print("\t", i)
