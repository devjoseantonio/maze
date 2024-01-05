#Library to use wasd to move
from readchar import readchar
#Library to clear the map in the console
from os import system
#Library to create random integers
from random import randint

#Map dimensions
MAP_WIDTH = 20
MAP_HEIGHT = 15

#Player initial position
PLAYER_X = 0
PLAYER_Y = 0
PLAYER_POS = [PLAYER_X, PLAYER_Y]

#Number of map objects
NUM_MAPOBJ = 10


#This method creates the objects in the map
def createmapobj():
    map_objects = []
    while len(map_objects) < NUM_MAPOBJ:
        new_obj = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
        if new_obj not in map_objects and new_obj != PLAYER_POS:
            map_objects.append(new_obj)
    return map_objects

#This method removes an object from the map
def removemapobj(map_object: list, map_objects: list):
    map_objects.remove(map_object)


#This method draws the map and all the objects in it
def drawmap(plposx: int, plposy: int, map_objects: list, tail_len: int, tail: list):
    touch_tail = False
    system("clear")
    print("Use wasd to move or q to end the game")
    print("+" + "-"*(MAP_WIDTH*3) + "+")
    for y in range(MAP_HEIGHT + 1):
        print("|", end="")
        for x in range(MAP_WIDTH ):
            map_object = [x, y]
            if map_object in map_objects:
                if plposx == map_object[0] and plposy == map_object[1]:
                    print(" @ ", end="")
                    tail_len += 1
                    removemapobj(map_object, map_objects)
                else:
                    print(" * ", end="")
            elif (plposx == x and plposy == y) :
                print(" @ ", end="")
                if([plposx, plposy] in tail):
                    tail_len = -1
            elif ([x, y] in tail):
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-"*(MAP_WIDTH*3) + "+")
    
    return tail_len

#This method is used to move the player on any direction
def moveplayer  (player_x, player_y, map_objects, tail_len, tail):
    move = readchar()
    endgame = False
    tail.insert(0, [player_x, player_y])
    match move:
        case "w":
            player_y -= 1
            if player_y < 0:
                player_y = 0
        case "a":
            player_x -= 1
            if player_x < 0:
                player_x = MAP_WIDTH -1
            
        case "s":
            player_y += 1
            if player_y > MAP_HEIGHT:
                player_y = MAP_HEIGHT
        case "d":
            player_x += 1
            if player_x > MAP_WIDTH - 1:
                player_x = 0
        case "q":
            endgame = True
    tail = tail[:tail_len]
    tail_len = drawmap(player_x, player_y, map_objects, tail_len, tail)
    if tail_len == -1:
        endgame = True
        print("Has muerto!")
    return [player_x, player_y, tail_len, endgame]

#This is the main method and initializes the program
def main ():
    tail_len = 0
    player_x = PLAYER_X
    player_y = PLAYER_Y
    endgame = False
    params = []
    tail = []
    map_objects = createmapobj()
    drawmap(PLAYER_X, PLAYER_Y, map_objects, tail_len, tail)
    while not endgame:
        params = moveplayer(player_x, player_y, map_objects, tail_len, tail)
        player_x = params[0]
        player_y = params[1]
        tail_len = params[2]
        endgame = params[3]

main()