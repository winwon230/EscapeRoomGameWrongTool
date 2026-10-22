lava = 1 #might need to lower the lava with certain actions so the game's still playable
deathLava = 5
clockNumber = 0
clockActive = False
hiding = False

database = {
    "items":[], #this is for perma items like the watch
    "carryableItems":[],
    "roomsComplete":[]
}

currentRoom = "ROOM1"

leverUsed = False #room 1 content
cabinetOpened = False #room 1 content

room2LockOpened = False #room 2 content
room1Peeked = False

clothingCorrect = False #room 3 content
georgeSolved = False
gooberSolved = False
receptionScenePlayed = False
hatEquipt = ""
shirtEquipt = ""
pantsEquipt = ""

print("You wake up in a crusty bed... You're in a dark room with red valves at the floor and a small layer of lava\n"
        "A clock sits on the wall, with no number (?) on it, and its gears aren't moving... You look around.\n"  
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
        if("KEYROOM1" not in database["carryableItems"]):
            print("\nThe door is locked. \n The lava rises.")
            lava += 1
            print("\nCurrent lava level:" + str(lava))
        elif("KEYROOM1" in database["carryableItems"]):
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
        if("KEYROOM1" not in database["carryableItems"]):
            print("\nYou find a dirty key.\n The lava rises.")
            database["carryableItems"].append("KEYROOM1")
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
            if(clockActive == True and clockNumber == 2):
                print("the clock ticks")

            elif(clockActive == True and clockNumber != 2):
                clockNumber -= 1
                if(clockNumber == 0):
                    print("\nThe clock ticks for the final time. You shiver...\n"
                    "\nA white-eyed Capybara in grubby surgical scrubs walks in and stares you blank in the face. You're paralyzed as your vision fades from the edges.\n"
                      "\nFreedom fades from sight...") # death text
                    break

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
                    currentRoom = "ROOM3A"
                    print("\n You arrive through the hole in the wall to a dimly lit room with dirty walls. Oddly enough, the door behind you seals shut, and the lava stops dripping. To your left, a sleepy looking bear in security uniform stands,"
                          " and to your right, a door. \nThe bear looks at you drowsily and mumbles, 'Protocol One-Twenty...' It points at a sign on the wall which says:\n"
                          "\n 'Correct uniform required for reception entry.'\n")
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

        elif(action == "4"):
                print("\n You see the clock, it reads the number 2.\n"
                      "\n It ticks, now reading 1. The feeling of impending doom intensifies and the lava rises.\n")
                clockNumber -= 1 #No need for clock active thing
                print("\n Current lava level:" + str(lava))
                room1Peeked = True

        else:
            print("You can't do that. Get back in line.")
            continue

    if(clockNumber == 0 and clockActive == True):
            if(hiding == True):
                print("\nThe lights flash outside the cabinet as a white-eyed Capy bara in surgical srubs walks past.\n"
                      "It turns toward you, staring at the cabinet blankly. It then turns back and continues, walking through (?) the wall...")
                lava += 1
                print("\n The lava rises.\n" "\nCurrent lava level:" + str(lava))
                clockActive = False
            elif(hiding == False):
                print("\nThe clock ticks for the final time. You shiver...\n"
                    "\nA white-eyed Capybara in grubby surgical scrubs walks in and stares you blank in the face. You're paralyzed as your vision fades from the edges.\n"
                      "\nFreedom fades from sight...") # death text
                break
        
while("ROOM3" not in database["roomsComplete"]):
    if(clockActive == True):
        clockNumber -= 1
        print("\nYour watch's gears tick, and it shows the number: " + str(clockNumber))
    if(clockNumber == 0 and clockActive == True):
            print("\nThe watch ticks for the final time. You shiver...\n"
                    "\nThe red-eyed reindeer reaches you, knocking you over as it flashes a jagged, toothy, grin. You're paralyzed as your vision fades from the edges.\n"
                      "\nFreedom fades from sight...") # death text
            break
    if(lava >= deathLava):
        print("\nThe lava reaches you. Freedom fades from sight...")
        break
    if(currentRoom == "ROOM3A"):
        print("\nWhat do you do?\n")
        if(receptionScenePlayed == False):
            print("1. Try to talk to the guard\n")
        print("2. Open the door\n")

        action = input("What do you do? Choose a number.")

        if(action == "1"):
            if(clothingCorrect == False):
                print("\nThe guard looks at you blankly with a drowsy smile. 'Protocol One-Twenty', it says again, before pulling a sandwich out of its pocket and chewing it.") #rise lava
                print("\nThe lava rises.\n" "\nCurrent lava level:" + str(lava))
            elif(clothingCorrect == True and receptionScenePlayed == False):
                print("\nThe guard blinks at you and opens the door without another word.\n") #put reception etntry stuff and maintain lava level here
                print(("\nYou enter a brightly lit room that very weirdly, empty. The only piece of furniture there is a reception desk, where a wide-eyed reindeer sits, typing away at a keyboard.\n"
                       "It looks up at you, eyes flicking to white like a camera shutter, and in a robotic voice, says, 'Collect your lift ticket, sir.'\n"
                       "You walk over to it and take a white paper ticket from him, which simply says, 'conform, direction: Touching Base' on it...\n"
                       "\n\nThe reindeers' eyes suddenly flicker red, and a gutteral, unworldly scream escapes its mouth, as its skin starts morphing.\n\n"
                       "\nYour watch ticks to two urgently, as a sense of panic rushes through your skin. A message appears on it. 'RUN.'"))
                database["items"].append("RECEPTIONTICKET")
                clockNumber = 3
                clockActive = True
                receptionScenePlayed = True
                currentRoom == "ROOM3C"

        elif(action == "2"):
            print("\nYou enter another dimly lit room with a cabinet labelled 'meds' to your left. There's a lift door on the wall, with a ticket machine next to it.\n"
              "There are two patient rooms, one labelled 'George' and the other,  'Goober'.")
            currentRoom = "ROOM3B"

        else:
            print("\nYou can't do that. Get back in line.")
            continue

    elif(currentRoom == "ROOM3B"):
        print("\nWhat do you do?\n")
        print("1. Open the med cabinet\n")
        print("2. Try the lift\n")
        print("3. Enter George's room\n")
        print("4. Enter Goober's room\n")
        print("5. Change clothes\n")
        print("6. Go back to the guard's room")

        action = input("Choose a number: \n")

        if(action == "1"):
            print("You find: \n" 
                  "\n1. Expired bottles of antibiotic syrup\n" 
                  "2. An old pack of band-aids\n" 
                  "3. A popsicle (how is it still cold?)...\n")
            #make it so you can only take one or two at a time so you actually have to think about which one to take
            action = input("\n Which one do you take?") #idk if i should make decisions like this not increase the lava level
            if(action == "1"):
                database["carryableItems"] = [] #clears the database so other items get removed (watch is in separate database)
                database["carryableItems"].append("ANTIBIOTICS")
                print("You take the antibiotic syrup, it's cherry flavoured. Ew...")

            elif(action == "2"):
                database["carryableItems"] = []
                database["carryableItems"].append("BANDAID")
                print("You take a band-aid, which somehow have an expiry date...")

            elif(action == "3"):
                database["carryableItems"] = []
                database["carryableItems"].append("POPSICLE")
                print("You take the popsicle. It looks tasty...")

            else:
                print("\nYou can't do that. Get back in line.")
                continue

        elif(action == "2"):
            if("RECEPTIONTICKET" in database["items"]):
                clockActive = False
                print("\nYour hands are shaking as you shove the ticket into the ticket machine as you look behind your back... The elevator door opens to an unusally shiny floor, which must've been cleaned recently.\n"
                      "The door just manages to slam shut as the red-eyed reindeer receptionist slams into it with a hungry look in its eyes. You turn to face the control panel.\n"
                      "There's only one button, which simply says, 'G'. You click it, it must be the way out...") #continue writing the next part and logic
                database["roomsComplete"].append("ROOM3")
            else:
                print("\nA ticket machine sits next to the elevator with a red light. There doesn't seem to be any other way to open the elevator...")

        elif(action == "3"):
            if("ANTIBIOTICS" in database["carryableItems"] and georgeSolved == False):
                print("\nGeorge grins at you, his eyes flicking back from white, 'Finally! I love the cherry flavour too!'\n"
                      "He then takes a second look at you... 'Oh yes, the clothes!' he exclaims.\n"
                      "He hands you a Polar fleeced hat and shirt, and a pair of Threaded trousers.\n"
                      "'You'll look spiffing in these,' he says, as you leave the room with the clothes...") #add the correct clothing to the database
                database["items"].extend(["P_HAT", "P_SHIRT", "T_PANTS"])

            elif("ANTIBIOTICS" not in database["carryableItems"] and georgeSolved == False):
                print("\nYou enter a patient room, with a bed in the middle. In the bed, lies a giraffe, with a badge on his gown that says, 'George'.\n"
                      "As he looks up to you from his newspaper (which is from 1989?), he jolts, startled.\n"
                      "\n'Who are you?' he says.\n His eyes go white for a second before his expression calms.\n"
                      "\nAs you're about to respond, he interrupts your thoughts.\n"
                      "\n'Nevermind, I don't need to know. I don't get any visitors at all, so you're welcome! You don't look particularly well dressed, but I need my medicine.'\n"
                      "\n 'What medicine do you need?' you ask.\n"
                      "\nHis eyes go white and his facial expression changes, his teeth arranging themselves into a snarl.\n"
                      "\n He stares at you, and his voice is robotic, as if playing a recording:\n"
                      "'Patient 10-5, external coverage ineffective. Condition persistent. Administer [REDACTED] treatment immediately.'")

            elif(georgeSolved == True):
                print("\nGeorge looks up at you, with a cup of antibiotic syrup in his hand and smiles. He then continues to sip the syrup.")

        elif(action == "4"):
            if("POPSICLE" in database["carryableItems"] and gooberSolved == False):
                print("\nGoober's eyes are back to normal, as he offers you a toothy smile, 'My favourite, thanks!'\n"
                      "'Personally, I think your clothes look a bit weird...' he says as he looks you over again.\n"
                      "\nHe pulls some clothes out of his bag, handing you a Threaded hat, an Orange shirt, and a Polar fleeced pair of trousers.\n"
                      "'Here, I think you'll look nice in these,' he says, before turning back to pack his stuff, as you walk out the room...")
                database["items"].extend(["T_HAT", "O_SHIRT", "P_PANTS"])

            elif("POPSICLE" not in database["carryableItems"] and georgeSolved == False):
                print("\nYou enter a patient (?) room, except it has no medical equipment(?). There's white line markings on the floor and bright lighting.\n"
                      "You hear the bouncing of a volleyball, looking up to see a pink dinosaur in a patient gown with a badge that says, 'Goober'\n"
                      "He catches the volleyball and turns to look at you, before waving at you.\n" \
                      "\n'Hi' he says. 'Who are you?'\n"
                      "\nYou're about to respond, but weirdly enough, WHO are you? You stand there speechless, looking stupid...\n"
                      "\n'Anyways, I don't really care. Apparently there's a volleyball court outside, but the capybara doctor said I needed my treatment...'\n"
                      "\nHis eyes flick to white, and his voice turns robotic, as if playing a recording:\n"
                      "'Patient 8, external coverage ineffective. Administer [REDACTED] treatment immediately.'")
            elif(gooberSolved == True):
                print("\nGoober sits on the floor with the popsicle in his mouth, packing his volleyball into his backpack.\n"
                      "\n'Thanks! You should play Duos with me some time...' he says with a smile.\n"
                      "\nHe turns back to his things, and continues packing stuff.")

        elif(action == "5"):
            if("P_HAT" in database["items"] or "T_HAT" in database["items"]):
                print("\nYou have: \n") #insert the clothes that player has
                if("P_HAT" in database["items"] and "T_HAT" not in database["items"]):
                    print("\n1. A Polar fleeced hat,\n"
                          "2. A Polar fleeced shirt,\n"
                          "3. And a pair of Threaded trousers\n")
                    action = input("\n What do you put on (in order of top to bottom, for example 12 for the hat/shirt or 123 for all of them)?\n")
                    if("1" in action and hatEquipt != "P_HAT"):
                        print("\n You put on the Polar fleeced hat.") #Insert script that checks if a hats already on and 
                        hatEquipt = "P_HAT"
                    if("2" in action and shirtEquipt != "P_SHIRT"):
                        print("\n You put on the Polar fleeced shirt.")
                        shirtEquipt = "P_SHIRT"
                    if("3" in action and pantsEquipt != "T_PANTS"):
                        print("\n You put on the Threaded Trousers")
                        pantsEquipt = "T_PANTS"

                elif("T_HAT" in database["items"] and "P_HAT" not in database["items"]):
                    print("\n1. A Threaded hat,\n"
                          "2. An Orange shirt\n"
                          "3. And a pair of Polar fleeced pants\n")
                    action = input("\n What do you put on (in order of top to bottom, for example 12 for the hat/shirt or 123 for all of them)?\n")
                    if("1" in action and hatEquipt != "T_HAT"):
                        print("\n You put on the Threaded hat.") #Insert script that checks if a hats already on and 
                        hatEquipt = "T_HAT"
                    if("2" in action and shirtEquipt != "O_SHIRT"):
                        print("\n You put on the Orange shirt.")
                        shirtEquipt = "O_SHIRT"
                    if("3" in action and pantsEquipt != "P_PANTS"):
                        print("\n You put on the Polar fleeced pants")
                        pantsEquipt = "P_PANTS"

                elif("T_HAT" in database["items"] and "P_HAT" in database["items"]):
                    print("\n1. A Polar fleeced hat,\n"
                          "2. A Polar fleeced shirt,\n"
                          "3. And a pair of Threaded trousers\n"
                          "4. A Threaded hat,\n"
                          "5. An Orange shirt\n"
                          "6. And a pair of Polar fleeced pants\n")
                    action = input("\n What do you put on (in order of top to bottom, for example 12 for the hat/shirt, but all at once won't work)?\n")
                    if(("1" in action and "4" in action) or ("2" in action and "5" in action) or ("3" in action and "6" in action)):
                        print("\nWhat are you even thinking? How are you meant to put two things on at the same time?\n"
                              "Goober walks out of his room and slaps you across the face. You feel an immense sense of shame...")
                    if("1" in action and hatEquipt != "P_HAT"):
                        print("\nYou put on the Polar fleeced hat.") #Insert script that checks if a hats already on and 
                        hatEquipt = "P_HAT"
                    if("2" in action and shirtEquipt != "P_SHIRT"):
                        print("\nYou put on the Polar fleeced shirt.")
                        shirtEquipt = "P_SHIRT"
                    if("3" in action and pantsEquipt != "T_PANTS"):
                        print("\nYou put on the Threaded trousers")
                        pantsEquipt = "T_PANTS"
                    if("4" in action and hatEquipt != "T_HAT"):
                        print("\nYou put on the Threaded hat.") #Insert script that checks if a hats already on and 
                        hatEquipt = "T_HAT"
                    if("5" in action and shirtEquipt != "O_SHIRT"):
                        print("\nYou put on the Orange shirt.")
                        shirtEquipt = "O_SHIRT"
                    if("6" in action and pantsEquipt != "P_PANTS"):
                        print("\nYou put on the Polar fleeced pants")
                        pantsEquipt = "P_PANTS"

                if(hatEquipt == "P_HAT" and shirtEquipt == "O_SHIRT" and pantsEquipt == "T_PANTS"):
                    clothingCorrect = True;
                else:
                    clothingCorrect = False;
                print("\n You leave the room, heading back to the guard's area.")
                currentRoom = "ROOM3A"
            else:
                print("\nYou don't currently have any extra clothes to change into.\n")

        elif(action == "6"):
            print("\nYou walk back to the guard's room.")
            currentRoom = "ROOM3A"

    elif(currentRoom == "ROOM3C"):
        print("\nYour breathing is heavy as you rush into the room where the guard is. You'd try speak to him but you don't think you have time.")
        currentRoom = "ROOM3A"

while("ROOM4" in database["roomsComplete"]):
    print("\nThe lift bell rings with a bright tone, and the doors open, but you can't see anything (?)...\n"
          "There's simply an extremely bright light and suddenly this voice inside your head turns to a whisper.\n"
          "You solved it. You escaped. But for what?\n"
          "You might be out of the confines of the hospital, but you're still trapped. You'll never escape the lava that never stops rising, or the clock that never stops ticking until it finally does.\n"
          "\nWhat is the point? \n")
    response = input("\nWhat IS the point?\n")
    if(response == "idk"):
        print("\nThat's ok. Perhaps finding the point is the point...")
    elif(response == "there is no point"):
        print("\nThen why does Goober keep playing volleyball? The ball will keep bouncing...")
    elif(response != "there is no point" or response != "idk"):
        print("\nidk what you just said, but thanks for playing the game. It was always just a game...")
    print("\n\nCREDITS: Winston Wong, sole creator and coder of the game. Thx for playing, it was really interesting making this game, it's my first big project in Python.")
