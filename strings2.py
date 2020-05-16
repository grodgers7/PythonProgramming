#                   11111
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)
#
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
#Printing with negative index numbers
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

#Slicing
print(parrot[0:9])    #Printing from index 0 upto but NOT including index 9 i.e 9 is not included
print(parrot[:9])
print(parrot[9:])
print(parrot[:])

#slicing with negative index
print(parrot[-4:-2])
print(parrot[-4:12])    #Mixture of both positve and negative

#Slicing with a step
print(parrot[0:6:2])    #2 is the step so every second character is omitted
print(parrot[0:6:3])





