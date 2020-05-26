# jabber = open("/Users/grodgers/desktop/sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()
#
# with open("/Users/grodgers/desktop/sample.txt", 'r') as jabber:     # with in this instance handles closing the file
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("/Users/grodgers/desktop/sample.txt", 'r') as jabber:
#     line = jabber.readline()        # readline() function will only read if there is data in the file, reads file line by line
#     while line:
#         print(line, end='')
#         line = jabber.readline()
#         # while there is a line in the file to be printed this wile loop will continue
#         # until there is nothing left to print

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()      # this returns it as a list, reads whole file at beginning
print(lines)

for line in lines:
    print(line, end='')
