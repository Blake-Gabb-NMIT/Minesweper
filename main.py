import gen, engine



###

grid = 5 #this is the sise of the screen
bombs = 3 #how many bombs are in the sqaure



#filling out maps with info
bombLocationsX, bombLocationsY = gen.bombMaker(bombs,grid) # this will be where the game gens and stores the bombs location to then be added into the viusal display
Visualmap = gen.FreshMap(grid)#this is the map that the user will see, starts off as all blanks
Computersmap = False #this will be the full map and what it should look like how the map looks like fully complete


### 




###start###






engine.renderScreen(Visualmap) # this renders the screen, all it needs is what the player sees
engine.renderScreen(

#end of loop#