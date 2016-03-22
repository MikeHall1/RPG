
# Main game file

from characters.player import *
import time
import sys

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
    #print_slow("Hello mighty hero! My name is Luandrith, I'm a level 7 Warlock of the square table.\nWhat might your name be? ")
    #name = raw_input(">> ")
    #player.name = name
    #print_slow("So your name is %r? Huh, that is a strange name, lets get your journey underway!" %name)
    while (not player.dead):
        line = raw_input(">> ")
        input = line.split()
        
        if isValidCMD(input[0]):
            print input[0]
            
        
        print input
 
    
main (player)

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)