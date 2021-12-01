# finalproject

So for this project I decided to make a pokemon inspired mini game. 

driver.py is the main driver, which imports the class modules that I have built.

When testing this program you must make sure that your terminal is in the main folder which
contains the two folders: data, designs, as well as the five different python scripts.

This project uses the text files stored in the data folder to build the pokedex object, build
the battle roster, build the pokemon dictionary, build the type effectiveness matrix, and the type list.

There's kind of a lot going on and I did my best to describe each function that I 
built out for this project and I hope that that will be able to provide enough context.

In arena.py I used this class attribute called self.bc (bc stands for battle conditions) to 
hold the critical values that will be used during the battle mode. This decision, now looking back
may not have been the most clear. There was a lot of occassions where I had to reference the current pokemon in play
and retrieve some stat from that pokemon and well, it kind of makes the code hard to read and understand...

ex:  print(f"{self.human.name}: {self.human.roster[self.bc[1][0]].name} HP: {self.bc[2][self.bc[1][0]][1]}")

This line is printing the human players name, then the name of that players current pokemon
in play, then it prints it's current HP points.

I got to a point where going back and switching everything out for something a little more readable 
became too daunting of a task. Hopefully all of that wont be too much of a problem.



Another thing to note is with regards to building your roster. As it stands the driver 
builds the players roster from this path: "./data/roster.txt" this can be found on 
line 97 of driver.py. If you wish to change the path, at this point you would have to go into the code
and change it manually. I bring this up though because in the pokedex section of the program
you are able to output a searched pokemon to a file (essentially building your own roster),
my recommendation would be to use the path "./data/roster.txt" to build your 
own roster if you so desire, but you can use any path you wish.
