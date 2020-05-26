# Modify the program (gamedictionary.py) so that the exits are a dictionary
# rather than a list, with the keys being the numbers of the locations and
# the values being dictionaries holding the exits (as they do at present).
# No Change should be needed to the actual code.

# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can user to determine which way to go.

locations = {0: {"desc": "You are sitting in front of a computer learning Python",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "You are standing at the end of a road before a small brick building",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "You are at the top of a hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "You are inside a building, a well house for a small stream",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "You are in a valley beside a stream",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "You are in the forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

vocabulary = {"QUIT":  "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST":  "E",
              "WEST":  "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
    # exits is the dictionary within the master dictionary that we are calling

    print(locations[loc]["desc"])
    # desc is the description dictionary within master locations dictionary
    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + availableExits + ": ").upper()
    print()
    # parse the user input, using our vocabulary dictionary of necessary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

    # if len(direction) > 1:
    #     for word in vocabulary:
    #         if word in direction:
    #             direction = vocabulary[word]

    #exits = {0: {"Q": 0},
    #          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    #          2: {"N": 5, "Q": 0},
    #          3: {"W": 1, "Q": 0},
    #          4: {"N": 1, "W": 2, "Q": 0},
    #          5: {"W": 2, "S": 1, "Q": 0}}
    #
    # namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
    #               2: {"5": 5},
    #               3: {"1": 1},
    #               4: {"1": 1, "2": 2},
    #               5: {"2": 2, "1": 1}}
