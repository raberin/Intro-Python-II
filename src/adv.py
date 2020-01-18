from room import Room
from player import Player
from item import Item

spacer = '\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons\n"),

    'foyer':    Room("Foyer", """Dim light filters in from the south.\nDusty passages run north and east.\n"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.\n"""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.\n"""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.\n"""),
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

# Items in rooms
room['outside'].items = [Item('sword'), Item('ring')]
room['foyer'].items = [Item('axe')]
room['overlook'].items = [Item('scimitar')]
room['narrow'].items = [Item('claymore')]
room['treasure'].items = [Item('gold'), Item('potion')]


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
    # Displays current location
    print(f"Your current location: {new_player.current_room.name}\n")
    # print(new_player.current_room, new_player.current_room.n_to)
    for current in room:
        if new_player.current_room.name == room[current].name:
            print(room[current].description)
            print('I see a...')
            for item in room[current].items:
                print(item.name)
            print(spacer)

    # Display input options
    print(
        f"Where would you like to go? \n [n] North    [s] South   [e] East    [w] West    [t] Take    [q] Quit")
    choice = input('Please input your choice here: ').lower().split()
    print(choice)
    print(spacer)

    # Error handling for incorrect input
    while choice[0] not in ['n', 's', 'e', 'w', 'q']:
        print(
            "Invalid option. Please, choose: \n[n] North    [s] South   [e] East    [w] West    [q] Quit ")
        choice = input('Please input your choice here: ').lower().split()
        print(spacer)

    # Conditionals for each input and movement between each room
    if len(choice) == 1:
        if choice[0] == 'q':
            print('You are now quitting the game...\n Goodbye!')
            isRunning = False
        elif choice[0] == 'n' and new_player.current_room.n_to != None:
            print(spacer)
            print('You walk north.')
            new_player.current_room = new_player.current_room.n_to
            print(spacer)
        elif choice[0] == 's' and new_player.current_room.s_to != None:
            print(spacer)
            print('You walk south.')
            new_player.current_room = new_player.current_room.s_to
            print(spacer)
        elif choice[0] == 'e' and new_player.current_room.e_to != None:
            print(spacer)
            print('You walk east.')
            new_player.current_room = new_player.current_room.e_to
            print(spacer)
        elif choice[0] == 'w' and new_player.current_room.w_to != None:
            print(spacer)
            print('You walk west.')
            new_player.current_room = new_player.current_room.w_to
            print(spacer)
        else:
            print(
                'You hit a magic barrier that wont let you pass. \n Please choose another direction.')
            print(spacer)
    elif len(choice) == 2:
        print('This is for items placeholder')
