from tkinter.constants import TRUE
from graphics import *
from squares import Square
from utils import Utils
import math
import random
import keyboard
r = lambda: random.randint(0,255)
rp = lambda: random.randint(0,255)
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

    def startGame(self):
        dims = self.dims
        scale = xd/dims
        utils = Utils()
        tsq = dims**2
        print('Starting the Game')
        self.gen_new()
        for a in range(tsq):
            posx = a%dims
            posy = math.floor(a/dims)
            color = utils.genGradient(redVals, greenVals, blueVals, dims, posx, posy)
            Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
            Sq.generate()
            colors.append(color)

        done = list.copy(colors)
        time.sleep(2)
        utils.Shuffle(colors, dims)
        for a in range (tsq):
            posx = a%(dims)
            posy = math.floor(a/dims)
            color = colors[a]
            Sq = Square(Point(posx*scale, posy*scale), Point((posx+1)*scale, (posy+1)*scale), color, win)
            Sq.generate()
        return done

    def playGame(self, dims, done):
        while not(colors==done):
            scale = xd/dims
            P1 = win.getMouse()
            P2 = win.getMouse()
            XP1 = math.floor(P1.getX()/scale)
            XP2 = math.floor(P2.getX()/scale)
            YP1 = math.floor(P1.getY()/scale)
            YP2 = math.floor(P2.getY()/scale)
            V1 = YP1 * dims + XP1%dims
            V2 = YP2 * dims + XP2%dims
            Square1 = Point(XP1 * scale, YP1 * scale)
            Square11 = Point((XP1+1) * scale, (YP1+1) * scale)
            Square2 = Point(XP2 * scale, YP2 * scale)
            Square22 = Point((XP2+1) * scale, (YP2+1) * scale)
            utils = Utils()
            utils.listSwap(colors, V1, V2)
            Swap = Square(Square1, Square11, colors[V1], win)
            Swap.generate()
            Swap = Square(Square2, Square22, colors[V2], win)
            Swap.generate()
            if colors==done:
                print ("You Win!")
            elif 1>0:
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
    