# Christopher Hunt
# CS 161
# Final Project

#~~~~ Driver ~~~~#

import random
from arena import Arena
from trainer import Trainer
from pokemon import Pokemon
from pokedex import Pokedex



###################
# Fucntion: buildPokeDict
# Description: Takes two files, one with keys and the other with values, formats them and turns them into lists.
#           Zips the lists together and turns it into a dictionary Returns dictionary
def buildPokeDict():
    with open("./data/pokekeys.txt") as keys:
        temp_poke_keys = keys.readlines()
    poke_keys = []
    for key in temp_poke_keys:
        poke_keys.append(key.replace("\n",""))

    with open("./data/pokevalues.txt") as values:
        temp_poke_values = values.readlines()
    poke_values = []
    for value in temp_poke_values:
        value = value.replace("\n", "")
        value = value.split("\t")
        poke_values.append(value)

    poke_dict = dict(zip(poke_keys, poke_values))
    
    return poke_dict

########################
# Function: typeEffectivenessMatrix
# Description: Takes file and creates a 2d matrix of the various pokemon types and their
#           associated attack effectiveness. Rows correspond to the attackers type, columns for defenders type
#           Each column and row corresponds to a particular pokemon type whose index is reflected by the type_list 
def typeEffectivenessMatrix():
    with open("./data/typeeffectiveness.txt") as values:
        temp_matrix = values.readlines()
    effective_matrix = []
    for row in temp_matrix:
        row = row.replace("\n","")
        row = row.split(",")
        effective_matrix.append(row)
    return effective_matrix

#######################
# Function: typeList
# Description: Takes the list of types in the order that corresponds to the rows and collumns
#       of the type effectiveness matrix. Returns these strings as a list.
def typeList():
    with open("./data/typelist.txt") as types:
        temp_type_list = types.readlines()
    type_list = temp_type_list[0].split(",")   
    return type_list

######################
# Function: buildCompRoster
# Description: Uses the poke dictionary object and a list of all the pokemon to create a random roster
#       of three pokemon for the computer opponent to use during battle mode.
def buildCompRoster(dictionary):
    with open("./data/pokekeys.txt") as poke:
        temp_poke_list = poke.readlines()
    poke_list = []
    for poke in temp_poke_list:
        poke_list.append(poke.replace("\n", ""))
    comp_roster = []
    for i in range(0,3):
        num = random.randint(0,800)
        pokemon = poke_list[num]
        type = dictionary.get(pokemon)[0]
        temp_pokemon = Pokemon(num+1, pokemon, type, [] )
        comp_roster.append(temp_pokemon)
    comp_roster = tuple(comp_roster)
    return comp_roster

####################
# Function: main
# Description: Main program driver.
def main():
    poke_dict = buildPokeDict()
    effective_matrix = typeEffectivenessMatrix()
    type_list = typeList()
    print("Welcome to the Ultimate Pokemon Battle Arena!!!")
    print("\nTo begin, let's create your pokedex and build your pokemon roster.")
    print("Your roster must only have 3 pokemon. Use your pokedex to search for pokemon.\nWhen you have found the pokemon you want, type 'y' to write it to the your roster file when prompted.\n")
    player_pokedex = Pokedex("", 0 , [], "./data/dex.txt")
    player_pokedex.signIn()
    player_pokedex.selectionLoop()
    player = Trainer(player_pokedex.owner, player_pokedex,[])
    player.buildRoster("./data/roster.txt")
    comp_roster = buildCompRoster(poke_dict)
    comp = Trainer("Giovanni", [], comp_roster)
    battle_conditions = [False, [0,0], [], []]
    
    print("\nYou are now entering the battle arena!\n")
    battle_arena = Arena(player, comp, poke_dict, battle_conditions)
    battle_arena.gameMode(effective_matrix, type_list)


if __name__ == "__main__":
    main()
