# Christopher Hunt
# CS 161
# Final Project

#~~~~ Pokedex Class ~~~~#

from pokemon import Pokemon

class Pokedex:
    def __init__(self, owner, num_of_pokemon, dex, dex_path):
        self.owner = owner
        self.num = num_of_pokemon
        self.dex = dex
        self.dexpath = dex_path


    ########################
    # Function: buildDex
    # Description: Takes the path attribute to the dex.txt file and formats it into
    #           a list of Pokemon objects. Assigns dex to pokedex object.
    def buildDex(self):
        temp_lines = []
        with open(self.dexpath) as dex_input:
            temp_lines = dex_input.readlines()
        lines = []
        for line in temp_lines:
            lines.append(line.replace("\n",""))

        dex = []
        for i in range(0,len(lines),2):
            num_name_type = lines[i].split(" ")
            moves = lines[i+1].split(" ")
            temp_poke = Pokemon(int(num_name_type[0]), num_name_type[1], num_name_type[2], moves)
            dex.append(temp_poke)
        self.dex = dex
    

    #################
    # Function: signIn
    # Description: Introduction screen to the pokedex, allows the user to set the objects attributes
    def signIn(self):
        name = input("******POKEDEX******\n\nUSER: ")
        self.owner = name
        #dex_path = input("Relative path to Dex: ")
        #self.dexpath = dex_path
        self.buildDex() 
        self.num = len(self.dex)
    

    ##################
    # Function: selectionLoop
    # Description: Allows the user to cycle through various modes that the pokedex offers
    def selectionLoop(self):
        game_on = True
        while(game_on):
            print("\n1. Search by Dex Number\n2. Search by Name\n3. Search by Type\n4. Add Pokemon\n5. Exit\n")
            selection = int(input(":: "))
            try:
                if(selection == 1):
                    self.searchByDex()
                elif(selection == 2):
                    self.searchByName()
                elif(selection == 3):
                    self.searchByType()
                elif(selection == 4):
                    self.addPokemon()
                elif(selection == 5):
                    game_on = False
                else:
                    print("\nPlease input an integer from 1-5\n")
            except:
                print("\nInput an integer from 1-5\n")
    

    ####################
    # Function: searchByDex
    # Description: Allows the user to search their pokedex list for a pokemon based on pokedex number
    def searchByDex(self):
        try:
            found = False
            choice = int(input("\nEnter Dex Number: "))
            for i in range(0,len(self.dex)):
                if (self.dex[i].dexnum == choice):
                    found = True
                    print(f"\nDex Number: {self.dex[i].dexnum}\nName: {self.dex[i].name}\nType: {self.dex[i].type}\nMoves: {self.dex[i].moves[0]}, {self.dex[i].moves[1]}, {self.dex[i].moves[2]}, {self.dex[i].moves[3]}")
                    answer = input("Would you like to add this pokemon to your battle roster? [y/n]")
                    if (answer == "y"):
                        self.writeFile(self.dex[i])
            if (found == False):
                print("No pokemon matches that dex number.")
        except:
            print("\nYou must input an integer.\n")
    

    ######################
    # Function: searchByName
    # Description: Allows user to search pokedex by pokemon name
    def searchByName(self):
        found = False
        choice = input("\nEnter Name: ")
        for i in range(0,len(self.dex)):
            if (self.dex[i].name == choice):
                found = True
                print(f"\nDex Number: {self.dex[i].dexnum}\nName: {self.dex[i].name}\nType: {self.dex[i].type}\nMoves: {self.dex[i].moves[0]}, {self.dex[i].moves[1]}, {self.dex[i].moves[2]}, {self.dex[i].moves[3]}")
                answer = input("Would you like to add this pokemon to your battle roster? [y/n]")
                if (answer == "y"):
                    self.writeFile(self.dex[i])
        if (found == False):
            print("No pokemon matches that name.")


    ######################
    # Function: searchByType
    # Description: Allows user to search pokedex by pokemon type
    def searchByType(self):
        found = False
        choice = input("\nEnter Type: ")
        for i in range(0,len(self.dex)):
            if (self.dex[i].type == choice):
                found = True
                print(f"\nDex Number: {self.dex[i].dexnum}\nName: {self.dex[i].name}\nType: {self.dex[i].type}\nMoves: {self.dex[i].moves[0]}, {self.dex[i].moves[1]}, {self.dex[i].moves[2]}, {self.dex[i].moves[3]}")
                answer = input("Would you like to add this pokemon to your battle roster? [y/n]")
                if (answer == "y"):
                    self.writeFile(self.dex[i])
        if (found == False):
            print("No pokemon matches that type.")


    ####################
    # Function: addPokemon
    # Description: Allows user to add a pokemon to their pokedex file. Also updates the current dex list
    def addPokemon(self):
        dex_file_out = open(self.dexpath, "at")
        print("So you caught a new pokemon!")
        print("Let's enter in it's information.")
        number = input("Dex Number: ")
        name = input("Name: ")
        type = input("Type: ")
        move1 = input("Move 1: ")
        move2 = input("Move 2: ")
        move3 = input("Move 3: ")
        move4 = input("Move 4: ")
        moves = [move1, move2, move3, move4]
        dex_file_out.write(f"\n{number} {name} {type}\n{moves[0]} {moves[1]} {moves[2]} {moves[3]}")
        new_poke = Pokemon(int(number), name, type, moves)
        self.dex.append(new_poke)
        self.num = self.num + 1
        dex_file_out.close()


    ###########################
    # Function: writeFile
    # Description: Used within other pokedex methods. Allows the user to write a searched for pokemon to 
    #           a file. This file could be the roster that will be used in the arena object.
    def writeFile(self, pokemon):
        file_path = input("Please input path to file: ")
        pokemon_file = open(file_path, "at")
        pokemon_file.write(f"{pokemon.dexnum} {pokemon.name} {pokemon.type}\n{pokemon.moves[0]} {pokemon.moves[1]} {pokemon.moves[2]} {pokemon.moves[3]}\n")
        print("Pokemon has been added to your battle roster!")

    
