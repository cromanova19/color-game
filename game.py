from tkinter.constants import TRUE
from graphics import *
from squares import Square
from utils import Utils
import math
import random
import keyboard
r = lambda: random.randint(0,255)
rp = lambda: random.randint(100,200)
xd = 750
yd = 750
win = GraphWin("Game", xd, yd)
redVals = []
greenVals = []
blueVals = []
colors = []
done = []


class Game:
    def __init__(self, dims):
        self.dims = dims
        utils = Utils()
        self.corners = utils.genCorners(dims)

    def startGame(self):
        corner = self.corners
        dims = self.dims
        scale = xd/dims
        utils = Utils()
        tsq = dims**2
        print('Starting the Game')
        self.gen_old()
        for a in range(tsq):
            posx = a%dims
            posy = math.floor(a/dims)
            color = utils.genGradient(redVals, greenVals, blueVals, dims, posx, posy)
            Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
            Sq.generate()
            colors.append(color)
        utils.genDots(corner, dims, scale, win)

        done = list.copy(colors)
        time.sleep(2)
        utils.Shuffle(colors, corner)
        for a in range (tsq):
            if a not in corner:
                posx = a%(dims)
                posy = math.floor(a/dims)
                color = colors[a]
                Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
                Sq.generate()
        return done

    def playGame(self, dims, done):
        while not(colors==done):
            corners = self.corners
            utils = Utils()
            scale = xd/dims
            P1 = win.getMouse()
            Ps = utils.squareNumber(scale, P1, dims, corners)
            if len(Ps) != 0:
                utils.highlightSquare(Ps[1], Ps[2], Ps[0], win)
                P2 = win.getMouse()
                Qs = utils.squareNumber(scale, P2, dims, corners)
                if len(Qs) != 0:
                    utils.listSwap(colors, Ps[0], Qs[0])
                    Swap = Square(Ps[1], Ps[2], colors[Ps[0]], win)
                    Swap.generate()
                    Swap = Square(Qs[1], Qs[2], colors[Qs[0]], win)
                    Swap.generate()
                elif True:
                    utils.unHighlight(Ps[1], Ps[2], colors[Ps[0]], win)
            if colors==done:
                print ("You Win!")
            elif True:
                print ("Not done yet!")
            
    
    def gen_old(self):
        redVals.append(255)
        greenVals.append(255)
        blueVals.append(0)
        
        redVals.append(255)
        greenVals.append(0)
        blueVals.append(255)
        
        redVals.append(0)
        greenVals.append(255)
        blueVals.append(255)

        redVals.append(0)
        greenVals.append(0)
        blueVals.append(255)
    
    def gen_new(self):
        redVals.append(r())
        greenVals.append(r())
        blueVals.append(r())

        for a in range (3):
            ra = rp()
            if ra+redVals[a]>255:
                redVals.append(abs(ra-redVals[a]))
            elif True:
                redVals.append(ra+redVals[a])
            ra = rp()
            if ra+greenVals[a]>255:
                greenVals.append(abs(ra-greenVals[a]))
            elif True:
                greenVals.append(ra+greenVals[a])
            ra = rp()
            if ra+blueVals[a]>255:
                blueVals.append(abs(ra-blueVals[a]))
            elif True:
                blueVals.append(ra+blueVals[a])
        for a in range (4):
            color = '#%02X%02X%02X' % (int(redVals[a]), int(greenVals[a]), int(blueVals[a]))
            print (str(color))












"""for a in range (3):
    redVals.append(r())
    greenVals.append(r())
    blueVals.append(r())"""
    