#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards =letters[25::-1]
print(backwards)

backwards = letters[::-1]    #known as a python idium (Printing backwards)

print(letters[16:13:-1])     #qpo
print(letters[4::-1])        #edcba
print(letters[:17:-1])       #zyxwvuts

#Common pything silcing idioms

print(letters[-4:])    #last 4 items
print(letters[-1:])    #last item only
print(letters[:1])     #first item only
