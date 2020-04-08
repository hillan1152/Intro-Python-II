from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

player_name = input("What is your name --> ")

# Make a new player object that is currently in the 'outside' room.
new_player = Player(player_name, room['outside'])
print(" ")
print(
    f"Welcome {new_player.name.upper()}, you are currently {new_player.curr_room.name}")
print(" ")
print(" ")

direction = ["n", "s", "e", "w"]
# Write a loop that:
while True:
    # * Prints the current room name
    print(f"Current Location: {new_player.curr_room.name}")
# * Prints the current description (the textwrap module might be useful here).
    print(" ")
    print(f"{new_player.curr_room.description}")
    print(" ")
# * Waits for user input and decides what to do.
    dirInput = input("Which Direction Will you go --> ").lower()
    print(" ")
    if dirInput == "q":
        break
    elif dirInput in direction:
        print(" ")
        print(f"Moving {dirInput}")
        print(" ")
        if dirInput == "n":
            if new_player.curr_room.n_to is not None:
                new_player.curr_room = new_player.curr_room.n_to
            else:
                print(" ")
                print("Can't Go That Way")
                print(" ")
        elif dirInput == "e":
            if new_player.curr_room.e_to is not None:
                new_player.curr_room = new_player.curr_room.e_to
            else:
                print(" ")
                print("Can't Go That Way")
                print(" ")
        elif dirInput == "w":
            if new_player.curr_room.w_to is not None:
                new_player.curr_room = new_player.curr_room.w_to
            else:
                print(" ")
                print("Can't Go That Way")
                print(" ")
        elif dirInput == "s":
            if new_player.curr_room.s_to is not None:
                new_player.curr_room = new_player.curr_room.s_to
            else:
                print(" ")
                print("CHOOSE NEW DIRECTION: Can't Go That Way")
                print(" ")
    else:
        print("Please choose a valid command")

        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
