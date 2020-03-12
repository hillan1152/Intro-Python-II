from room import Room
from player import Player

import os
import re
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

myPlayer = Player(input("Lets get your name: "), room['outside'])
movement = ("n", "e", "s", "w")
print(f"Welcome to the Adventure Game {myPlayer.name} \n\n")
print(f"{myPlayer.current_room.name} is where you must make your first choice. \n Take a hint: {myPlayer.current_room.description}")
print("\n")
print(f"Please Choose a direction {movement}")


while True:
    playerInput = input("-> ")
    if playerInput == "q":
        os.system('clear')
        break
    elif playerInput in movement:
        myPlayer.move(playerInput)
    else:
        print("Please Choose a valid key")


# ---------------------- FROM BEFORE HOURS -------------------------
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
# def tryDirection(d, curRoom):
#     """
#     Try to move a direction, or print an error if the player can't go that way.
#     Returns the room the player has moved to (or the same room if the player
#     didn't move).
#     """
#     attrib = d + '_to'

#     # See if the room has the destination attribute
#     if hasattr(curRoom, attrib):
#         # If so, return its value (the next room)
#         return getattr(curRoom, attrib)

#     # Otherwise print an error and stay in the same room
#     print("You can't go that way")

#     return curRoom 
