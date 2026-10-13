lava = 1
deathLava = 5
clockNumber = 0

database = {
    "items":[],
    "roomsComplete":[]
}

currentRoom = "ROOM1"

leverUsed = False #room 1 content
cabinetOpened = False #room 1 content

room2LockOpened = False


print("You wake up in a crusty bed... You're in a dark room with red valves at the floor and a small layer of lava\n"
        "A clock ticks, it's currently at 0. You look around.\n"  
        "There's a door, lever, and a cabinet.\n")

while ("ROOM1" not in database["roomsComplete"] and currentRoom == "ROOM1"): # this while block is for room 1
    print("\n What do you do?\n")
    print("1. Open door\n")
    if(leverUsed == False):
        print("2. Flick lever \n")
    if(cabinetOpened == False):
        print("3. Open cabinet \n")

    initialAction = input("\nChoose one of the numbers.\n")
    

    if(initialAction == "1"):
        if("KEYROOM1" not in database["items"]):
            print("\nThe door is locked. \n The lava rises.")
            lava += 1
            print("\nCurrent lava level:" + str(lava))
        elif("KEYROOM1" in database["items"]):
            database["roomsComplete"].append("ROOM1")
            currentRoom = "ROOM2"
            print("\nThe lock clicks and falls to the floor. You enter a white hospital(?) corridor. Lava drips through the closed door.\n"
                  "There's a human-sized cabinet, a blue door to the right, and a red door on the left.")

    elif(initialAction == "2"):
        print("\nThe lava level drops, you can see the floor now.")
        lava -= 1
        leverUsed = True
        print("\nCurrent lava level:" + str(lava))

    elif(initialAction == "3"):
        if("KEYROOM1" not in database["items"]):
            print("\nYou find a dirty key.\n The lava rises.")
            database["items"].append("KEYROOM1")
            lava += 1
            cabinetOpened = True
            print("\nCurrent lava level:" + str(lava))
    else:
        print("\nThat's not allowed. Get back in line.")
        continue

    if(lava >= deathLava): # prolly need to put this in the code for every room
        print("\nThe lava reaches you. Freedom fades from sight...")
        break

while("ROOM2" not in database["roomsComplete"]):
    if(lava >= deathLava):
        print("\nThe lava reaches you. Freedom fades from sight...")
        break
    if(currentRoom == "ROOM2"):
        print("\nWhat do you do?\n")
        print("1. Open cabinet\n") ## add the if conditions later
        print("2. Open blue door\n")
        print("3. Open red door\n")
        
        action = input("\n Choose one of the numbers \n")

        if(action == "1"):
            print("\n It's empty. Seems like a good hiding spot... The lava rises")
            lava += 1
            print("\n Current lava level:" + str(lava))

        if(action == "2"):
            if(room2LockOpened == False):
                print("\nYou stop at a pair of cold, rusty, iron bars... It's very dark inside this room. A 3 digit padlock sits at the handle.")
                givenCode = input("\n What is the code?")
                if(givenCode == "483"):
                    print("\n The rusty door creaks open. A dirty raccoon in a dusty hospital gown looks up at you. \n"
                          "He stares wide-eyed at you... And hands you a torch.\n")
                elif(givenCode != "483"):
                    print("")