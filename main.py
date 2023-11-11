from readchar import readchar
from os import system
import json

MAP_WIDTH = 20
MAP_HEIGHT = 15
PLAYER_X = 0
PLAYER_Y = 0

def drawmap(plposx: int, plposy: int):
    system("clear")
    print("Use wasd to move or q to end the game")
    print("+" + "-"*(MAP_WIDTH*3 ) + "+")
    for y in range(MAP_HEIGHT):
        print("|", end="")
        for x in range(MAP_WIDTH):
            if(plposx == x and plposy == y):
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-"*(MAP_WIDTH*3 ) + "+")

def moveplayer  (player_x, player_y):
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
                player_x = MAP_WIDTH-1
            
        case "s":
            player_y += 1
            if player_y == MAP_HEIGHT:
                player_y = MAP_HEIGHT-1
        case "d":
            player_x += 1
            if player_x == MAP_WIDTH:
                player_x = 0
        case "q":
            endgame = True
    drawmap(player_x, player_y)
    return [player_x, player_y, endgame]

def main ():
    player_x = PLAYER_X
    player_y = PLAYER_Y
    endgame = False
    params = []
    drawmap(PLAYER_X, PLAYER_Y)
    while not endgame:
        params = moveplayer(player_x, player_y)
        player_x = params[0]
        player_y = params[1]
        endgame = params[2]
            

main()