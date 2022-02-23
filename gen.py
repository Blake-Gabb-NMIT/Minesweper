#this will store all the map generation modules. 
import random





def FreshMap (sise): #this just auto makes a array to the sise needed and will auto fill with blanks
    multi_list = [[0 for col in range(sise)] for row in range(sise)]

    for row in range(sise):
        for col in range(sise):
            multi_list[row][col]= "[]" # is what a blank square will be rep'ed by
    return multi_list

def FullMap (mapinfo,bombsx,bombsy): #this will generate a "hidden map", this is how the map will end up being showm
    pass


def bombMaker (bombs,sise):
    x=0
    locationsX = []
    locationsY = []
    while x < bombs:
        locationsX.append(random.randint(0,sise))
        locationsY.append(random.randint(0,sise))
    return locationsX, locationsY
        

