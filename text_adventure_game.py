#Text Adventure Game

import sys
import os
import time
import random

class Player :
    def __init__(self) :
        self.location = 'loc1'
        self.invt = []
    def take(self, item) :
        self.invt.append(item)
    def rmv(self, item) :
        self.invt.remove(item)
    def show(self) :
        print("Inventory", self.invt)

myPlayer = Player()

def title_screen_selections() :
    while True :
        option = input(">> ")
        if option.lower() == "play" :
            main_game()
        elif option.lower() == "help" :
            help_menu()
        elif option.lower() == "quit" :
            sys.exit()
        else :
            print("Please enter a valid command.")

def title_screen() :
    os.system('clear')
    print("########################################")
    print("#  Welcome to the Text Adventure Game  #")
    print("########################################")
    print("                - Play -                ")
    print("                - Help -                ")
    print("                - Quit -                ")
    title_screen_selections()

def help_menu() :
    print("Enter what you would like to do with 'action' and 'object'.")
    print("For example, use 'look' with 'note' to examine a note.")
    print("You can look, examine, check, inspect, take, get, bring, give, hand, ...")
    print("If you want to move, enter 'go' or 'walk' with direction.")
    print("Type direction like 'north' or you can also use 'n', 'up', 'u'.")
    title_screen_selections()

DESCRIPTION = 'description'
NPC = ''
N = 'north', 'n', 'up', 'u'
E = 'east', 'e', 'right', 'r'
S = 'south', 's', 'down', 'd'
W = 'west', 'w', 'left', 'l'

forest_map = {
    'loc1' : {
        DESCRIPTION : "\nYou are standing in the forest and there is a note in your pocket.\nTwo paths lead north and east.",
        N : 'loc2',
        E : 'loc3',
        S : 'loc1',
        W : 'loc1'
    },
    'loc2' : {
        DESCRIPTION : "\nThere is a small pond and paths lead south and east.",
        N : 'loc2',
        E : 'loc4',
        S : 'loc1',
        W : 'loc2'
    },
    'loc3' : {
        DESCRIPTION : "\nThere is a pine tree and paths lead north and west.",
        NPC : "On the tree a crow has a key and it seems like because of his preference of shiny things.",
        N : 'loc4',
        E : 'loc3',
        S : 'loc3',
        W : 'loc1'
    },
    'loc4' : {
        DESCRIPTION : "\nThere are paths to the south and west. You can also see the sunlight from east.\nThere is a tiny puddle at yout feet.",
        NPC : "A poor fish is barely breathing in it.",
        N : 'loc4',
        E : 'loc5',
        S : 'loc3',
        W : 'loc2'
    },
    'loc5' : {
        DESCRIPTION : "\nYou are in a clearing, with trees all around you.\nOn one side, there is an ivy-covered wall.",
        N : 'loc5',
        E : 'loc5',
        S : 'loc5',
        W : 'loc4'
    }
}

def wrong_direction() :
    wd = ["It's a dead end.",
          "It's impossible to go.",
          "There's no way.",
          "There's nothing but trees.",
          "You can't go that way.",
          "You are going to be lost."]
    rn = random.randint(0, 5)
    print(wd[rn])

def player_move(direction) :
    temp = myPlayer.location
    
    if direction in ['north', 'n', 'up', 'u'] :
        myPlayer.location = forest_map[myPlayer.location][N]
    elif direction in ['east', 'e', 'right', 'r'] :
        myPlayer.location = forest_map[myPlayer.location][E]
    elif direction in ['south', 's', 'down', 'd'] :
        myPlayer.location = forest_map[myPlayer.location][S]
    elif direction in ['west', 'w', 'left', 'l'] :
        myPlayer.location = forest_map[myPlayer.location][W]
    
    if temp != myPlayer.location :
        print("You go", direction)
    else :
        wrong_direction()

def wrong_input() :
    wi = ["Pardon?",
          "Try differently",
          "I cannot understand."]
    rn = random.randint(0, 2)
    print(wi[rn])    

def text_effect(text) :
    for t in text :
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def main_game() :
    print("----------------------------------------")
    while True :
        if myPlayer.location == 'loc1' :
            text_effect(forest_map[myPlayer.location][DESCRIPTION])
            command = input(">> ").split()
            cmd = [i.lower() for i in command]
            if cmd[0] in ['go', 'walk'] :
                player_move(cmd[1])
            elif cmd[0] in ['look', 'examine', 'check', 'inspect', 'read'] and 'note' in cmd[1:] :
                print("! Find the exit and get out of this forest !")
            elif cmd[0] in ['help', 'hint'] :
                print("You can read something or walk somewhere.")
            else :
                wrong_input()

        if myPlayer.location == 'loc2' :
            text_effect(forest_map[myPlayer.location][DESCRIPTION])
            command = input(">> ").split()
            cmd = [i.lower() for i in command]
            if cmd[0] in ['go', 'walk'] :
                player_move(cmd[1])
            elif cmd[0] in ['look', 'examine', 'check', 'inspect'] and 'pond' in cmd[1:] :
                print("You can see clear water with fish swimming.")
            elif cmd[0] in ['put', 'place', 'release'] and 'fish' in cmd[1:] :
                if 'a fish' in myPlayer.invt :
                    myPlayer.rmv('a fish')
                    myPlayer.take('a ring')
                    print("You release the fish then she bring a ring.")
                else :
                    print("You don't have a fish.")
            elif cmd[0] in ['help', 'hint'] :
                print("This pond is home of fish.")
            else :
                wrong_input()

        if myPlayer.location == 'loc3' :
            text_effect(forest_map[myPlayer.location][DESCRIPTION])
            command = input(">> ").split()
            cmd = [i.lower() for i in command]
            if cmd[0] in ['go', 'walk'] :
                player_move(cmd[1])
            elif cmd[0] in ['look', 'examine', 'check', 'inspect'] and 'tree' in cmd[1:] :
                print(forest_map[myPlayer.location][NPC])
            elif (cmd[0] in ['take', 'get', 'bring'] and 'key' in cmd[1:]) or (cmd[0] in ['give', 'hand'] and 'ring' in cmd[1:]) :
                if 'a ring' in myPlayer.invt :
                    myPlayer.rmv('a ring')
                    myPlayer.take('a key')
                    forest_map[myPlayer.location][NPC] = "Looks like the crow is gone."
                    print("He drops the key and you take it.")
                else :
                    print("You don't have any shiny stuff to trade.")
            elif cmd[0] in ['help', 'hint'] :
                print("Did you look at the tree and find the crow? Did you give him something?")
            else :
                wrong_input()

        if myPlayer.location == 'loc4' :
            text_effect(forest_map[myPlayer.location][DESCRIPTION])
            command = input(">> ").split()
            cmd = [i.lower() for i in command]
            if cmd[0] in ['go', 'walk'] :
                player_move(cmd[1])
            elif cmd[0] in ['look', 'examine', 'check', 'inspect'] and 'puddle' in cmd[1:] :
                print(forest_map[myPlayer.location][NPC])
            elif cmd[0] in ['take', 'get', 'bring'] and 'fish' in cmd[1:] :
                if 'a fish' not in myPlayer.invt :
                    myPlayer.take('a fish')
                    forest_map[myPlayer.location][NPC] = "It's empty."
                    print("Ok...")
                else :
                    print("You already have a fish.")
            elif cmd[0]in ['help', 'hint'] :
                print("You can take something from the puddle.")
            else :
                wrong_input()

        if myPlayer.location == 'loc5' :
            text_effect(forest_map[myPlayer.location][DESCRIPTION])
            command = input(">> ").split()
            cmd = [i.lower() for i in command]
            if cmd[0] in ['go', 'walk'] :
                player_move(cmd[1])
            elif cmd[0] in ['look', 'examine', 'check', 'inspect'] and ('leaves' in cmd[1:] or 'ivy' in cmd[1:] or 'wall' in cmd[1:]) :
                print("There's nothing special about the leaves.")
            elif cmd[0] in ['move'] and ('leaves' in cmd[1:] or 'ivy' in cmd[1:]) :
                print("In disturbing the leaves, an wooden door is revealed.")
            elif cmd[0] in ['look', 'examine', 'check', 'inspect'] and 'door' in cmd[1:] :
                print("The door is locked")
            elif (cmd[0] in ['open', 'push', 'pull'] and 'door' in cmd[1:]) or (cmd[0] in ['use'] and 'key' in cmd[1:]) :
                if 'a key' in myPlayer.invt :
                    myPlayer.rmv('a key')
                    print("You use the key to open the door and exit the forest!")
                    sys.exit()
                else :
                    print("You need a key to unlock the door.")
            elif cmd[0] in ['help', 'hint'] :
                print("Did you examine the leaves and try to move them?")
            else :
                wrong_input()

        myPlayer.show()

title_screen()
