print("You have tracked down the island that is said to contain a legendary treasure! Now, you just have to find it! Getting off of your ship and onto the island...")
HasKey = False

while True:

    print("\nYou see a giant temple in the distance. It seems to be at the center of the island. There are also some ruins to the left of where you landed and to you right is the remains of an old pirate ship.")
    Choice1 = input(
        "Would you like to go to the 'temple', investigate the 'ruins' or look at the remains of the 'pirate ship'?\n")

    if Choice1 == "temple":
        print("\nAs you are heading towards the temple, you come across a sign that says 'TURN BACK NOW OR SUFFER'. You notice a trail leading from the sign into the woods.")
        Choice1_A = input(
            "Would you like to ignore the sign and continue to the 'temple', take the signs advice and 'turn back', or 'follow the trail' into the woods?\n")
        if Choice1_A == 'temple':
            print("\nYou arrive at the temple! There is a sturdy gate locking the entrance. The gate has a key hole!")
            Choice1_A_1 = input(
                "Would you like to 'enter key', or 'go back' to your boat?\n")
            if Choice1_A_1 == "enter key":
                if HasKey == False:
                    print("\nYou do not the key that goes to this lock, go find it!")
                    print("Now begone!")
                    continue
                if HasKey == True:
                    print(
                        "\nAs you turn the key, the lock drops away revaling a screen that has an equation and a place for you to enter an answer.")
                    print("The equation is (4x3-6+1)3(12÷6+1).")
                    Choice1_A_2 = input(
                        "Would you like to 'enter an answer' or 'go back'?\n")
                    if Choice1_A_2 == "enter an answer":
                        Answer = input("\nWhat is your answer?\n")
                        if Answer == "2":
                            print(
                                "\n\n\nThe gate opens up! You travel into the temple, before your very eyes is more treasure than you could have imagined in your wildest dreams!")
                            print("DING!!!!")
                            print("DING!!!!DING!!!!DING!!!!")
                            print("It's your alarm.")
                            print(
                                "Evidently you could have imagined it in your wildest dreams...")
                            quit()
                        else:
                            print("that answer is not correct! Please try again.")
                            print("Now away with you!")
                            continue
        if Choice1_A == "follow the trail":
            print("\nAs you are walking along the trail, you somehow get lost and find yourself back where you began!")
            continue
        if Choice1_A == "turn back":
            continue

    elif Choice1 == "ruins":
        print("\nThe ruins are mostly rubble, but as you are about to leave, you notice something that catches your eye. There is something engraved into the wall.'These operations once had order, now there is nothing but division amongst the ranks.' There does not seem to be anything else of note around the ruins.")
        Choice1_B = input(
            "there is nothing left to do here, you should 'go back'.\n")
        if Choice1_B == "go back":
            continue

    elif Choice1 == "pirate ship":
        print("\nThe ship is in many pieces, most of which have degraded beyond recognition. However, the cabin seems to be unaturally preseerved. As you approach the door, something begins to appear on the door!\n '2B||!2B'\n  You get the sense that the door is waiting for you to respond...")
        Choice1_C = input(
            "Would you like to forget about this magical nonsense and 'go back' to your boat, or 'respond' to the cabin door?\n")
        if Choice1_C == "respond":
            Response = input("\nWhat would you like to say?\n")
            if Response == "that is the question":
                print(
                    "\nThe door opens! The room is empty except for a key laying in the middle")
                TakeKey = input(
                    "Would you like to take the key? 'yes' or 'no'\n")
                if TakeKey == "yes":
                    HasKey = True
                    print("\nYou take the key, you look down to put it in your pocket and as you look up, you are suddenly standing in the same place you began. You can feel the key still in your pocket.")
                    continue
                if TakeKey == "no":
                    print(
                        "\nYou hear a voice say, then there is no need for you to be here, goodbye!")
                    print("You find yourself back where you began!")
                    continue
            else:
                print(
                    "\nThat is incorrect, better luck next time! Deus Ex Machina something someting, you are back where you started!")
            continue
        if Choice1_C == "go back":
            continue
