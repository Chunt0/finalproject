# Christopher Hunt
# CS 161
# Final Project

#~~~~ Pokemon Class ~~~~#

# Very simple class, created as a way to package data into an easily accessable format
class Pokemon:
    def __init__(self,dex_number, name, type, moves):
        self.dexnum = dex_number
        self.name = name
        self.type = type
        self.moves = moves