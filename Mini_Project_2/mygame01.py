#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

from rooms import rooms
from rooms import monsters
from rooms import monsters_dict
from os import system, name

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      help
      show
      shoot [monster]
      exit
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    print('Minerals:', minerals)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if "monster" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['monster'])
        print('Monster HP', monsters_dict[rooms[currentRoom]['monster']]['hp'])
    print('Your HP:', health)
    print('Your Attack:', attack)
    print("---------------------------")

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# an inventory, which is initially empty
inventory = []
minerals = 0
health = 40
attack = 0
# start the player in the Hall
currentRoom = 'Entry'

clear()

showInstructions()
input("Press Enter to continue...")

# breaking this while loop means the game is over
while True:
    clear()
    
    if health <= 0:
        print(f"A {rooms[currentRoom]['monster']} killed you")
        input("Press enter to continue")
        break

    showStatus()
    
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    
    #teleport
    if move[0] == 'tele':
        currentRoom = move[1].title()

    #if they type 'go' first
    if move[0] == 'go':
        #check if monster still alive
        if 'monster' in rooms[currentRoom]:
            print(f"The {rooms[currentRoom]['monster']} attacks you!")
            print(f"You lose 10 health")
            health -= 10
            input("Press Enter to continue")
            continue

        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            if rooms[currentRoom]['item'] == 'stim pack':
                print('Enter stim to use. Stimming will deplete 10 health for 10 attack.')
            if rooms[currentRoom]['item'] == 'gauss rifle':
                attack += 8
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    #shows which direction players can go
    if move[0] == 'show':
        print(f"You can go the following direcitons: ")
        for dirs in list(rooms[currentRoom].keys()):
            if not dirs == 'item':
                print(dirs)
    
    #shows instructions
    if move[0] == 'help':
        showInstructions()
    
    #exits the game
    if move[0] == 'exit':
        print("Thank you for playing!")
        break

    #upgrade
    if move[0] == 'upgrade':
        try:
            upChoice = input(f'Would you like to upgrade you guass rifle for {rooms[currentRoom]["upgrade"]} minerals? [y/n]')
            if upChoice == 'y':
                if (minerals - rooms[currentRoom]['upgrade']) < 0:
                    print("You don't have enough minerals.")
                else:
                    attack += 8
                    minerals -= rooms[currentRoom]['upgrade']
                    rooms[currentRoom]['upgrade'] += 5
            elif upChoice == 'n':
                print('good luck')
            else: 
                print('Not a valid response')
        except:
            print("You must be in the Engineering Bay to upgrade.")
    #stim
    if move[0] == 'stim':
        if health == 1:
            print('You cannot stim anymore')
        elif (health -10) <= 0:
            print('You are now at 1 healt and gained 10 attack. You cannot stim anymore.')
            health = 1
            attack += 10
        else: 
            print("You lose 10 health and gain 10 attack.")
            health -= 10
            attack += 10
    
    #attempts to shoot the monster
    if move[0] == 'shoot':
        if 'gauss rifle' in inventory:
            try:
                if move[1] == f'{rooms[currentRoom]["monster"]}':
                    monsters_dict[rooms[currentRoom]['monster']]['hp'] -= attack
                    if monsters_dict[rooms[currentRoom]['monster']]['hp'] <= 0: 
                        print(f'You killed the {rooms[currentRoom]["monster"]}')
                        print(f'You obtained {monsters_dict[rooms[currentRoom]["monster"]]["reward"]} minerals')
                        minerals += monsters_dict[rooms[currentRoom]['monster']]['reward']
                        if rooms[currentRoom]['monster'] == 'zergling':
                            monsters_dict['zergling']['hp'] = 35
                        elif rooms[currentRoom]['monster'] == 'hydralisk':
                            monsters_dict['hydralisk']['hp'] = 75
                        del rooms[currentRoom]["monster"]
                    else:
                        print(f'You shot the {rooms[currentRoom]["monster"]}')
                        print(f'You did {attack} damage')
                        input("Press Enter to continue")
                        continue
            except:
                print(f"You can\'t shoot {move[1]}")
                input("Press Enter to continue")
                continue
        else:
            print(f'You don\'t have a gun!')
            input("Press Enter to continue")
            continue

    ## If a player enters a room with a monster
    if 'monster' in rooms[currentRoom] and 'zergling' in rooms[currentRoom]['monster']:
        print(f'You see a {rooms[currentRoom]["monster"]} in the {currentRoom}.')
    
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    
    input("Press Enter to continue")

