from readchar import readchar
from os import system
from random import randint


MAP_WIDTH = 20
MAP_HEIGHT = 15
PLAYER_X = 0
PLAYER_Y = 0


def createmapobj():
    map_objects = []
    for x in range(10):
        map_objects.append([randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)])
    return map_objects

def removemapobj(map_object: list, map_objects: list):
    map_objects.remove(map_object)

def drawmap(plposx: int, plposy: int, map_objects: list):
    system("clear")
    print("Use wasd to move or q to end the game")
    print("+" + "-"*(MAP_WIDTH*3) + "+")
    for y in range(MAP_HEIGHT + 1):
        print("|", end="")
        for x in range(MAP_WIDTH ):
            map_object = [x, y]
            if map_object in map_objects:
                if plposx == map_object[0] and plposy == map_object[1]:
                    print(" x ", end="")
                    removemapobj(map_object, map_objects)
                else:
                    print(" * ", end="")
            elif plposx == x and plposy == y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-"*(MAP_WIDTH*3) + "+")

def moveplayer  (player_x, player_y, map_objects):
    move = readchar()
    endgame = False
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
    drawmap(player_x, player_y, map_objects)
    return [player_x, player_y, endgame]

def main ():
    player_x = PLAYER_X
    player_y = PLAYER_Y
    endgame = False
    params = []
    map_objects = createmapobj()
    drawmap(PLAYER_X, PLAYER_Y, map_objects)
    while not endgame:
        params = moveplayer(player_x, player_y, map_objects)
        player_x = params[0]
        player_y = params[1]
        endgame = params[2]

main()