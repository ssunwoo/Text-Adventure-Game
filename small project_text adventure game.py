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
    def show(self) :    #for debugging
        print(self.invt)
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
    print("If you want to move, type like 'go north'.")
    title_screen_selections()

DESCRIPTION = 'description'
NPC = ''
N = 'north'
E = 'east'
S = 'south'
W = 'west'

forest_map = {
    'loc1' : {
        DESCRIPTION : "\nYou are standing in the forest and there is a note in your pocket.\nTwo paths lead north and east.",
        N : 'loc2',
        E : 'loc3',
        S : 'loc1',
        W : 'loc1'
    },
    'loc2' : {
        DESCRIPTION : "\nThere is a small pond and a path leads east.",
        N : 'loc2',
        E : 'loc4',
        S : 'loc1',
        W : 'loc2'
    },
    'loc3' : {
        DESCRIPTION : "\nThere is a pine tree and a path leads north.",
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
    
    if direction.lower() == 'north' :
        myPlayer.location = forest_map[myPlayer.location][N]
    elif direction.lower() == 'east' :
        myPlayer.location = forest_map[myPlayer.location][E]
    elif direction.lower() == 'south' :
        myPlayer.location = forest_map[myPlayer.location][S]
    elif direction.lower() == 'west' :
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

def main_game() :
    print("----------------------------------------")
    while True :
        if myPlayer.location == 'loc1' :
            print(forest_map[myPlayer.location][DESCRIPTION])
            cmd = input(">> ").split()
            if len(cmd) == 2 :
                if cmd[0].lower() in ['go', 'walk'] :
                    player_move(cmd[1])
                elif cmd[0].lower() in ['look', 'examine', 'check', 'inspect', 'read'] and cmd[1].lower() == 'note' :
                    print("! Find the exit and get out of this forest !")
                else :
                    wrong_input()
            else :
                print("Enter one action first and one object after.")

        if myPlayer.location == 'loc2' :
            print(forest_map[myPlayer.location][DESCRIPTION])
            cmd = input(">> ").split()
            if len(cmd) == 2 :
                if cmd[0].lower() in ['go', 'walk'] :
                    player_move(cmd[1])
                elif cmd[0].lower() in ['look', 'examine', 'check', 'inspect'] and cmd[1].lower() == 'pond' :
                    print("You can see clear water with fish swimming.")
                elif cmd[0].lower() in ['put', 'place', 'release'] and cmd[1].lower() == 'fish' :
                    if 'a fish' in myPlayer.invt :
                        myPlayer.rmv('a fish')
                        myPlayer.take('a ring')
                        print("You release the fish then she bring a ring.")
                    else :
                        print("You don't have a fish.")
                else :
                    wrong_input()
            else :
                print("Enter one action first and one object after.")

        if myPlayer.location == 'loc3' :
            print(forest_map[myPlayer.location][DESCRIPTION])
            cmd = input(">> ").split()
            if len(cmd) == 2 :
                if cmd[0].lower() in ['go', 'walk'] :
                    player_move(cmd[1])
                elif cmd[0].lower() in ['look', 'examine', 'check', 'inspect'] and cmd[1].lower() == 'tree' :
                    print(forest_map[myPlayer.location][NPC])
                elif (cmd[0].lower() in ['take', 'get', 'bring'] and cmd[1].lower() == 'key') or (cmd[0].lower() in ['give', 'hand'] and cmd[1].lower() == 'ring') :
                    if 'a ring' in myPlayer.invt :
                        myPlayer.rmv('a ring')
                        myPlayer.take('a key')
                        forest_map[myPlayer.location][NPC] = "Looks like the crow is gone."
                        print("He drops the key and you take it.")
                    else :
                        print("You don't have any shiny stuff to trade.")
                else :
                    wrong_input()
            else :
                print("Enter one action first and one object after.")

        if myPlayer.location == 'loc4' :
            print(forest_map[myPlayer.location][DESCRIPTION])
            cmd = input(">> ").split()
            if len(cmd) == 2 :
                if cmd[0].lower() in ['go', 'walk'] :
                    player_move(cmd[1])
                elif cmd[0].lower() in ['look', 'examine', 'check', 'inspect'] and cmd[1].lower() == 'puddle' :
                    print(forest_map[myPlayer.location][NPC])
                elif cmd[0].lower() in ['take', 'get', 'bring'] and cmd[1].lower() == 'fish' :
                    if 'a fish' not in myPlayer.invt :
                        myPlayer.take('a fish')
                        forest_map[myPlayer.location][NPC] = "It's empty."
                        print("Ok...")
                    else :
                        print("You already have a fish.")
                else :
                    wrong_input()
            else :
                print("Enter one action first and one object after.")

        if myPlayer.location == 'loc5' :
            print(forest_map[myPlayer.location][DESCRIPTION])
            cmd = input(">> ").split()
            if len(cmd) == 2 :
                if cmd[0].lower() in ['go', 'walk'] :
                    player_move(cmd[1])
                elif cmd[0].lower() in ['look', 'examine', 'check', 'inspect'] and cmd[1].lower() in ['leaves', 'ivy'] :
                    print("There's nothing special about the leaves.")
                elif cmd[0].lower() in ['move'] and cmd[1].lower() in ['leaves', 'ivy'] :
                    print("In disturbing the leaves, an wooden door is revealed.")
                elif cmd[0].lower() in ['look', 'examine', 'check', 'inspect'] and cmd[1].lower() == 'door' :
                    print("The door is locked")
                elif (cmd[0].lower() in ['open', 'push', 'pull'] and cmd[1].lower() == 'door') or (cmd[0].lower() in ['use'] and cmd[1].lower() == 'key') :
                    if 'a key' in myPlayer.invt :
                        myPlayer.rmv('a key')
                        print("You use the key to open the door and exit the forest!")
                        sys.exit()
                    else :
                        print("You need a key to unlock the door.")
                else :
                    wrong_input()
            else :
                print("Enter one action first and one object after.")

title_screen()