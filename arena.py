# Christopher Hunt
# CS 161
# Final Project

#~~~~ Arena Class ~~~~#

import random


class Arena:
    def __init__(self, player, opponent, poke_dict, battle_conditions):
        self.human = player
        self.comp = opponent
        self.dict = poke_dict
        self.bc = battle_conditions # [game_on(T/F), poke_in_play[player, comp], player_stats[[],[],[]] comp_stats[[],[],[]]


    ###########################
    # Function: gameMode
    # Description: Arena's main driver. This function allows the player and comp to battle
    def gameMode(self, effective_matrix, type_list):

        ## Build out comp and player stats in battle conditions list ## 
        for i in range(0,3):
            temp_name = self.human.roster[i].name
            values = self.dict.get(temp_name)
            self.bc[2].append(values)
        
        for i in range(0,3):
            temp_name = self.comp.roster[i].name
            values = self.dict.get(temp_name)
            self.bc[3].append(values)
        ###############################################################


        print(f"Welcome {self.human.name}! Today, your opponent is {self.comp.name}... This should be an interesting match!")
        choice = input("Are you ready to fight!? [y/n] :: ")
        if (choice == "y"):
            self.bc[0] = True
        while(self.bc[0] == True):
            print("\n~~~~ Current Pokemon In Play ~~~~\n")
            print(f"{self.human.name}: {self.human.roster[self.bc[1][0]].name} HP: {self.bc[2][self.bc[1][0]][1]}")
            print(f"{self.comp.name}: {self.comp.roster[self.bc[1][1]].name} HP: {self.bc[3][self.bc[1][1]][1]}")
            if (self.bc[2][self.bc[1][0]][4] >= self.bc[3][self.bc[1][1]][4]):
                print(f"\nPlayer is faster, attacks first!\n")
                selection = (input("What would you like to do?\n1. Fight\n2. Heal\n3. Swap\n:: "))
                if (selection == "1"):
                    self.playerAttack(effective_matrix, type_list)
                elif (selection == "2"):
                    self.playerHeal()
                elif (selection == "3"):
                    self.playerSwap()
                else:
                    print("\nYou made the wrong choice, you skip you turn.\n")
                comp_choice = random.randint(1,3)
                if (comp_choice == 1):
                    self.compAttack(effective_matrix, type_list)
                elif (comp_choice == 2):
                    self.compHeal()
                else:
                    self.compSwap()
            else:
                print(f"\n{self.comp.name} is faster, attacks first!\n")
                comp_choice = random.randint(1,3)
                if (comp_choice == 1):
                    self.compAttack(effective_matrix, type_list)
                elif (comp_choice == 2):
                    self.compHeal()
                else:
                    self.compSwap()
                print("It is now your turn!!")
                selection = (input("What would you like to do?\n1. Fight\n2. Heal\n3. Swap\n:: "))
                if (selection == "1"):
                    self.playerAttack(effective_matrix, type_list)
                elif (selection == "2"):
                    self.playerHeal()
                elif (selection == "3"):
                    self.playerSwap()
                else:
                    print("You made the wrong choice, you skip you turn.")
            print("\n\n\n\n")


    ##################
    # Function: playerAttack
    # Description: Players current pokemon attacks computers current pokemon.
    #           This is determined by the "damage" calculator. The damage is deducted from the pokemons hp located in
    #           self.bc (the battle conditions list).
    def playerAttack(self, effective_matrix, type_list):
        player_type = type_list.index(self.bc[2][self.bc[1][0]][0])
        player_attack = float(self.bc[2][self.bc[1][0]][2])
        comp_type = type_list.index(self.bc[3][self.bc[1][1]][0])
        comp_defense = float(self.bc[3][self.bc[1][1]][3])
        random_num = 0.85 + (random.randint(0,30)/100)
        damage = 15 * (player_attack/comp_defense) * float(effective_matrix[player_type][comp_type]) * random_num
        print(f"\n{self.human.roster[self.bc[1][0]].name} dealt {damage} points of damage to {self.comp.roster[self.bc[1][1]].name}\n")
        self.bc[3][self.bc[1][1]][1] = float(self.bc[3][self.bc[1][1]][1]) - damage
        if (self.bc[3][self.bc[1][1]][1] <= 0):
            self.bc[3][self.bc[1][1]][1] = 0
            print(f"{self.comp.roster[self.bc[1][1]].name} fainted!\n")
            self.compSwap()        

    ##################
    # Function: compAttack
    # Description: Computers current pokemon attacks players current pokemon.
    #           This is determined by the "damage" calculator. The damage is deducted from the pokemons hp located in
    #           self.bc (the battle conditions list).
    def compAttack(self, effective_matrix, type_list):
        print(f"{self.comp.name} chose to attack!\n")
        player_type = type_list.index(self.bc[2][self.bc[1][0]][0])
        player_defense = float(self.bc[2][self.bc[1][0]][3])
        comp_type = type_list.index(self.bc[3][self.bc[1][1]][0])
        comp_attack = float(self.bc[3][self.bc[1][1]][2])
        random_num = 0.85 + ((random.randint(0,30))/100)
        damage = 15 * (comp_attack/player_defense) * float(effective_matrix[comp_type][player_type]) * random_num
        print(f"\n{self.comp.roster[self.bc[1][1]].name} dealt {damage} points of damage to {self.human.roster[self.bc[1][0]].name}\n")
        self.bc[2][self.bc[1][0]][1] = float(self.bc[2][self.bc[1][0]][1]) - damage
        if (self.bc[2][self.bc[1][0]][1] <= 0):
            self.bc[2][self.bc[1][0]][1] = 0
            print(f"{self.human.roster[self.bc[1][0]].name} fainted!\n")
            self.playerSwap()   

    ##################
    # Function: playerHeal
    # Description: Player chooses one of their pokemon to heal by 15 hp.
    def playerHeal(self):
        print(f"Choose a Pokemon to heal: \n1. {self.human.roster[0].name} - HP: {self.bc[2][0][1]}\n2. {self.human.roster[1].name} - HP: {self.bc[2][1][1]}\n3. {self.human.roster[2].name} - HP: {self.bc[2][2][1]}\n")
        selection = int(input(":: "))
        try:
            if (selection == 1 and float(self.bc[2][0][1]) > 0.0):
                max_health = int(self.dict.get(self.human.roster[0].name)[1])
                self.bc[2][0][1] = float(self.bc[2][0][1]) + 15
                if(self.bc[2][0][1] > max_health):
                    self.bc[2][0][1] = max_health
            elif (selection == 2 and float(self.bc[2][1][1]) > 0.0):
                max_health = int(self.dict.get(self.human.roster[1].name)[1])
                self.bc[2][1][1] = float(self.bc[2][1][1]) + 15
                if(self.bc[2][1][1] > max_health):
                    self.bc[2][1][1] = max_health
            elif (selection == 3 and float(self.bc[2][2][1]) > 0.0):
                max_health = int(self.dict.get(self.human.roster[2].name)[1])
                self.bc[2][2][1] = float(self.bc[2][2][1]) + 15
                if(self.bc[2][2][1] > max_health):
                    self.bc[2][2][1] = max_health
            else:
                print("You tried to heal a fainted Pokemon, nothing happened...")
        except:
            print("You needed to enter an integer...try again next time!")

    ##################
    # Function: compHeal
    # Description: Computer randomly selects one of its pokemon to heal by 15 hp.
    def compHeal(self):
        selection = random.randint(1,3)
        if (selection == 1 and float(self.bc[3][0][1]) > 0.0):
            print(f"{self.comp.name} chose to heal {self.comp.roster[0].name}!\n")
            max_health = int(self.dict.get(self.comp.roster[0].name)[1])
            self.bc[3][0][1] = float(self.bc[3][0][1]) + 15
            if(self.bc[3][0][1] > max_health):
                self.bc[3][0][1] = max_health
        elif (selection == 2 and float(self.bc[3][1][1]) > 0.0):
            print(f"{self.comp.name} chose to heal {self.comp.roster[1].name}!\n")
            max_health = int(self.dict.get(self.comp.roster[1].name)[1])
            self.bc[3][1][1] = float(self.bc[3][1][1]) + 15
            if(self.bc[3][1][1] > max_health):
                self.bc[3][1][1] = max_health
        elif (selection == 3 and float(self.bc[3][2][1]) > 0.0):
            print(f"{self.comp.name} chose to heal {self.comp.roster[0].name}!\n")
            max_health = int(self.dict.get(self.comp.roster[2].name)[1])
            self.bc[3][2][1] = float(self.bc[3][2][1]) + 15
            if(self.bc[3][2][1] > max_health):
                self.bc[3][2][1] = max_health
        else:
            pass

    ##################
    # Function: playerSwap
    # Description: Player is given the option to swap for another pokemon in their roster.
    def playerSwap(self):
        print(f"\nWhich Pokemon would you like to swap to?\n1. {self.human.roster[0].name} - HP: {self.bc[2][0][1]}\n2. {self.human.roster[1].name} - HP: {self.bc[2][1][1]}\n3. {self.human.roster[2].name} - HP: {self.bc[2][2][1]}\n")
        try:
            selection = int(input(":: "))
            if (selection == 1 and float(self.bc[2][0][1]) > 0.0):
                self.bc[1][0] = 0
            elif (selection == 2 and float(self.bc[2][1][1]) > 0.0):
                self.bc[1][0] = 1           
            elif (selection == 3 and float(self.bc[2][2][1]) > 0.0):
                self.bc[1][0] = 2
            elif (float(self.bc[2][0][1]) <= 0.0 and float(self.bc[2][1][1]) <= 0.0 and float(self.bc[2][2][1]) <= 0.0):
                print("All of your pokemon have fainted!")
                self.bc[0] = False
            else:
                print("The Pokemon you selected cannot be swapped to, try again.")
                self.playerSwap()
        except:
            print("You needed to enter an integer... try again next time!")

    ##################
    # Function: compSwap
    # Description: Computer randomly selects a pokemon to swap to.
    def compSwap(self):
        selection = random.randint(1,3)
        if (selection == 1 and float(self.bc[3][0][1]) > 0.0):
            print(f"{self.comp.name} chose to swap out their pokemon!\n")
            self.bc[1][1] = 0
        elif (selection == 2 and float(self.bc[3][1][1]) > 0.0):
            print(f"{self.comp.name} chose to swap out their pokemon!\n")
            self.bc[1][1] = 1           
        elif (selection == 3 and float(self.bc[3][2][1]) > 0.0):
            print(f"{self.comp.name} chose to swap out their pokemon!\n")
            self.bc[1][1] = 2
        elif (float(self.bc[3][0][1]) <= 0.0 and float(self.bc[3][1][1]) <= 0.0 and float(self.bc[3][2][1]) <= 0.0):
            print(f"All of {self.comp.name}'s pokemon have fainted!")
            self.bc[0] = False
        else:
            self.compSwap()       

