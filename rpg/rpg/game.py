
# Main game file

from characters.player import *
from characters.movement import *

import time
import sys
movement = Movement()

commands = {
    'help' : help,
    'exit': exit 
}

player = Player("Default", 1, 1, 1)


def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False

def main(player):
    
    while (not player.dead):
        move = raw_input(">> where to? ")
        input = move.lower()
        print y
        if input == "north":
            movement.north(x, y)          
        elif input == "south":
            movement.south(x, y)
        elif input == "east":
            movement.east(x, y)
        elif input == "west":
            movement.west(x, y)
        
        print "New Co-Ords", coords
            
main (player)

