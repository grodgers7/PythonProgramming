activity = input("What wold you like to do today? ")

if "cinema" not in activity.casefold():     # converts to lowercase but can handle other languages compared to .lower()
    print("I want to go to the cinema")
