for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))    #:number is spcifying field width with the variable value

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))    #< will align left > will align right ^ will centre values

print()

print("Pi is approx {0:12}".format(22 / 7))                 #Default for float is 15 decimals
print("Pi is approx {0:12f}".format(22 / 7))                #12 places
print("Pi is approx {0:12.50f}".format(22 / 7))             #precision of 50 decimals, 12 is ignored as width as cant fit 50 in 12
print("Pi is approx {0:52.50f}".format(22 / 7))
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:72.50f}".format(22 / 7))