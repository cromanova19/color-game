from graphics import *
from squares import Square
from utils import Utils
import math
import random
import keyboard
r = lambda: random.randint(0,255)
rp = lambda: random.randint(0,255)
xd = 500
yd = 500
win = GraphWin("Game", xd, yd)
redVals = []
greenVals = []
blueVals = []
colors = []

class Game:
    def __init__(self, dims):
        self.dims = dims

    def startGame(self):
        dims = self.dims
        utils = Utils()
        tsq = dims**2
        scale = xd/dims
        print('Starting the Game')
        self.gen_new()
        for a in range(tsq):
            posx = a%(dims)
            posy = math.floor(a/dims)
            wg = (dims-posy)/dims
            xp = (posx/dims)
            yp = (posy/dims)
            color = utils.genGradient(xp, yp, scale, redVals, greenVals, blueVals, wg, posx, posy)
            Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
            Sq.generate()
            colors.append(color)
            
        """random.shuffle(colors)
        for a in range (tsq):
            posx = a%(dims)
            posy = math.floor(a/dims)
            color = colors[a]
            Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
            Sq.generate()"""
            
        return win
    
    def gen_old(self):
        redVals.append(20)
        greenVals.append(200)
        blueVals.append(200)
        
        redVals.append(205)
        greenVals.append(20)
        blueVals.append(150)
        
        redVals.append(255)
        greenVals.append(255)
        blueVals.append(0)
    
    def gen_new(self):
        redVals.append(r())
        greenVals.append(r())
        blueVals.append(r())

        for a in range (3):
            ra = rp()
            redVals.append((blueVals[0]+ra)%255)
            #redVals.append(redVals[0]+ra*(math.floor(ra+redVals[0])/255)*-1)
            ra = rp()
            greenVals.append((blueVals[0]+ra)%255)
            #greenVals.append(greenVals[0]+ra*(math.floor(ra+greenVals[0])/255)*-1)
            ra = rp()
            blueVals.append((blueVals[0]+ra)%255)
            #blueVals.append(blueVals[0]+ra*(math.floor(ra+blueVals[0])/255)*-1)
        for a in range (4):
            color = '#%02X%02X%02X' % (int(redVals[a]), int(greenVals[a]), int(blueVals[a]))
            print (str(color))












"""for a in range (3):
    redVals.append(r())
    greenVals.append(r())
    blueVals.append(r())"""
    