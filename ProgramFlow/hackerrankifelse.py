n = int(input("Enter a number: "))
if 1<= n <=100:
    if n %2 != 0:
        print("Weird")
    else:
        if n > 20:
            print("Not Weird")
        elif n in range(2, 6):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")
else:
    print("Number not in range")