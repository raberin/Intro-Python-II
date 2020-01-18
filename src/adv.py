from room import Room
from player import Player

spacer = '\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'

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
print(spacer)
print('Welcome to the Intro to Python II - Game')

# Make a new player object that is currently in the 'outside' room.
player_name = input('Please input your character name: ')
new_player = Player(player_name, room['outside'])
print(spacer)


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
isRunning = True
while isRunning:
    print(f"Your current location: {new_player.current_room.name}\n")
    for current_room in room:
        if new_player.current_room.name == room[current_room].name:
            print(room[current_room].description)
    print(
        f"Where would you like to go? \n [n] North    [s] South   [e] East    [w] West    [q] Quit")
    choice = input('Please input your choice here: ')
    spacer = '\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'

    while choice not in ['n', 's', 'e', 'w', 'q']:
        print(
            "Invalid option. Please, choose: \n[n] North    [s] South   [e] East    [w] West    [q] Quit ")
        choice = input('Please input your choice here: ')
        spacer = '\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'

    if choice == 'q':
        print('You are now quitting the game...\n Goodbye!')
        isRunning = False
