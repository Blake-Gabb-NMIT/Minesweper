#this will store all the map generation modules. 
import random





def FreshMap (sise): #this just auto makes a array to the sise needed and will auto fill with blanks
    multi_list = [[0 for col in range(sise)] for row in range(sise)]

    for row in range(sise):
        for col in range(sise):
            multi_list[row][col]= "[]" # is what a blank square will be rep'ed by
    return multi_list



def bombMaker (bombs,sise):
    x=0
    locationsX = []
    locationsY = []
    while x < bombs:
        locationsX.append(random.randint(0,sise))
        locationsY.append(random.randint(0,sise))
        x+=1
    return locationsX, locationsY
        

