from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['rock', 'sword']),

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
player = Player("Dave", room['outside'])


def check_move(current_room, direction):
    move = direction + '_to'
    if hasattr(current_room, move):
        return getattr(current_room, move)
    else:
        print('You cannot move there!')
        return current_room


# print(player)
# Write a loop that:
#
while True:
    # * Prints the current room name
    print(f'{player.name} is now in the {player.current_room.name}.')
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # * Waits for user input and decides what to do.
    move = input("\n>").lower().split()
    if len(move) == 1:
        move = move[0][0]
        if move is 'inventory' or 'i':
            if len(player.inventory) == 0:
                print("There are no items in your inventory.")
            else:
                print(f'Your items: {player.inventory}')
        elif move == 'q':
            print('Exiting game')
            break
        player.current_room = check_move(player.current_room, move)
    elif len(move) == 2:
        item = move[1]
        move = move[0]
        if move == 'get' or 'take':
            # ADD ITEM TO PLAYER'S INVENTORY
            print(item)
            player.get_item(item)
            print(f'You picked up a {item}')
    if move == 'q':
        print('Exiting game')
        break
    player.current_room = check_move(player.current_room, move)

    # move = input("\n>").lower()[0]
    # if move == 'n' or 's' or 'e' or 'w':
    # if player.current_room.n_to is None:
    #     print('You cannot move there!')
    # else:
    #     player.current_room = player.current_room.n_to
    # elif move == 's':
    #     if player.current_room.s_to is None:
    #         print('You cannot move there!')
    #     else:
    #         player.current_room = player.current_room.s_to
    # elif move == 'e':
    #     player.current_room = player.current_room.e_to
    # elif move == 'w':
    #     player.current_room = player.current_room.w_to

    # elif move == 'q':
    #     print('Exiting game')
    #     break

    # else:
    #     print('Invalid direction')
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
