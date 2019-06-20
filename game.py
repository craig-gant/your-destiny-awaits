#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import time
import sys

answer = input("Would you like to play a game? ")

if answer.lower().strip() == "yes":
    #intro to the adventure, which will present three options to the player
    answer = input("\nYou wake to find yourself in a dimly lit stone corridor with rough wooden doors set in each side "
                   "every few paces.\nThere are no markings or discernible differences amongst the doors that you can see."
                   "\nLook down the corridor in either direction reveals the same view from the dim light.\nYou note that "
                   "you don't see any source of the light.\nThere are no lights overhead or on the walls.\n\nWhat will you do?\n\n"
                   "a. Open the door to your RIGHT.\n"
                   "b. Open the door to your LEFT.\n"
                   "c. Walk further down the corridor.\n"
                   "(Enter: 'a', 'b' or 'c'): ")

    if answer.lower().strip() == "a":
        print("\n\nYou reach for the handle of the door immediately to your right.\nThe handle is neither warm nor cold to the touch.\n"
              "The wood of the door looks old, but in sound condition, and for the first time you notice that\n"
              "there are faint carvings around the door inlay unlike anything you have seen before.\n"
              "You pause to trace your finger along the strange shapes and symbols,")

        #pausing and printing a series of dots for dramatic effect
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)

        print("And start back from the door in pain!\n")

        time.sleep(1)
        print("Buried in your finger is a large splinter from the door, and a small spot of blood.\n"
              "You stick your finger in your mouth and quickly grab the handle of the door and turn.\n\n"
              "It's locked.\n\n"
              "What will you do?\n\n"
              "a. Open the door behind you.\n"
              "b. Walk further down the corridor.\n"
              "(Enter: 'a' or 'b'): ")


else:
    print("That's too bad!")