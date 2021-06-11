from graphics import *
from squares import Square
import math
import random
import keyboard
from game import Game
r = lambda: random.randint(0,255)
rp = lambda: random.randint(0,100)
dims = 3
#dims = input("Enter the dimension you would like")

def main():
    color_game = Game(dims)
    done = color_game.startGame()
    color_game.playGame(dims, done)

main()