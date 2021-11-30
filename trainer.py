# Christopher Hunt
# CS 161
# Final Project

#~~~~ Trainer Class ~~~~#

from pokemon import Pokemon

class Trainer:
    def __init__(self, name, pokedex, roster):
        self.name = name
        self.pokedex = pokedex # Pokedex object
        self.roster = roster # Tuple of pokemon selected from the pokedex
    
    ###########################
    # Function: buildRoster
    # Description: Takes a the path to a file created by the Pokedex and builds
    #           a tuple of Pokemon objects from the first three pokemon on the roster  
    def buildRoster(self, path):
        # Retrieving data from the file
        # and formatting it to be easily packaged as a Pokemon object
        temp_lines = []
        with open(path) as dex_input:
            temp_lines = dex_input.readlines()
        lines = []
        for line in temp_lines:
            lines.append(line.replace("\n",""))

        roster = []
        for i in range(0,len(lines),2):
            num_name_type = lines[i].split(" ")
            moves = lines[i+1].split(" ")
            temp_poke = Pokemon(int(num_name_type[0]), num_name_type[1], num_name_type[2], moves)
            roster.append(temp_poke)
        length = len(roster)
        if (len(roster) > 3):
            for i in range(3, length):
                roster.pop(3)
        self.roster = tuple(roster)