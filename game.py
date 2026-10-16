lava = 1
deathLava = 10
clockNumber = 0
clockActive = False
hiding = False

database = {
    "items":[],
    "roomsComplete":[]
}

currentRoom = "ROOM1"

leverUsed = False #room 1 content
cabinetOpened = False #room 1 content

room2LockOpened = False #room 2 content
room1Peeked = False

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


while("ROOM2" not in database["roomsComplete"]): #room 2 code!
    if(lava >= deathLava):
        print("\nThe lava reaches you. Freedom fades from sight...")
        break

    if(currentRoom == "ROOM2"):
        print("\nWhat do you do?\n")
        print("1. Open cabinet\n") ## add the if conditions later
        print("2. Open blue door\n")
        print("3. Open red door\n")
        if(clockNumber > 0 and room1Peeked == False):
            print("4. Peek back into the previous room\n")
        
        action = input("\n Choose one of the numbers \n")

        if(action != 1):
            hiding = False

        if(action == "1" and clockActive == False):
            print("\n It's empty. Seems like a good hiding spot... The lava rises")
            lava += 1
            print("\n Current lava level:" + str(lava))
            hiding = True

        elif(action == "1" and clockActive == True):
            print("\n You rush inside the cabinet and peek through the holes. The feeling of impending doom eases slightly.\n")
            clockNumber -= 1
            if("WATCH" in database["items"]):
                print("\n The clock ticks. It now shows " + str(clockNumber)) # change to make it you dont see the clock number but either doom calms down
                print("You feel the clicking of the clock gears stop.")
            else:
                print("\n The clock ticks. You feel the clicking of the clock gears stop.")
            hiding = True


        elif(action == "2"):
            if(clockActive == True):
                clockNumber -= 1
            if(room2LockOpened == False):
                print("\nYou stop at a pair of cold, rusty, iron bars... It's very dark inside this room. A 3 digit padlock sits at the handle.")
                givenCode = input("\n What is the code?")
                if(givenCode == "483"):
                    print("\n The rusty door creaks open. A dirty raccoon in a dusty hospital gown looks up at you. \n"
                          "He stares wide-eyed at you... And hands you a watch.\n"
                          "You continue through a hole in the wall.\n")
                    print("Current lava level:" + str(lava))
                    database["items"].append("WATCH")
                    database["roomsComplete"].append("ROOM2")
                    room2LockOpened = True
                elif(givenCode != "483"):
                    print("Wrong code. You turn back. The lava rises.")
                    lava += 1
                    print("\n Current lava level:" + str(lava))
                    
                    

        elif(action == "3"):
            if(clockActive == True):
                clockNumber -= 1
            print("\n You continue down the red corridor, until you reach a room with three snakes in patient gowns tied to chairs.\n"
                  "\n Snake 1 says, 'Both the others are lying.'\n"
                  "\n Snake 2 says, 'None of us are lying.'\n" 
                  "\n Snake 3 says, 'Snake 2 is lying.'\n")
            response = input("\nWho is telling the truth? 1, 2 or 3?")
            if(response == "3"):
                print("Snake 3 gets out of the chair and smiles at you. 'The code is 483', he says, before slithering through (?) the wall... You head back to the main room.")
                #idk if i should rise the lava here
            elif(response != "3"):
                print("The snakes laugh at you as you head back to the main room... The lava rises.")
                lava +=1
                print("\n Current lava level:" + str(lava))
                clockNumber = 2
                print("\n A feeling of impending doom approaches. The clock ticks.")
                clockActive = True
        if(action == "4"):
                print("\n You see the clock, it reads the number 2.\n"
                      "\n It ticks, now reading 1. The feeling of impending doom intensifies and the lava rises.\n")
                clockNumber -= 1 #No need for clock active thing
                print("\n Current lava level:" + str(lava))
                room1Peeked = True

    if(clockNumber == 0 and clockActive == True):
            if(hiding == True):
                print("Monster passes")#insert print for when monster passes
                clockActive = False
            elif(hiding == False):
                print("\nThe clock ticks for the final time. You shiver...\n"
                    "\nA white-eyed Capybara in surgical scrubs walks in and stares you blank in the face. You're paralyzed as your vision fades from the edges.\n"
                      "Freedom fades from sight...") # death text
                break
        
while("ROOM3" not in database["roomsComplete"]):
    print("")